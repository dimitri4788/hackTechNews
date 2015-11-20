#!/usr/local/bin/python

import re
import sys
import urllib2
import webbrowser

############################
##### Global variables #####
############################
argsDict = {} #or use dict()
resultCode = {
    "result_ok": "No error",
    "result_flag_error": "Error with flag(s)."
}
usage = """\
usage: hackNews [-h | -help]
                [-p <number of pages to scan>]
                [-c <categories to search for>]
                [-n <number of pages to open at a time> | <all>]
                [-points <points used to display pages with points higher than this>]

Syntax for flags:
    -p:         <Integer greater than 0>
    -c:         <category1|category2|category3|...>
    -n:         <Integer greater than 0>
    -points:    <Integer greater than 0>

Default values of flags:
    -p:         Default value is 1
    -c:         None; a value is needed
    -n:         Default value is 1
    -points:    Default value is 0

Example usage: hackNews -p 2 -c c++|linux|apache -n 3
               hackNews -c script -n 2
               hackNews -c os|guide|database|jquery|rust -points 150

Additional information:
    1. The -c flag is needed. Other flags are optional.
    2. Google Chrome web browser is needed.
    3. urllib2 and webbrowser libraries are needed.
"""

#./hackNews [-p <number of pages to scan>] [-c <categories to search for>] [-n <number of pages to open at a time> | <all>] [-points <points used to display pages with points higher than this>]
#0           1      2                        3               4              5          6                                          7          8
def parseArguments(arguments):
    argumentsLen = len(arguments)

    #Check whether number of arguments is odd or not
    if(argumentsLen % 2 == 0):
        return resultCode["result_flag_error"]

    numOfIterations = ((argumentsLen-1)/2)
    """
    while(numOfIterations > 0):
        arguments[]


        numOfIterations -= 1;
    """




def main(argc, argv):
    #Check if the script is ran without any arguments
    if(argc < 2):
        print usage
        sys.exit()

    #If help command is passed, print usage and quit
    if(argv[1] == "-h" or argv[1] == "-help" or argv[1] == "h" or argv[1] == "help"):
        print usage
        sys.exit()

    #Parse the arguments
    result = parseArguments(argv)
    if(result == resultCode["result_flag_error"]):
        print result
        print usage
        sys.exit()

    print "----- Hack Tech News -----"
    print "--------------------------"
    print "\n"

if __name__ == "__main__":
    commandLineArgs = sys.argv
    main(len(commandLineArgs), commandLineArgs)
