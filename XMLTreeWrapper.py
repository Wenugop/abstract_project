import xml.etree.ElementTree as ET
import os
import Constants
import sys

class XMLTreeWrapper:        
    def writeXMLTree(self, fileName):
        sourceLoc = os.path.join(Constants.DirectoryHead, fileName)
        
        xmlTree = ET.parse(sourceLoc)
        
        root = xmlTree.getroot()
        count = 0
        
        refString = ""
        
        print('writing', end="")
        print('now writing the abstract stuff')
        
        for reference in root.iter('reference'):
            refString = ET.tostring(reference)
            count = count + 1
            outputFileName = "".join(["output_", str(count), ".xml"])
            destLoc = os.path.join(Constants.KeepDirectory, outputFileName)
            #destLoc = self.curDir + "\\Keep\\output_" + str(count) + ".xml"
            newXMLTreeElem = ET.fromstring(refString)
            newXMLTree = ET.ElementTree(newXMLTreeElem)
            newXMLTree.write(destLoc)
            if (count % 30) == 0:
                print('.', end="")
                sys.stdout.flush()
        print('') 