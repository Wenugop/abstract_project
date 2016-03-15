import xml.etree.ElementTree as ET
import os

class XMLTreeWrapper:
    def __init__(self):
        self.curDir = os.curdir
        
    def writeXMLTree(self, fileName):
        sourceLoc = self.curDir + "\\" + fileName
        
        xmlTree = ET.parse(sourceLoc)
        
        root = xmlTree.getroot()
        count = 0
        
        refString = ""
        
        print('writing', end="")
        
        for reference in root.iter('reference'):
            refString = ET.tostring(reference)
            count = count + 1
            destLoc = self.curDir + "\\Keep\\output_" + str(count) + ".xml"
            newXMLTreeElem = ET.fromstring(refString)
            newXMLTree = ET.ElementTree(newXMLTreeElem)
            newXMLTree.write(destLoc)
            if (count % 20) == 0:
                print('.', end="")
        print('') 