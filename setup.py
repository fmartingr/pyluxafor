#!/usr/bin/env python3
import os
import re
from setuptools import setup, find_packages
import sys

THIS_PATH = os.path.dirname(os.path.abspath(__file__))
README = open(os.path.join(THIS_PATH, 'README.md')).read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search(
        "^__version__ = ['\"]([^'\"]+)['\"]",
        init_py, re.MULTILINE).group(1)


if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    args = {'version': get_version('luxafor')}
    print("You probably want to also tag the version now:")
    print("  git tag -a %(version)s -m 'version %(version)s'" % args)
    print("  git push --tags")
    sys.exit()


scripts = {
    "console_scripts": [
        "luxa=luxafor.cli:cli",
    ]
}

setup(
    name='luxafor',
    version=get_version('luxafor'),
    description='CLI and libraries to interact with luxafor USB leds',
    long_description=README,
    author='Felipe Martin',
    author_email='me@fmartingr.com',
    url='https://github.com/fmartingr/pyluxafor',
    packages=find_packages(),
    install_requires=(
        "click>=6.0,<=6.7.99",
        "pyusb==1.0.0",
    ),
    entry_points=scripts,
    classifiers=[],
)
