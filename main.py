# Pseudo code/Planning

# Get user input of games they’ve played, ask for at least 3 maybe
# while they want to enter more data, let them enter
#   name of board game
#   Their group rating of the board game
#       int input range bound from 1-10 

def searchForGame(gameTitle):
    # call the api search function on gameTitle
    # get a list of game id's returned probably
    # loop through those games 
    #   add to possibleGames list if not an expansion
    #   ignore otherwise
    # display possibleGames to user as a numbered list format
    # take user input - 1 bc zero index
    # return game selected by user

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