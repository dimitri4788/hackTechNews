#!/usr/local/bin/python
# #!/usr/bin/env python XXX

import re
import sys
import urllib2
import webbrowser

#########################
# Some useful declaration
#########################
argsDict = {}  # or use dict()
resultCode = {
    "resultOk": "No error",
    "resultFlagError": "Error with flag(s)."
}
hackerNewsURL = "https://news.ycombinator.com"
#pathForMorePages = "/news?p=" XXX
#pathForOverPoints = "/over?points=" XXX
#https://news.ycombinator.com/over?points=200         XXX
#https://news.ycombinator.com/over?points=50&p=3      XXX
regularExpForUrls = '(class="deadmark"></span><a href="https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,4}\b([-a-zA-Z0-9@:%_;\+.~#?&//=()]*)">(.+</a><)|class="deadmark"></span><a href="https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,4}\b([-a-zA-Z0-9@:%_;\+.~#?&//=()]*)" rel="nofollow">(.+</a><))'
usage = """\
usage: hackNews [-h | -help]
                [-p <number of pages to scan>]
                [-c <categories to search for>]
                [-points <points used to display pages with points higher than this>]

Syntax for flags:
    -p:         <Integer greater than 0>
    -c:         <category1,category2,category3, ...>
    -points:    <Integer greater than 0>

Default values of flags:
    -p:         Default value is 1
    -c:         None; a value is needed
    -points:    Default value is 0

Example usage: hackNews -p 2 -c c++,linux,apache
               hackNews -c script
               hackNews -c os,guide,database,jquery,rust -points 150

Additional information:
    1. The -c flag is needed. Other flags are optional.
    2. Google Chrome web browser is needed.
    3. urllib2 and webbrowser libraries are needed.
"""

# @brief This function parses the command line arguments and fills the global variable argsDict
#   NOTE:
#   Possible flag keys: -p, -c, -points
#   Possible flag values: <20>, <os,guide,database> etc.
#   For example: hackNews -p 2 -c c++,linux,apache 3
#                keys: -p, -c
#                values: 2, c++,linux,apache, 3
#
# @param arguments The command line arguments to parse
#
# @return It returns one of the resultCode's
def parseArguments(arguments):
    # Get the length of the list arguments
    argumentsLen = len(arguments)
    print argumentsLen #XXX

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
    expectedFlagKeys = ["-p", "-c", "-points"]
    for (i,j) in zip(flagKeyIndex, flagValueIndex):
        # Check whether flag key is in the expectedFlagKeys or not
        if(arguments[i] not in expectedFlagKeys):
            return resultCode["resultFlagError"]

        # Check whether flag value is the correct format and type
        if(arguments[i] == "-p" or arguments[i] == "-points"):
            if(arguments[j].isdigit() == False or int(arguments[j]) < 1):
                return resultCode["resultFlagError"]
        #elif(arguments[i] == "-c"):
            #NOTE:Any value can be passed to -c flag key, but if user
            #inputs some wrong formatted data, then nothing can be done

        argsDict[arguments[i]] = arguments[j]

    return resultCode["resultOk"]

# @brief Processes the request based on arguments in argsDict and
#   forms the output TODO
#
# @return  It returns the TODO
def processRequest():
    print "Processes Request" # XXX
    print argsDict
    numberPoints = "1"
    numberOfPages = "1"
    categoriesStringValue = ""

    # Check if points flag is passed, if yes, save in a variable
    if '-points' in argsDict:
        numberPoints = argsDict['-points']
    print "numberPoints", numberPoints

    # Check if pages flag is passed, if yes, save in a variable
    if '-p' in argsDict:
        numberOfPages = argsDict['-p']
    print "numberOfPages", numberOfPages

    # Check if categories flag is passed, if yes, save in a variable
    if '-c' in argsDict:
        categoriesStringValue = argsDict['-c']
    print "categoriesStringValue ", categoriesStringValue

    #https://news.ycombinator.com/over?points=200&p=1 XXX
    # Loop over all the pages, open 3 pages from the top of list of pages
    #   and display the rest of the list on stdout
    for page in range(int(numberOfPages)):
        #strr = 'http://garethrees.org/2015/12/14/javascript/">Plan to throw one away</a><'
        #urll = strr.split("\">")
        #print urll[0]
        #print urll[1]
        #print urll[1][:-5]
        url = hackerNewsURL + "/over?points=" + numberPoints + "&p=" + str(page+1)
        print "url", url #XXX
        response = urllib2.urlopen(url)
        htmlData = response.read()
        urlMatches = re.findall(r'(class="deadmark"></span><a href="https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,4}\b([-a-zA-Z0-9@:%_;\+.~#?&//=()]*)">(.+</a><)|class="deadmark"></span><a href="https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,4}\b([-a-zA-Z0-9@:%_;\+.~#?&//=()]*)" rel="nofollow">(.+</a><))', htmlData)
        if urlMatches:
            for match in urlMatches:
                #print match
                #print match[0]
                print match[0][33:].split("\">")
                #url = match[0][33:]
                #webbrowser.get(chrome_path).open(url)
        else:
            print 'did not find'

    #if '-points' in argsDict:
        #url = hackerNewsURL + "/over?points=" + argsDict['-points']
        #response = urllib2.urlopen(url)
        #htmlData = response.read()
        #urlMatches = re.findall(r'%s' %(regularExpForUrls), htmlData)
        #urlMatches = re.findall(r'(class="deadmark"></span><a href="https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,4}\b([-a-zA-Z0-9@:%_;\+.~#?&//=()]*)">(.+</a><)|class="deadmark"></span><a href="https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,4}\b([-a-zA-Z0-9@:%_;\+.~#?&//=()]*)" rel="nofollow">(.+</a><))', htmlData)
        #print '%s' %(regularExpForUrls)
        #print "YESSSSSS"
        #print url
        #if urlMatches:
        #    for match in urlMatches:
        #        #print match[0][33:]
        #        print match[0]
        #        #url = match[0][33:]
        #        #webbrowser.get(chrome_path).open(url)
        #else:
        #    print 'did not find'

            #https://news.ycombinator.com/over?points=200&p=1



def main(argc, argv):
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
