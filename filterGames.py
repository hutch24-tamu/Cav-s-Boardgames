import csv
import requests as r
from bs4 import BeautifulSoup

#   The purpose of this file is to create filteredgames_ranks.csv
#   filteredgames_ranks should be boardgames_ranks without the header or all invalid games (expansion and non-English games)
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
for game in candidateGameIDs:
    gameInformation = BeautifulSoup(r.get(f'https://boardgamegeek.com/xmlapi/boardgame/{game}').content, 'xml')
    boardgameCategories = gameInformation.find_all('boardgamecategory')
    isExpansion = False
    for category in boardgameCategories:
        if category['objectid'] == '1042':
            isExpansion = True
    boardgameVersion = gameInformation.find_all('boardgameversion')
    isEnglish = False
    for category in boardgameVersion:
        if 'English' in category.text:
            isEnglish = True
    if isEnglish and not isExpansion:
        possibleGames.append(game)
     #   if len(possibleGames) == 10000:
     #       print("Made it to 10000")
     #   if len(possibleGames) == 50000:
     #       print("Made it to 50000")
#print(len(possibleGames))

#Third step returns back to boardgames_ranks and acquire all information about valid boardgames
possibleGamesQuick = set(possibleGames) #referencing a set will make this less painful 
possibleGamesInformation = []
with open('boardgames_ranks.csv', encoding="utf8") as g:
    next(g)
    for row in g: #Will keep each row with games that are valid (English and nonexpansion)
        gameID = row.split(",")[0]
        if gameID in possibleGamesQuick:
            possibleGamesInformation.append(row)
    g.close()

#Final step is to create the new file will the information about the valid boardgames to be used for vectors
with open('filteredgames_ranks.csv', 'x', encoding='utf8') as w:
    write = csv.writer(w)
    write.writerows(possibleGamesInformation)
