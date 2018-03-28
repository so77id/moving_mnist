from __future__ import absolute_import, division, print_function

import argparse


def get_args():
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument(
        '-c',
        '--config_file',
        metavar='C',
        default='None',
        help='The Configuration file',
    )
    args = argparser.parse_args()
    return args
