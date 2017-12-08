# -*- coding: utf-8 -*-
import argparse
from config import *
import time
import sys


#TODO debug below function
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


def timed_askForInput(prompt):
    sys.stdout.write("{}>".format(prompt))
    begin = time.time()
    inp = sys.stdin.readline()
    end = time.time()
    elapsed = end - begin
    return inp, elapsed