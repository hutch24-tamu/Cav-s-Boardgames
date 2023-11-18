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
    #   add to possibleGames list if NOT an expansion
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
    all_userboardgames = []
    all_userratings = []
    input_game = ""
    game_rating = None
    done_notification = False
    print("Welcome to Cav's boardgames! You are now entering the Hypersphere of Trust, please share some boardgames your group has played and a rating 1-10 for each.")
    while True:
        game_rating = None
        if len(all_userboardgames) > 2 and done_notification==False:
            print("Thank you for your input! You may enter Done to finish your list")
            done_notification=True
        input_game=input("Boardgame: ")
        if input_game == "Done":
            break
      #  input_game = searchForGame(input_game) #will need to implement searchForGame
        while game_rating is None: #ensures the user gives a numerical value between 1 and 10
            try:
                game_rating=float(input("Group Rating: "))
                while game_rating > 10 or game_rating < 1:
                    print("Please provide a valid rating between 1-10")
                    game_rating=float(input("Group Rating: "))
            except ValueError:
                print("Please provide a valid rating between 1-10")
                game_rating = None
        all_userboardgames.append(input_game)
        all_userratings.append(game_rating)
    print(all_userboardgames)
    print(all_userratings)

'Standard python convention to have this'
if __name__ == "__main__":
    main()