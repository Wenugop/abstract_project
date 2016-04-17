import os
import errno
import Constants

class DirectoryWrapper:
    def makeFolder(self, folderName):
        #get file path for the directory
        #TODO: implement the foldername stuff. For now, it's just hardcoded in
        myDirPath = Constants.KeepDirectory
        print()
        print('----------------- our Keep directory is in: -----------------')
        print(myDirPath)
        print('-------------------------------------------------------------')
        print()
        #do it this way so that we avoid the race condition
        #from having a folder created between the check for 
        #existence and call for creation.
        try:
            os.makedirs(myDirPath)            
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise exception
            else:
                print (myDirPath + " already exists")