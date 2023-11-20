from bs4 import BeautifulSoup
import requests as r
from sklearn.metrics.pairwise import cosine_similarity


def board2vec(gameID):
    """
    Black Box Recommending
    gonna recommend games with similar factors for games user rating highly
    factors: 
        family of game (by ranks) - 'childrensgame_rank', 'familygame_rank', etc.
        player count - ‘minplayers’ & ‘maxplayers’ in xml
        game length - ‘minplaytime’ & ‘maxplaytime’ in xml
        complexity - ‘averageweight’ in xml
        age rating - ‘age’ in xml
        year of game release - 'yearpublished' in xml

    Description:
        Takes in the id of a board game, and invokes the API to get a vectorized version
        of the boardgame

    inputs:
        `gameid` (as collected from userPrompting)

    outputs:
        returns a tuple where index 0 is the gameID and index 1 is the vectorized version of the game
    """
    game = BeautifulSoup(r.get(f'https://boardgamegeek.com/xmlapi/boardgame/{gameID}').content, 'xml')
    # example for how to access data from searchForGames
    # boardgameCategories = game.find_all('boardgamecategory')
    #     isExpansion = False
    #     for category in boardgameCategories:
    #         if category['objectid'] == '1042':
    #             # print("expansion!")
    #             isExpansion = True

    # player counts
    minPlayers = int(game.find('minplayers').text)
    print(minPlayers, type(minPlayers))
    # maxPlayers = game.find('maxplayers')
def sortCosSim(boardgamelist, usergames):
    """
    
    Description:
        utilize cosine similarity function compare boardgamelist games to usergames
        score absolute value (distance) between boardgamelist games and each usergames [Group rating: 3.0 -> Ideal Cosine Similarity: .3]

    Inputs:
        ::list(list) the vectors for all boardgames under consideration
        usergames::parameter to indicate which boardgames vectors are the user's inputted boardgames 

    Outputs:
        returns top n (default is 10) list of tuples where index 0 is the gameID and index 1 is the game name
        top n are the top n lowest collective distance from every usergame
    
        
    """
    pass

def main():
    board2vec('35424')
if __name__ == "__main__":
    main()