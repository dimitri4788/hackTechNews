#!/usr/local/bin/python

import re
import sys
import urllib2
import webbrowser

#Global variables
usage = """\
usage: ./hackNews [-h | -help]
                  [-p <number of pages to scan>]
                  [-c <categories to search for>]
                  [-n <number of pages to open at a time> | <all>]
                  [-points <points used to display pages with points higher than this>]
"""
commandLineArgs = sys.argv

def checkIfValidArgs(args):
    return False

def main():
    if(len(commandLineArgs) < 2):
        print usage
        sys.exit()

    if(commandLineArgs[1] == "-h" or commandLineArgs[1] == "-help" or commandLineArgs[1] == "h" or commandLineArgs[1] == "help"):
        print usage
        sys.exit()

    isValidArgs  = checkIfValidArgs(commandLineArgs)
    if(isValidArgs == False):
        print "Error in command line arguments."
        print usage
        sys.exit()

    print "----- Hack Tech News -----"
    print "--------------------------"
    print "\n"



if __name__ == "__main__":
    main()
