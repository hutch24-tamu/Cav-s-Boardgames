import requests as r
import xmltodict
from bs4 import BeautifulSoup
# Pseudo code/Planning

# Get user input of games they’ve played, ask for at least 3 maybe
# while they want to enter more data, let them enter
#   name of board game
#   Their group rating of the board game
#       int input range bound from 1-10 

def searchForGame(gameTitle):
    # call the api search function on gameTitle
    # get a list of game id's returned probably
    searchedGames = []
    gamesSearch = BeautifulSoup(r.get(f'https://boardgamegeek.com/xmlapi/search?search={gameTitle}').content, 'xml')
    # print(gamesSearch)
    gameIDs = ""
    for game in gamesSearch.find_all('boardgame'):
        # print(game)
        gameID = game['objectid']
        gameIDs += gameID + ","
        gameName = game.text.strip().split('\n')[0]
        searchedGames.append((gameID, gameName))
    # loop through those games 
    #   add to possibleGames list if not an expansion
    #   ignore otherwise
    # print(searchedGames, '\n\n')
    
    print(gameIDs)
    gamesInformation = BeautifulSoup(r.get(f'https://boardgamegeek.com/xmlapi/boardgame/{gameIDs}').content, 'xml')
    possibleGames = []
    for index, contents in enumerate(gamesInformation.find_all('boardgame')):
        boardgameCategories = contents.find_all('boardgamecategory')
        isExpansion = False
        for category in boardgameCategories:
            if category['objectid'] == '1042':
                # print("expansion!")
                isExpansion = True
        # print(game)
        boardgameVersion = contents.find_all('boardgameversion')
        isEnglish = False
        for category in boardgameVersion:
            if 'English' in category.text:
                # print("english!")
                isEnglish = True
        if isEnglish and not isExpansion:
            possibleGames.append(searchedGames[index])
    print(possibleGames)
    # display possibleGames to user as a numbered list format
    if len(possibleGames) > 1:
        for i, game in enumerate(possibleGames):
            print(f"{i+1}: {game[1]}")
        # take user input - 1 bc zero index
        userSelection = int(input("Select with game you meant by inputing it's number: ")) - 1
        # return game selected by user
        return possibleGames[userSelection]
    else:
        return possibleGames[0]

print(searchForGame("spirit island"))

# Black Box Recommending
# gonna recommend games with similar factors for games user rating highly
# factors: 
#   family of game 
#   player count - ‘minplayers’ & ‘maxplayers’ in xml
#   game length - ‘minplaytime’ & ‘maxplaytime’ in xml
#   complexity - ‘averageweight’ in xml
#   age rating - ‘age’ in xml
#   designer/publisher of games
#   year of game release

# output top 10 games we’d think they like
#   pretty print a list
#   let user let us know if they’ve played any of them and their ratings?

def main():
    pass

'Standard python convention to have this'
if __name__ == "__main__":
    main()