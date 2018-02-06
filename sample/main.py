#!/usr/bin/env python3

import argparse
import logging
import mod_config
import mod_version
from colorama import Fore, Style

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
    
    if args.debug:
        logformat =  Fore.RED + '%(asctime)s %(module)s-%(funcName)s %(message)s' + Style.RESET_ALL
        logging.basicConfig(level=logging.DEBUG, format=logformat, datefmt='%m/%d/%Y %H:%M:%S ')
        logging.getLogger().setLevel(logging.DEBUG)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True
        deblog = logging.getLogger(__name__)
        deblog.setLevel(logging.DEBUG)
        deblog.propagate = True
        deblog.debug("[ DEBUG Mode Enabled! ] ")
    if args.verbose:
        logformat =  Fore.BLUE + '%(asctime)s %(module)s-%(funcName)s %(message)s' + Style.RESET_ALL
        logging.basicConfig(level=logging.INFO, format=logformat, datefmt='%m/%d/%Y %H:%M:%S ')
        logging.getLogger().setLevel(logging.INFO)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.INFO)
        requests_log.propagate = True
        verlog = logging.getLogger(__name__)
        verlog.setLevel(logging.INFO)
        verlog.propagate = True
        verlog.info("[ Verbose Mode Enabled! ] ")
    if args.version:
        show_version()
    mod_config.verbose = args.verbose
    mod_config.debug = args.debug


def show_version():
    print("sample version {} ".format(mod_version.__version__))


if __name__ == '__main__':
    main()
