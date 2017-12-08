# -*- coding: utf-8 -*-
import argparse
import sys
from config import *


def oneArgParse(key):
    parser = argparse.ArgumentParser()
    parser.add_argument(key)
    args = parser.parse_args()
    if DEBUG:
        print args.key
    return args.key
#    if args.key is False or args.key is None:
#        return
#    else:
#        return args.key


def askForInput(prompt):
    sys.stdout.write("{}>".format(prompt))
    inp = sys.stdin.readline()
    return inp