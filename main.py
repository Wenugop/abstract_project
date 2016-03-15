import xml.etree.ElementTree as ET
import re
import os
import errno
import DirectoryWrapper
import XMLTreeWrapper
from datetime import timedelta, datetime

def main():
    #first create our directory
    startTime = datetime.now()
    _directoryWrapper = DirectoryWrapper.DirectoryWrapper()
    print('Creating the "Keep" folder')
    _directoryWrapper.makeFolder('Keep')
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