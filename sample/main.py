#!/usr/bin/env python3

import argparse
import logging
import config
from version import __version__


def main():
    """ Main Loop """
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
        print("verbose")
        logging.basicConfig(level=logging.INFO)
        logging.getLogger().setLevel(logging.INFO)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.INFO)
        requests_log.propagate = True
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger().setLevel(logging.DEBUG)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True
    if args.version:
        show_version()
    config.verbose = args.verbose
    config.debug = args.debug


def show_version():
    print("sample version {} ".format(__version__))


if __name__ == '__main__':
    main()
