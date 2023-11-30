from bs4 import BeautifulSoup
import requests as r
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize

debug = False

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
    game = BeautifulSoup(r.get(f'https://boardgamegeek.com/xmlapi/boardgame/{gameID}?stats=1').content, 'xml')
    gameID = gameID.replace("\n","").replace(",","")
    #file = open(f"./xmls/{gameID[:]}.xml","r",encoding="utf8")
    #game = BeautifulSoup(file, 'xml')
    # Get information from the xml. All are in try-except because some have '' returned when trying 
    # to access the tree, so int('') creates an error
    try:
        minPlayers = int(game.find('minplayers').text)
    except:
        minPlayers = 0
        if debug:
            print('Issue with getting minplayers')
    
    try:
        maxPlayers = int(game.find('maxplayers').text)
    except:
        maxPlayers = 0
        if debug:
            print('Issue with getting maxplayers')
    
    try:
        minPlayTime = int(game.find('minplaytime').text)
    except:
        minPlayTime = 0
        if debug:
            print('Issue with getting minplaytime')
    
    try:
        maxPlayTime = int(game.find('maxplaytime').text)
    except:
        maxPlayTime = 0
        if debug:
            print('Issue with getting maxplaytime')
    
    try:
        childrensGameRank = float(game.find(friendlyname="Children's Game Rank").get('bayesaverage'))
    except:
        childrensGameRank = 0
        if debug:
            print('Issue with getting childrensgame_rank')
    
    try:
        familyGameRank = float(game.find(friendlyname="Family Game Rank").get('bayesaverage'))
    except:
        familyGameRank = 0
        if debug:
            print('Issue with getting familygame_rank')

    try:
        partyGameRank = float(game.find(friendlyname="Party Game Rank").get('bayesaverage'))
    except:
        partyGameRank = 0
        if debug:
            print('Issue with getting partygames_rank')
    
    try:
        strategyGameRank = float(game.find(friendlyname="Strategy Game Rank").get('bayesaverage'))
    except:
        strategyGameRank = 0
        if debug:
            print('Issue with getting strategygames_rank')
    
    try:
        thematicGameRank = float(game.find(friendlyname="Thematic Rank").get('bayesaverage'))
    except:
        thematicGameRank = 0
        if debug:
            print('Issue with getting thematic_rank')
    
    try:
        warGameRank = float(game.find(friendlyname="War Game Rank").get('bayesaverage'))
    except:
        warGameRank = 0
        if debug:
            print('Issue with getting wargames_rank')
    
    try:
        complexity = float(game.find('averageweight').text)
    except:
        complexity = 0
        if debug:
            print('Issue with getting averageweight (complexity)')
    
    try:
        age = int(game.find('age').text)
    except:
        age = 0
        if debug:
            print('Issue with getting age')
    
    try:
        yearPublished = int(game.find('yearpublished').text)
    except:
        yearPublished = 0
        if debug:
            print('Issue with getting yearpublished')

    vec = [minPlayers, maxPlayers, minPlayTime, maxPlayTime, childrensGameRank, familyGameRank, partyGameRank, strategyGameRank, thematicGameRank, warGameRank, complexity, age, yearPublished]

    return (gameID, vec)


def sortCosSim(boardgamelist, boardgameIDs, usergames, groupRatings = [], n=10):
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
    if groupRatings == []:
        groupRatings = [10 for i in range(len(usergames))]

    # [i][j] index in cos sim matrix is a dot product of the ith column, jth row
    #if boardgameIDs[j]!=usergames[i][0]: #Need to implement a way to ignore self-comparisons
    dotProducts = cosine_similarity(boardgamelist, usergames)

    similarityScores = []
    for i in range(len(boardgamelist)):
        cosineScores = dotProducts[i]
        relativeSimScoreSum = 0

        for j in range(len(usergames)):
            userRated = groupRatings[j] / 10.0
            relativeSimScoreSum += abs(cosineScores[j] - userRated)

        similarityScores.append((boardgameIDs[i], relativeSimScoreSum))

    similarityScores.sort(key=lambda x: x[1])
    
    # Return type is (gameID, summed relative sim score)
    return similarityScores[:n]
        

def main():
    # Used to test my code
    # au = board2vec('14978')
    # bu = board2vec('12354')
    # cu = board2vec('2586')
    # du = board2vec('9831')
    # eu = board2vec('5677')
    # userGamesList = [au, bu, cu, du, eu]
    # a = board2vec('164928')
    # b = board2vec('12358')
    # c = board2vec('7895')
    # d = board2vec('78954')
    # e = board2vec('85321')
    # gameList = [a, b, c, d, e]
    
    # # Used to verify that the second value in the tuple is the closest in the list to the user ranked value
    # a = sortCosSim(gameList, userGamesList, [10,10,5,10,10])
    # print(a[2])

    # Used to test to make sure the correct averages are retrieved and put into the vector
    print(board2vec('246900')) # strat
    print(board2vec('268864')) # war
    print(board2vec('171131')) # party & thematic
    print(board2vec('91514'))  # children's & family

    pass
    
if __name__ == "__main__":
    main()