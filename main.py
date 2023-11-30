import requests as r
from bs4 import BeautifulSoup
from b2v import board2vec, sortCosSim
from lib3api import setupDicts, idToName, nameToId

# GLOBALS
NumberOfBoardgamesToSearch = 4

# Pseudo code/Planning 

# Get user input of games they’ve played, ask for at least 3 maybe
# while they want to enter more data, let them enter
#   name of board game
#   Their group rating of the board game
#       int input range bound from 1-10 

def searchForGame(gameTitle):
    # call the api search function on gameTitle
    # get a list of game id's returned probably
    # searchedGames = []
    possibleGames = []
    gamesSearch = BeautifulSoup(r.get(f'https://boardgamegeek.com/xmlapi/search?search={gameTitle}').content, 'xml')
    gameIDs = ""
    i=0    
    for game in gamesSearch.find_all('boardgame'):
        # print(game)
        gameID = game['objectid']
        gameIDs += gameID + ","
        gameName = game.text.strip().split('\n')[0]
        # searchedGames.append((gameID, gameName))
        gameInformation = BeautifulSoup(r.get(f'https://boardgamegeek.com/xmlapi/boardgame/{gameID}').content, 'xml')
        boardgameCategories = gameInformation.find_all('boardgamecategory')
        isExpansion = False
        for category in boardgameCategories:
            if category['objectid'] == '1042':
                # print("expansion!")
                isExpansion = True
        boardgameVersion = gameInformation.find_all('boardgameversion')
        isEnglish = False
        for category in boardgameVersion:
            if 'English' in category.text:
                # print("english!")
                isEnglish = True
        if isEnglish and not isExpansion:
            print(f"{i+1}: {gameName}")
            i += 1
            possibleGames.append((gameID, gameName))
        if len(possibleGames) > NumberOfBoardgamesToSearch:
            print("Only the first 5 games have been listed. \nPlease be more specific with your game title.")
            break
    # loop through those games 
    #   add to possibleGames list if NOT an expansion
    #   ignore otherwise
    # print(searchedGames, '\n\n')
    
    # print(gameIDs)
    # print(possibleGames)
    # display possibleGames to user as a numbered list format
    if len(possibleGames) > 1:
        # for i, game in enumerate(possibleGames):
        #     print(f"{i+1}: {game[1]}")
        # take user input - 1 bc zero index
        userSelection = int(input("Select with game you meant by inputing it's number: ")) - 1
        while userSelection < 0 or userSelection > len(possibleGames) - 1:
            userSelection = int(input("Please select a game within the range: ")) - 1
        # return game selected by user
        return possibleGames[userSelection]
    elif len(possibleGames) == 0:
        return ["Error"]
    else:
        return possibleGames[0]

def userPrompting():
    allUserBoardGames = []
    allUserRatings = []
    inputGame = None
    gameRating = None
    print("Welcome to Cav's boardgames! You are now entering the Hypersphere of Trust, please share some boardgames your group has played and a rating 1-10 for each.")
    while True:
        inputGame = None
        gameRating = None
        if len(allUserBoardGames) == 2:
            print("Thank you for your input! You may enter \"Done\" to finish your list")
        while inputGame is None: #ensures user does not enter a duplicate board game
            inputGame=input("Boardgame: ")
            if inputGame == "Done":
                break
            inputGame=searchForGame(inputGame)[0] 
            if inputGame == "Error":
                print("I'm sorry I don't recognize that game. Please provide a different game.")
                inputGame = None
            for game in allUserBoardGames: 
                if game==inputGame:
                    print("This boardgame is already recorded on our list. Please provide a different game.")
                    inputGame = None
        if inputGame == "Done":
            break
        while gameRating is None: #ensures the user gives a numerical value between 1 and 10
            try:
                gameRating=float(input("Group Rating: "))
                while gameRating > 10 or gameRating < 1:
                    print("Please provide a valid rating between 1-10")
                    gameRating=float(input("Group Rating: "))
            except ValueError:
                print("Please provide a valid rating between 1-10")
                gameRating = None
        allUserBoardGames.append(inputGame)
        allUserRatings.append(gameRating)
    return (allUserBoardGames, allUserRatings)

# output top 10 games we’d think they like
#   pretty print a list

def main():
    userGames, groupRatings = userPrompting()
    userGamesVectorized = []
    allGamesVectorized = []
    boardGamesIDs = []
    for game in userGames:
        userGamesVectorized.append(board2vec(game)[1])
    #print(userGamesVectorized)
    with open('vectors.csv', encoding="utf8") as f:
        for row in f:
            boardGamesIDs.append(row.split(",")[0]) #the gameids for reference
            allGamesVectorized.append([float(i) for i in row.split(",")[1:]]) #the values for comparison   
    recommendedGames = sortCosSim(allGamesVectorized, boardGamesIDs, userGamesVectorized, groupRatings)  

    for i in range(len(recommendedGames)):
        recommendedGames[i] = idToName[int(recommendedGames[i][0])]

    print("Based on your provided games, here are some games we recommend:", recommendedGames)
    #done
    

if __name__ == "__main__":
    main()