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
    "resultOk": "No error",
    "resultFlagError": "Error with flag(s)."
}
hackerNewsURL = "https://news.ycombinator.com"
#pathForMorePages = "/news?p=" XXX
#pathForOverPoints = "/over?points=" XXX
#https://news.ycombinator.com/over?points=200         XXX
#https://news.ycombinator.com/over?points=50&p=3      XXX
usage = """\
usage: hackNews [-h | -help]
                [-p <number of pages to scan>]
                [-c <categories to search for>]
                [-n <number of pages to open at a time> | <all>]
                [-points <points used to display pages with points higher than this>]

Syntax for flags:
    -p:         <Integer greater than 0>
    -c:         <category1,category2,category3, ...>
    -n:         <Integer greater than 0>
    -points:    <Integer greater than 0>

Default values of flags:
    -p:         Default value is 1
    -c:         None; a value is needed
    -n:         Default value is 1
    -points:    Default value is 0

Example usage: hackNews -p 2 -c c++,linux,apache -n 3
               hackNews -c script -n 2
               hackNews -c os,guide,database,jquery,rust -points 150

Additional information:
    1. The -c flag is needed. Other flags are optional.
    2. Google Chrome web browser is needed.
    3. urllib2 and webbrowser libraries are needed.
"""

# @brief This function parses the command line arguments and fills the global variable argsDict
#   NOTE:
#   Possible flag keys: -p, -c, -n, -points
#   Possible flag values: <20>, <os,guide,database> etc.
#   For example: hackNews -p 2 -c c++,linux,apache -n 3
#                keys: -p, -c, -n
#                values: 2, c++,linux,apache, 3
#
# @param arguments The command line arguments to parse
#
# @return It returns one of the resultCode's
def parseArguments(arguments):
    #Get the length of the list arguments
    argumentsLen = len(arguments)

    #Check whether number of arguments is odd or not
    if(argumentsLen % 2 == 0):
        return resultCode["resultFlagError"]

    #Get the indices of flags keys and values
    flagKeyIndex = range(1, argumentsLen, 2)
    flagValueIndex = range(2, argumentsLen, 2)
    if(len(flagKeyIndex) != len(flagValueIndex)):
        #This if check is redundant
        return resultCode["resultFlagError"]

    #Iterate over the flagKeyIndex and flagValueIndex and fill argsDict
    expectedFlagKeys = ["-p", "-c", "-n", "-points"]
    for (i,j) in zip(flagKeyIndex,flagValueIndex):
        #Check whether flag key is in the expectedFlagKeys or not
        if(arguments[i] not in expectedFlagKeys):
            return resultCode["resultFlagError"]

        #Check whether flag value is the correct format and type
        if(arguments[i] == "-p" or arguments[i] == "-n" or arguments[i] == "-points"):
            if(arguments[j].isdigit() == False or int(arguments[j]) < 1):
                return resultCode["resultFlagError"]
        #elif(arguments[i] == "-c"):
            #NOTE:Any value can be passed to -c flag key, but if user
            #inputs some wrong formatted data, then nothing can be done

        argsDict[arguments[i]] = arguments[j]

    return resultCode["resultOk"]

# @brief Processes the request based on arguments in argsDict and
#   forms the output
#
# @return  It returns the 
def processRequest():
    print "Processes Request"
    if '-points' in argsDict:
        print "YESSSSSS"



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
    parseResult = parseArguments(argv)
    if(parseResult == resultCode["resultFlagError"]):
        print parseResult
        print usage
        sys.exit()

    print "----- Hack Tech News -----"
    print "--------------------------"
    print "\n"
    print argsDict #XXX
    processRequest()
    #generate keywords for project XXX
    #also, make a list suggetion on keywords XXX


if __name__ == "__main__":
    commandLineArgs = sys.argv
    main(len(commandLineArgs), commandLineArgs)
