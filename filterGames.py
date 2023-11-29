import csv
import requests as r
from bs4 import BeautifulSoup
from time import time
startTime = time()
#   The purpose of this file is to create filteredgames_ids.csv
#   filteredgames_ids should contain the game ids of valid games (expansion and non-English games)
#   creating this file beforehand should make creating every vector a bit faster

#First step is gathering every boardgameid from boardgames_ranks.csv
candidateGameIDs = [] 
with open('boardgames_ranks.csv', encoding="utf8") as f:
    next(f) #first line is header 
    for row in f:
        candidateGameIDs.append(row.split(",")[0]) 
    f.close()

#Second step is filtering the gamelist by removing all invalid games (very similar to searchForGame)
possibleGames = []
numCanidates = len(candidateGameIDs)
print(numCanidates)
gamesStart = time()
print("Time since start",gamesStart-startTime)
i = 0
lastTime = time()
for game in candidateGameIDs:
    i+=1
    if i%1000 == 0:
        print(f"Time from {i-1000} to {i}", time()-lastTime)
        lastTime = time()
    #gameInformation = BeautifulSoup(r.get(f'https://boardgamegeek.com/xmlapi/boardgame/{game}').content, 'xml')
    file = open(f"./xmls/{game}.xml","r",encoding="utf8")
    gameInformation = BeautifulSoup(file, 'xml')
    boardgameCategories = gameInformation.find_all('boardgamecategory')
    isExpansion = False
    for category in boardgameCategories:
        if category['objectid'] == '1042':
            isExpansion = True
            break
    if isExpansion:
        continue
    boardgameVersion = gameInformation.find_all('boardgameversion')
    isEnglish = False
    for category in boardgameVersion:
        if 'English' in category.text:
            isEnglish = True
            break
    if isEnglish:
        possibleGames.append(game)
     #   if len(possibleGames) == 10000:
     #       print("Made it to 10000")
     #   if len(possibleGames) == 50000:
     #       print("Made it to 50000")
#print(len(possibleGames))

#NO LONGER USED (only gameIDs will be of use for using the board2vec function)
#Third step returns back to boardgames_ranks and acquire all information about valid boardgames
#possibleGamesQuick = set(possibleGames) #referencing a set will make this less painful 
#possibleGamesInformation = []
#with open('boardgames_ranks.csv', encoding="utf8") as g:
#    next(g)
#    for row in g: #Will keep each row with games that are valid (English and nonexpansion)
#        gameID = row.split(",")[0]
#        if gameID in possibleGamesQuick:
#            possibleGamesInformation.append(row)
#    g.close()

#Final step is to create the new file which will only contain valid gameIDs
with open('filteredgames_ids.csv', 'x', encoding='utf8') as w:
    write = csv.writer(w)
    write.writerows(possibleGames)
endTime = time()
