# This file is an attempt to write some api calls with urllib3 since that is what we used in cav's class
#
import urllib3
from time import time

# Functionality of the API
# Search for games by name and by AKAs
# Retrieve information about a particular game or games
# Retrieve games in a user's collection
# Retrieve the messages from a forum/game thread
# Retrieve entries from a geeklist 

# Note from tthe Documentation Page
# Note: BGG throttles the requests now, which is to say that if you send requests too frequently, 
# the server will give you 500 or 503 return codes, reporting that it is too busy. 
# Currently, a 5-second wait between requests seems to suffice.
# 
# I think we should make an offline database of games
# 
# 
# 

idToName = {}
nameToId = {}

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


def setupDicts(filepath = "./boardgames_ranks.csv") -> None:
    """
    Sets up the dictionaries `idToName` and `nameToId`
    """

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



setupDicts()
def main():
    """Main function of this file."""
    
    print(list(nameToId)[0])





s = time()
setupDicts()
if __name__ == "__main__":
    main()
f = time()
pass
#print("Time passed:", f-s)