import xml.etree.ElementTree as ET
import os
import getXMLs


#my attempt to use the xml module to search through the xmls

pathtoXMLs = ".//xmls//"
xmlNames = [i for i in os.listdir(pathtoXMLs)]
def getFromFile(filename):
    tree = ET.parse(pathtoXMLs+filename)
    root = tree.getroot()
    for elem in root.iter():
        print(elem.tag)
        for item in root.iter(elem.tag):
            print(item.attrib, item.text)
        print()

   



online = False
def main():
    getFromFile("400179.xml")
if __name__ == "__main__":
    main()