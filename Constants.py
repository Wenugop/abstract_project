#this file houses all our constants for the program

#CHANGES THAT NEED TO BE MADE:
#   Redo Keep directory so that it isn't hard coded in I guess? I'm not sure. 

import os
from sys import platform as _platform

def init():
    #the following is OS dependent    
    global DirectoryHead
    DirectoryHead = os.getcwd()
    global KeepDirectory
    KeepDirectory = os.path.join(DirectoryHead, "Keep_Abstract")
    print("Keep Directory for Linux: " + KeepDirectory)
    