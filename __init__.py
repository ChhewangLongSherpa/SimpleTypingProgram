# -*- coding: utf-8 -*-
from getFile import *


def sysout(line):
    sys.stdout.write(line)


def lineNposMatch(arraySource, array1):
    if set(arraySource) & set(array1):
        z = [i for i, j in zip(arraySource, array1) if i == j]
        p = [x for x in a if x in b]
        if len(arraySource) == len(z) and len(arraySource) == len(p):
            print "Matching!"
            print "\n{}\n{}".format(p, z)
            return True
    return False


if __name__ == "__main__":
#    link = "http://classics.mit.edu/Antoninus/meditations.2.two.html"
#    link = linkCheck('-w')
#    print urlRead(link)
#    print askForInput("link")

    line = "Begin the morning by saying to thyself, I shall meet with the"

    while 1:
        sysout(line)
        sysin = askForInput("\n>")
        a = line.split()
        b = sysin.split()
        if lineNposMatch(a, b):
            break
        print "Non-matching!"
        continue


'''
        if set(a) & set(b):
            z = [i for i, j in zip(a, b) if i == j]
            p = [x for x in a if x in b]
            if len(a) == len(z) and len(a) == len(p):
                print "Matching!"
                print "\n{}\n{}".format(p, z)
                break
'''