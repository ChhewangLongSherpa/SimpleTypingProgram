# -*- coding: utf-8 -*-
import sys
from getFile import *


def askForInput(prompt):
    sys.stdout.write("{}>".format(prompt))
    inp = sys.stdin.readline()
    return inp


def sysout(line):
    sys.stdout.write(line)


def lineNposMatch(arraySource, array1):
    #If the number of elements in the array match
    if set(arraySource) & set(array1):
        #Do the two array have the same values in the same order
        #Method1
        z = [i for i, j in zip(arraySource, array1) if i == j]
        #Method2
        p = [x for x in arraySource if x in array1]
        #Possibly Redundant: Check if the len of the arraySource and the
        #matches are the same
        if len(arraySource) == len(z) and len(arraySource) == len(p):
            if DEBUG:
                print "Matching!"
                print "\n{}\n{}".format(p, z)
            return True
    return False


def mistyped(a, b):
#set(a).union(b) - set(a).intersection(b)
#Make the array to be compared into a set
    s = set(b)
#Preserves order of input list
#Check for the difference
    t = [x for x in a if x not in s]
#Returns the difference values in array format
    return t


if __name__ == "__main__":
#    link = "http://classics.mit.edu/Antoninus/meditations.mb.txt"
#    link = "http://classics.mit.edu/Herodotus/history.mb.txt"
#    link = linkCheck('-w')
#    print urlRead(link)
#    print askForInput("link")

#    line = "Begin the morning by saying to thyself, I shall meet with the"
    
    #openfiles content - May want to shift this to function
    with open('README.md') as f:
	lines = f.readlines()
    
    #Remove whitespace like '\n' at the end of each line
    lines = [x.strip() for x in lines]
    line = lines[0]

    #TODO - Shift the below code to a boolean function
    while 1:
        sysout(line)
        if TIMED:
            sysin, ti = timed_askForInput("\nt>")
        else:
            sysin = askForInput("\n>")
        a = line.split()
        b = sysin.split()
        if lineNposMatch(a, b):
            if TIMED:
                sysout("\nTime: {}".format(ti))
                sysout("\nWords: {}".format(len(a)))
                sysout("\nWords/Time: {}".format(len(a) / ti))
                sysout("\n")
                #hello
            break
        print "Non-Matching: {}".format(mistyped(a, b))
        continue
