import requests
import xml.etree.ElementTree as ET
searchHTML = "https://boardgamegeek.com/xmlapi/search?search={}"
idHTML = "https://boardgamegeek.com/xmlapi/boardgame/{}"
def getNamesFromSearchURL(url):
    response = requests.get(url)
    tree = ET.fromstring(response.content)
    #root = tree.iter
    for elem in tree.iter():
        if(elem.tag == "name"):
            for item in tree.iter(elem.tag):
                if "{'primary': 'true'}" == str(item.attrib):
                    print(item.text)


def getIDsFromSearchURL(url):
    response = requests.get(url)
    tree = ET.fromstring(response.content)
    #root = tree.iter
    ret = []
    for elem in tree.iter():
        if(elem.tag == "boardgame"):
            print(elem.attrib["objectid"])
            ret.append(elem.attrib["objectid"])
            # for item in tree.iter(elem.tag):
            #     print(item.text)
            #     if "{'primary': 'true'}" == str(item.attrib):
            #         pass
    return ret

def testfun(idS):
    print(idHTML.format(idS))
    response = requests.get(idHTML.format(idS))
    #tree = ET.fromstring(response.content)
    pass


def main():
    #searchString = "%20".join(input("Please enter a Board Game: ").split(" "))
    searchString = "%20".join("Crossbows and Catapults".split(" "))
    thisSearch = searchHTML.format(searchString)
    print(thisSearch)
    getNamesFromSearchURL(thisSearch)
    gameIds = getIDsFromSearchURL(thisSearch)
    idSearch = ",".join(gameIds)
    testfun(idSearch)

if __name__ == "__main__":
    main()