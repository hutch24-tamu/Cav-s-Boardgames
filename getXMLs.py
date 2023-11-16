import requests
import os
from numpy import setdiff1d

idToName = {}
nameToId = {}

# def writeToCsv(filename:str,content):
#     with open(filename) as f:



def preprocessName(gameName:str) -> str:
    """
    A preprocessing function for the strings in the csv file

    Arguments
    `gameName` : str
        the title from the csv that should be formated
    
    Returns
    `processed` : str
         The processed title of the game passed in
    """
    #remove leading and trailing quotation marks
    processed = gameName[1:] if gameName[0] == '"' else gameName
    processed = processed[:-1] if processed[-1] == '"' else processed
    processed = processed.replace('""','"')
    #any other preprocessing goes here

    return processed

def getXMLRequests(pt=False):
    filepath = "./boardgames_ranks.csv"
    with open(filepath,"r",encoding="utf8") as f:

        normalCommas = f.readline().count(",")
        i = 1
        for line in f:
            commas = line.count(",")
            lineparts = line.split(",")
            gameID = -1
            try:
                gameID = int(lineparts[0])
                name = preprocessName(",".join([lineparts[1+i] for i in range(commas-normalCommas+1)]))
                #if '"' in name: print(name) # I just wanted to see the names with quotation marks
            except:
                print("Game id",lineparts[0],"is not a valid int")
            # if commas != 14:
            #     print(name,"on line",i,"has",commas-normalCommas,"commas")
            i+=1
            idToName[gameID] = name
            nameToId[name] = gameID


    URL = "https://boardgamegeek.com/xmlapi/boardgame/{}?stats=1"
    XML = "//{}.xml"

    # response = requests.get(URL)
    # with open('feed.xml', 'wb') as file:
    #     file.write(response.content)

    path = "D://SDCode//xmls"
    allList = list(idToName.keys())
    done = [int(i[:-4]) for i in os.listdir(path) ]
    #skips = [143950,143951,143952,143967,143973]
    needToDo = setdiff1d(allList,done)
    #needToDo = setdiff1d(needToDo,skips)
    N = 5
    i = 0
    print(len(needToDo))
    if (len(needToDo)< 100):
        print("Very few left, remove this check now")
        return
    
    for id in needToDo:
        if pt:
            print(id)
        response = requests.get(URL.format(id))
        # try:
        #     response = requests.get(URL.format(id))
        # except:
        #     print("Request for {} was refused".format(id))
        try:
            with open(path+XML.format(id), 'wb') as file:
                file.write(response.content)
            i += 1
            if i%100 == 0: print(i)
        except:
            print("Something went wrong writing the file")
            if os.path.exists(path+XML.format(id)):
                os.remove(path+XML.format(id))

if __name__== "__main__":
    getXMLRequests()