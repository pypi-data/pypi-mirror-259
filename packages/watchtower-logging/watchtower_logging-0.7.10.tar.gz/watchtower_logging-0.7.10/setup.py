from setuptools import setup, find_packages
import re
import os


PACKAGE_DIR = os.path.join(os.getcwd(), 'watchtower_logging')
with open(os.path.join(PACKAGE_DIR, 'version.py')) as version_file:
    verstrline = version_file.read().strip()
VSRE = r'^__version__ = [\']([0-9\.]*)[\']'
mo = re.search(VSRE, verstrline, re.M)
if mo:
    VERSION = mo.group(1)
else:
    raise Exception('No version string found')


with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='watchtower_logging',
    version=VERSION,
    description='Logging to WatchTower instance',
    license='MIT',
    packages=find_packages(),
    author='Jacob Noordmans',
    author_email='jacob@graindataconsultants.com',
    keywords=['WatchTower']
)

install_requires = [
    'requests==2.31.0',
    'python-json-logger==2.0.7',
    'pytz==2024.1',
    'packaging==23.2'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)