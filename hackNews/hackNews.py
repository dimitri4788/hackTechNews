#!/usr/bin/env python

import re
import sys
import urllib2
import webbrowser

#####################
# Useful declarations
#####################
argsDict = {}  # or use dict()
resultCode = {
    "resultOk": "No error",
    "resultFlagError": "Error with flag(s)."
}
hackerNewsURL = "https://news.ycombinator.com"
chromePath = 'open -a /Applications/Google\ Chrome.app %s'
class termColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
usage = """\
usage: hacknews [-h | -help]
                [-p <number of pages to scan>]
                [-c <categories to search for>]
                [-n <number of pages to open at a time>]
                [-points <points used to display pages with points higher than this>]

Syntax for flags:
    -p:         <Integer greater than 0>
    -c:         <category1,category2,category3, ...>
    -n:         <Integer greater than 0>
    -points:    <Integer greater than 0>

Default values of flags:
    -p:         Default value is 1
    -c:         None
    -n:         Default value is 3
    -points:    Default value is 1

Example usage:
    hacknews -p 2 -c c++,linux,apache -n 3
    hacknews -c script -n 2
    hacknews -c os,guide,database,jquery,rust -points 150

Additional information:
    1. Google Chrome web browser is needed.
    2. urllib2 and webbrowser libraries are needed.
"""

# @brief This function parses the command line arguments and fills the global variable argsDict
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
    # Get the length of the list arguments
    argumentsLen = len(arguments)

    # Check whether number of arguments is odd or not
    if(argumentsLen % 2 == 0):
        return resultCode["resultFlagError"]

    # Get the indices of flags keys and values
    flagKeyIndex = range(1, argumentsLen, 2)
    flagValueIndex = range(2, argumentsLen, 2)
    if(len(flagKeyIndex) != len(flagValueIndex)):
        # This if check is redundant
        return resultCode["resultFlagError"]

    # Iterate over the flagKeyIndex and flagValueIndex and fill argsDict
    expectedFlagKeys = ["-p", "-c", "-n", "-points"]
    for (i,j) in zip(flagKeyIndex, flagValueIndex):
        # Check whether flag key is in the expectedFlagKeys or not
        if(arguments[i] not in expectedFlagKeys):
            return resultCode["resultFlagError"]

        # Check whether flag value is the correct format and type
        if(arguments[i] == "-p" or arguments[i] == "-n" or arguments[i] == "-points"):
            if(arguments[j].isdigit() == False or int(arguments[j]) < 1):
                return resultCode["resultFlagError"]
        #elif(arguments[i] == "-c"):
            #NOTE:Any value can be passed to -c flag key, but if user
            #inputs some wrong formatted data, then nothing can be done

        argsDict[arguments[i]] = arguments[j]

    return resultCode["resultOk"]


# @brief Processes the request based on arguments in argsDict and
#   forms the output urls and open them in Google Chrome
def processRequest():
    print termColors.BOLD + termColors.UNDERLINE + termColors.HEADER + "Processing Start" + termColors.ENDC
    numberOfPoints = "1"
    numberOfPages = "1"
    numberOfPagesToOpen = "3"
    categoriesStringValue = ""
    pagesToOpen = []

    # Check if points flag is passed, if yes, save in a variable
    if '-points' in argsDict:
        numberOfPoints = argsDict['-points']
        print termColors.OKGREEN + "Number of points (-points): " + numberOfPoints + termColors.ENDC

    # Check if pages flag is passed, if yes, save in a variable
    if '-p' in argsDict:
        numberOfPages = argsDict['-p']
        print termColors.OKGREEN + "Number of pages to scan (-p): " + numberOfPages + termColors.ENDC

    # Check if number of pages to open flag is passed, if yes, save in a variable
    if '-n' in argsDict:
        numberOfPagesToOpen = argsDict['-n']
        print termColors.OKGREEN + "Number of pages to open (-n): " + numberOfPagesToOpen + termColors.ENDC
        # Check numberOfPagesToOpen for errors
        if int(numberOfPagesToOpen) == 0:
            print termColors.FAIL + 'Enter number of pages (-n)' + termColors.ENDC
            return
        if int(numberOfPagesToOpen) > 20:
            print termColors.FAIL + 'Are you sure you want to enter number of pages (-n) greater than 20 (Y/N):' + termColors.ENDC,
            usersDecision = raw_input()
            if usersDecision == "N" or usersDecision == "n" or usersDecision == "no" or usersDecision == "No":
                return

    # Check if categories flag is passed, if yes, save in a variable
    categoriesStringValueLower = ""
    if '-c' in argsDict:
        categoriesStringValue = argsDict['-c']
        categoriesStringValueLower = categoriesStringValue.lower()
        print termColors.OKGREEN + "Categories to search for (-c): " + categoriesStringValue + termColors.ENDC

    # Loop over the number of pages and construct pagesToOpen
    for page in range(int(numberOfPages)):
        url = hackerNewsURL + "/over?points=" + numberOfPoints + "&p=" + str(page+1)
        response = urllib2.urlopen(url)
        htmlData = response.read()
        urlMatches = re.findall(r'(class="deadmark"></span><a href="https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,4}\b([-a-zA-Z0-9@:%_;\+.~#?&//=()]*)">(.+</a><)|class="deadmark"></span><a href="https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,4}\b([-a-zA-Z0-9@:%_;\+.~#?&//=()]*)" rel="nofollow">(.+</a><))', htmlData)
        if urlMatches:
            for match in urlMatches:
                splittedMatch = match[0][33:].split("\">")
                splittedMatchLower = splittedMatch[1].lower()
                splittedMatchLowerList = splittedMatchLower.split()
                if categoriesStringValueLower:
                    splittedCategories = categoriesStringValueLower.split(",")
                    splittedCategoriesF = list(set(splittedCategories))  # Remove duplicates from the categories list
                    for sc in splittedCategoriesF:
                        if sc in splittedMatchLowerList:
                            if splittedMatch[0].find("nofollow") != -1:
                                pagesToOpen.append(splittedMatch[0][:-15])
                            else:
                                pagesToOpen.append(splittedMatch[0])
                else:
                    if splittedMatch[0].find("nofollow") != -1:
                        pagesToOpen.append(splittedMatch[0][:-15])
                    else:
                        pagesToOpen.append(splittedMatch[0])

    # Open the web pages in the browser
    if len(pagesToOpen) == 0:
        print termColors.FAIL + 'Did not find anything' + termColors.ENDC
        return
    print termColors.OKGREEN + "Number of pages found: " + str(len(pagesToOpen)) + termColors.ENDC
    if len(pagesToOpen) < int(numberOfPagesToOpen):
        for urlToOpen in pagesToOpen:
            webbrowser.get(chromePath).open(urlToOpen)
    else:
        for p in range(int(numberOfPagesToOpen)):
            webbrowser.get(chromePath).open(pagesToOpen[p])

def main(argc=None, argv=None):
    # Get command line arguments
    if argc is None and argv is None:
        commandLineArgs = sys.argv
        argc = len(commandLineArgs)
        argv = commandLineArgs

    # Check if the script is ran without any arguments
    if(argc < 2):
        print usage
        sys.exit()

    # If help command is passed, print usage and quit
    if(argv[1] == "-h" or argv[1] == "-help" or argv[1] == "h" or argv[1] == "help"):
        print usage
        sys.exit()

    # Parse the arguments
    parseResult = parseArguments(argv)
    if(parseResult == resultCode["resultFlagError"]):
        print termColors.FAIL + parseResult + termColors.ENDC
        print usage
        sys.exit()

    # Process the request
    processRequest()
    print termColors.BOLD + termColors.UNDERLINE + termColors.HEADER + "Processing Done" + termColors.ENDC

if __name__ == "__main__":
    main()
