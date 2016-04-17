import xml.etree.ElementTree as ET
import re
import os
import errno
import DirectoryWrapper
import XMLTreeWrapper
import Constants
from datetime import timedelta, datetime

def main():
    #init the constants first. Without that, you have nothing
    Constants.init()
    print("Printing from main: " + Constants.KeepDirectory)
    # first create our directory
    startTime = datetime.now()
    print('----------------- time now is ----------------------')
    print(startTime)
    print('----------------------------------------------------')
    print()
    print()
    _directoryWrapper = DirectoryWrapper.DirectoryWrapper()
    print('Creating the "Keep_Abstract" folder')
    _directoryWrapper.makeFolder("Keep_Abstract")
    print('writing out each file')
    _xmlTreeWrapper = XMLTreeWrapper.XMLTreeWrapper()
    _xmlTreeWrapper.writeXMLTree('List_of_150.txt')
    print('finished writing files')
    endTime = datetime.now()
    totaltime = endTime - startTime
    print('total time = ' + str(totaltime))
    
    #xmlStressTest()
    #xmlTreeChildrenTest()
    #dictionaryStuff()
    #xmlTreeStuff()
    
main()