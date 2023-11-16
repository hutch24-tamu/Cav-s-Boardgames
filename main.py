# Pseudo code/Planning

# Get user input of games they’ve played, ask for at least 3 maybe
# while they want to enter more data, let them enter
#   name of board game
#   Their group rating of the board game
#       int input range bound from 1-10 

def searchForGame(gameTitle):
    # call the api search function on gameTitle
    # get a list of game id's returned probably
    searchedGames = [] #change for api call instead
    # loop through those games 
    #   add to possibleGames list if not an expansion
    #   ignore otherwise
    possibleGames = []
    for game in searchedGames:
        boardgameCategoryID = "0000" #replace with api call for boardgamecategory id number
        # may need to change this to a loop through the IDs because 
        # boardgamecategory can be listed multiple times and we want to make sure none of them
        # are 1024 for expansion
        # may don't need loop and could just do if "1024" in boardgameCategoryIDs, maybe
        if boardgameCategoryID == "1024":
            possibleGames.append(game)

    # display possibleGames to user as a numbered list format
    for i, game in enumerate(possibleGames):
        print(f"{i+1}: {game}")
    # take user input - 1 bc zero index
    userSelection = int(input("Select with game you meant by inputing it's number")) - 1
    # return game selected by user
    return possibleGames[userSelection]

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