# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import argparse
import logging
import sys

from kube_controller.metacontroller import run_meta
from kube_controller.nativecontroller import run_native


def _setup_logger(level=logging.INFO):
    logger = logging.getLogger()
    logger.setLevel(level)
    log_handler = logging.StreamHandler(sys.stdout)
    fmt = logging.Formatter(fmt='%(asctime)s %(threadName)s %(name)s '
                            '%(levelname)s: %(message)s',
                            datefmt='%F %H:%M:%S')
    log_handler.setFormatter(fmt)
    logger.addHandler(log_handler)


def metacontroller(args):
    run_meta()


def nativecontroller(args):
    run_native()


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
 
    metaparser = subparsers.add_parser("meta")
    metaparser.set_defaults(func=metacontroller)

    nativeparser = subparsers.add_parser("native")
    nativeparser.set_defaults(func=nativecontroller)

    args = parser.parse_args()

    _setup_logger()
    args.func(args)


if __name__ == '__main__':
    main()
