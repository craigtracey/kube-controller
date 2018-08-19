# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import argparse
from kube_controller.metacontroller import run_controller


def metacontroller(args):
    run_controller()


def nativecontroller(args):
    print "native"


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    
    metaparser = subparsers.add_parser("meta")
    metaparser.set_defaults(func=metacontroller)

    nativeparser = subparsers.add_parser("native")
    nativeparser.set_defaults(func=nativecontroller)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
