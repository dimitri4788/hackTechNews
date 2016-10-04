hacknews
========

A command line utility to access Hacker News website (https://news.ycombinator.com/) in a more fun/useful way.

Description
-----------
Hacker News website has two features: *pages* and *points*. Each page has links to 30 news articles/pages and the user can go to the next page by clicking *More* at the bottom of each page. The points feature lets you filter search results based on the number of points articles have received from the users. Using these, and in addition to the categories (keywords passed as a command line flag), you can filter articles you want to read.

Categories are just keywords that are matched over all the links found on the page(s).

Installation
------------
```sh
python setup.py install
```

TODO fix this
```sh
# Development with alias mode (-A flag)
# Alias mode (the -A or --alias option) instructs py2app to build an application bundle that uses your source and data files in-place. It does not create standalone applications, and the applications built in alias mode are not portable to other machines
$ python setup.py py2app -A

# To run application directly from the Terminal
$ ./dist/BudgetManager.app/Contents/MacOS/BudgetManager

# Building for deployment
# This will assemble your application as dist/BudgetManager.app. Since this application is self-contained, you will have to run the py2app command again any time you change any source code, data files, options, etc.
# The easiest way to wrap your application up for distribution at this point is simply to right-click the application from Finder and choose “Create Archive”.
$ python setup.py py2app

# Copy the application (.app) bundle to Applications directory
$ sudo cp -r dist/BudgetManager.app /Applications/

# NOTE: Useful link: https://pythonhosted.org/py2app/tutorial.html
```

Usage
-----
```
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
```

Notes
-----
It assumes that you have Google Chrome installed and the path to its executable is */Applications/Google Chrome.app*

Author
------
Deep Aggarwal  
deep.uiuc@gmail.com  
Date Started: 11/16/2015  
