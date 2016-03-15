import os

class DirectoryWrapper:
    def __init__(self):
        self.curdir = os.curdir

    def makeFolder(self, folderName):
        #get file path for the directory
        #TODO: change os.curdir to directory of abstract files.
        myDirPath = self.curdir + "\\" + folderName
        #do it this way so that we avoid the race condition
        #from having a folder created between the check for 
        #existence and call for creation.
        try:
            os.makedirs(myDirPath)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise exception
            else:
                print (os.curdir + " already exists")