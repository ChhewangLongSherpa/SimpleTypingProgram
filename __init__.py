# -*- coding: utf-8 -*-
import sys
import os
from getFile import *


def ask_for_input(prompt):
    sys.stdout.write("{}>".format(prompt))
    inp = sys.stdin.readline()
    return inp


def sysout(line):
    sys.stdout.write(line)


def line_n_pos_Match(arraySource, array1):
    #METHOD PURPOSE: For checking if the input and line from file match
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


def file_to_array(file):
    #https://codereview.stackexchange.com/questions/145126/
    #open-a-text-file-and-remove-any-blank-lines
    if not os.path.isfile(file):
        print '{} as file does not exist!!'.format(f)
        return
    with open(file) as filehandle:
        lines = filehandle.readlines()
    lines = filter(lambda x: x.strip(), lines)
    return lines


def Main_Typing_Loop(line):
    #METHOD PURPOSE: 2 Modes: Timed & Non Timed
    #Loop through file
    timed = "\nt>"
    not_timed = "\n>"
    while 1:
        if TIMED:
            sysout("{} {}".format(timed, line))
            sysin, ti = timed_askForInput(timed)
        else:
            sysout("{} {}".format(not_timed, line))
            sysin = ask_for_input(not_timed)
        a = line.split()
        b = sysin.split()
        if line_n_pos_Match(a, b):
            if TIMED:
                #sysout("\nTime: {}".format(ti))
                #sysout("\nWords: {}".format(len(a)))
                sysout("\nWords/Time: {}".format(len(a) / ti))
                sysout("\n")
                return (len(a) / ti)
            break
            return
        print "Non-Matching: {}".format(mistyped(a, b))
        continue


if __name__ == "__main__":
#    link = "http://classics.mit.edu/Antoninus/meditations.mb.txt"
#    link = "http://classics.mit.edu/Herodotus/history.mb.txt"
#    link = linkCheck('-w')
#    print urlRead(link)
#    print ask_for_input("link")

#    line = "Begin the morning by saying to thyself, I shall meet with the"

    lines = file_to_array('Meditations.txt')
    for x in lines:
        avg = Main_Typing_Loop(x)
    if avg >= 0:
        print avg
