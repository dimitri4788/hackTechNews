hacknews
========

A command line utility to access Hacker News website (https://news.ycombinator.com/) in a more fun/useful way.

Installation
------------
```sh
python setup.py install
```

Usage
-----
```
usage: hackNews [-h | -help]
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

Example usage: hackNews -p 2 -c c++,linux,apache -n 3
               hackNews -c script -n 2
               hackNews -c os,guide,database,jquery,rust -points 150

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
