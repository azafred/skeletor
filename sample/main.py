#!/usr/bin/env python

import argparse
import logging
from settings import *
from version import __version__


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-v', '--verbose', action='store_true', default=False,
        help='Increase log verbosity')
    parser.add_argument(
        '-d', '--debug', action='store_true', default=False,
        help='Debug level verbosity')
    parser.add_argument(
        '--version', action='store_true', default=False,
        help='Show version information', dest='version')

    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.INFO)
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    if args.version:
        show_version()


def show_version():
    print "Sample version %s " % __version__


if __name__ == '__main__':
    main()