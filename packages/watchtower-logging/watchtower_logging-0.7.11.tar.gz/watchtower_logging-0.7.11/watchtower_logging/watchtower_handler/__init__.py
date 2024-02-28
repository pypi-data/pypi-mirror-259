import atexit
import logging
import time
import traceback
from threading import Timer

import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from ..version import __version__

instances = []  # For keeping track of running class instances
DEFAULT_QUEUE_SIZE = 5000
DEFAULT_HOST = 'localhost:8855'

# Called when application exit imminent (main thread ended / got kill signal)
@atexit.register
def perform_exit():
    for instance in instances:
        try:
            instance.shutdown()
        except Exception:
            pass


def force_flush():
    for instance in instances:
        try:
            instance.force_flush()
        except Exception:
            pass


def wait_until_empty():
    for instance in instances:
        try:
            instance.wait_until_empty()
        except Exception:
            pass


class WatchTowerHandler(logging.Handler):
    """
    A logging handler to send events to a Watch Tower instance
    """

    def __init__(self,
                 beam_id: str,
                 token: (str, None) = None,
                 host: str = DEFAULT_HOST,
                 use_fallback: bool = True,
                 fallback_host: (str, None) = None,
                 dev: bool = False,
                 debug: bool = False,
                 flush_interval: float = 5.0,
                 force_keep_ahead: bool = False,
                 protocol: str = 'https',
                 queue_size: int = DEFAULT_QUEUE_SIZE,
                 retry_backoff: float = 2.0,
                 retry_count: int = 2,
                 timeout: float = 1.0,
                 verify: bool = True,
                 version: str = __version__):
        """
        Args:
            beam_id (str): The id of the Watchtower beam to send the events to
            token (str): Authentication token
            host (str): The Watchtower host (should include port if necessary)
            fallback_host (str): The Watchtower fallback host, defaults to fallback.<host>
            dev (bool): Whether to send the dev flag with all event
            debug (bool): Whether to print debug console messages
            flush_interval (float): How often to push events to Watchtower in seconds
            force_keep_ahead (bool): Sleep instead of dropping logs when queue fills
            protocol (str): The web protocol to use
            queue_size (int): The max number of logs to queue, set to 0 for no max
            retry_backoff (float): The requests lib backoff factor
            retry_count (int): The number of times to retry a failed request
            timeout (float): The time to wait for a response from Watch Tower
            verify (bool): Whether to perform ssl certificate validation
            version (str): Version string to specify the watchtower-logging library version
        """

        global instances
        instances.append(self)
        logging.Handler.__init__(self)

        self.beam_id = beam_id
        self.host = host or DEFAULT_HOST
        self.use_fallback = use_fallback
        self.fallback_host = fallback_host or 'fallback.' + self.host
        self.token = token
        self.verify = verify
        self.timeout = timeout
        self.flush_interval = flush_interval
        self.force_keep_ahead = force_keep_ahead
        self.log_payload = ""
        self.SIGTERM = False  # 'True' if application requested exit
        self.timer = None
        # It is possible to get 'behind' and never catch up, so we limit the queue size
        self.queue = list()
        self.max_queue_size = max(queue_size, 0)  # 0 is min queue size
        self.debug = debug
        self.session = requests.Session()
        self.retry_count = retry_count
        self.retry_backoff = retry_backoff
        self.protocol = protocol or 'https'
        self.processing_payload = False
        self.version = version
        self.dev = dev

        # Keep ahead depends on queue size, so cannot be 0
        if self.force_keep_ahead and not self.max_queue_size:
            self.write_log('Cannot keep ahead of unbound queue, using default queue size')
            self.max_queue_size = DEFAULT_QUEUE_SIZE

        self.write_debug_log('Starting debug mode')
        self.write_debug_log('Preparing to override loggers')

        # prevent infinite recursion by silencing requests and urllib3 loggers
        logging.getLogger('requests').propagate = False
        logging.getLogger('urllib3').propagate = False

        # and do the same for ourselves
        logging.getLogger(__name__).propagate = False

        # disable all warnings from urllib3 package
        if not self.verify:
            requests.packages.urllib3.disable_warnings()

        if self.verify and self.protocol == 'http':
            self.write_debug_log('cannot use SSL Verify and unsecure connection')

        # Set up automatic retry with back-off
        self.write_debug_log('Preparing to create a Requests session')
        retry = Retry(total=self.retry_count,
                      backoff_factor=self.retry_backoff,  # Retry for any HTTP verb
                      status_forcelist=[500, 502, 503, 504])
        self.session.mount(self.protocol + '://', HTTPAdapter(max_retries=retry))

        self.start_worker_thread()

        self.write_debug_log('Class initialize complete')

    def build_endpoint(self,
                       host: str):

        return '{protocol}://{host}/api/beams/{beam_id}'.format(
            protocol=self.protocol,
            host=host,
            beam_id=self.beam_id)

    def emit(self,
             record):

        self.write_debug_log("emit() called")

        try:
            record = self.format_record(record)
        except Exception as e:
            self.write_log('Exception in WatchTower logging handler: %s' % str(e))
            self.write_log(traceback.format_exc())
            return

        if self.flush_interval <= 0:
            # Flush log immediately; is blocking call
            self._wt_worker(payload=record)
            return

        self.write_debug_log('Writing record to log queue')

        # If force keep ahead, sleep until space in queue to prevent falling behind
        while self.force_keep_ahead and len(self.queue) >= self.max_queue_size:
            time.sleep(self.alt_flush_interval)

        # Put log message into queue; worker thread will pick up
        if not self.max_queue_size or len(self.queue) < self.max_queue_size:
            self.queue.append(record)
        else:
            self.write_log('Log queue full; log data will be dropped.')

    def close(self):

        self.shutdown()
        logging.Handler.close(self)

    #
    # helper methods
    #

    def start_worker_thread(self):

        # Start a worker thread responsible for sending logs
        if self.flush_interval > 0:
            self.write_debug_log('Preparing to spin off first worker thread Timer')
            self.timer = Timer(self.flush_interval, self._wt_worker)
            self.timer.daemon = True  # Auto-kill thread if main process exits
            self.timer.start()

    def write_log(self,
                  log_message: str):

        print('[WatchTowerHandler] ' + log_message)

    def write_debug_log(self,
                        log_message: str):

        if self.debug:
            print('[WatchTowerHandler DEBUG] ' + log_message)

    def format_record(self,
                      record):

        self.write_debug_log('format_record() called')
        record.dev = self.dev
        return self.format(record)


    def _wt_worker(self,
                   payload: (str, None) = None):

        self.write_debug_log("_wt_worker() called")
        if self.flush_interval > 0:
            # Stop the timer. Happens automatically if this is called
            # via the timer, does not if invoked by force_flush()
            self.timer.cancel()
            self.processing_payload = True
            queue_is_empty = self.empty_queue()

        if not payload:
            payload = self.log_payload
            self.log_payload = ""

        if payload:
            self.write_debug_log("Payload available for sending")
            self.write_debug_log("Destination URL is " + self.url)

            try:
                headers = {'Content-Type': 'application/json',
                           'User-Agent': self.user_agent}
                if self.token:
                    headers.update({'Authorization': 'Token {token}'.format(token=self.token)})

                payload = '[{payload}]'.format(payload=payload)

                self.write_debug_log("Sending payload: " + payload)
                do_fallback = False

                try:
                    r = self.session.post(
                        self.url,
                        data=payload,
                        headers=headers,
                        verify=self.verify,
                        timeout=self.timeout
                    )
                    if not r.status_code in (200, 201) and r.status_code >= 500:
                        if self.use_fallback:
                            do_fallback = True
                        else:
                            r.raise_for_status()
                    else:
                        r.raise_for_status()

                except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
                    if self.use_fallback:
                        do_fallback = True
                    else:
                        raise e

                if do_fallback:

                    rf = self.session.post(
                        self.fallback_url,
                        data=payload,
                        headers=headers,
                        verify=self.verify,
                        timeout=self.timeout
                    )
                    rf.raise_for_status()

                self.write_debug_log("Payload sent successfully")

            except Exception as e:
                try:
                    self.write_log("Exception in Watchtower logging handler: %s" % str(e))
                    self.write_log(traceback.format_exc())
                except Exception:
                    self.write_debug_log("Exception encountered," +
                                         "but traceback could not be formatted")

        else:
            self.write_debug_log("Timer thread executed but no payload was available to send")

        # Restart the timer
        if self.flush_interval > 0:
            timer_interval = self.flush_interval
            if self.SIGTERM:
                self.write_debug_log("Timer reset aborted due to SIGTERM received")
            else:
                if not queue_is_empty:
                    self.write_debug_log("Queue not empty, scheduling timer to run immediately")
                    # Start up again right away if queue was not cleared
                    timer_interval = self.alt_flush_interval

                self.write_debug_log("Resetting timer thread")
                self.timer = Timer(timer_interval, self._wt_worker)
                self.timer.daemon = True  # Auto-kill thread if main process exits
                self.timer.start()
                self.write_debug_log("Timer thread scheduled")

        self.processing_payload = False

    def empty_queue(self):

        if len(self.queue) == 0:
            self.write_debug_log("Queue was empty")
            return True

        self.write_debug_log("Recursing through queue")
        if self.SIGTERM:
            self.log_payload += ','.join(self.queue)
            self.queue.clear()
        else:
            # without looking at each item, estimate how many can fit in 50 MB
            apprx_size_base = len(self.queue[0])
            # dont count more than what is in queue to ensure the same number as pulled are deleted
            count = min(int(524288 / apprx_size_base), len(self.queue))
            self.log_payload += ','.join(self.queue[:count])
            del self.queue[:count]
        self.write_debug_log("Queue task completed")

        return len(self.queue) > 0

    def force_flush(self):

        self.write_debug_log("Force flush requested")
        self._wt_worker()
        self.wait_until_empty()  # guarantees queue is emptied

    def shutdown(self):

        self.write_debug_log("Immediate shutdown requested")

        # Only initiate shutdown once
        if self.SIGTERM:
            return

        self.write_debug_log("Setting instance SIGTERM=True")
        self.SIGTERM = True

        if self.flush_interval > 0:
            self.timer.cancel()  # Cancels the scheduled Timer, allows exit immediately

        self.write_debug_log("Starting up the final run of the worker thread before shutdown")
        # Send the remaining items that might be sitting in queue.
        self._wt_worker()
        self.wait_until_empty()  # guarantees queue is emptied before exit

    def wait_until_empty(self):

        self.write_debug_log("Waiting until queue empty")
        while len(self.queue) > 0 or self.processing_payload:
            self.write_debug_log("Current queue size: " + str(len(self.queue)))
            time.sleep(self.alt_flush_interval)

    @property
    def alt_flush_interval(self):

        return min(1.0, self.flush_interval / 2)

    @property
    def user_agent(self):

        return 'watchtower-logging-python/{version}'.format(version=self.version)

    @property
    def url(self):

        return self.build_endpoint(host=self.host)

    @property
    def fallback_url(self):

        return self.build_endpoint(host=self.fallback_host)