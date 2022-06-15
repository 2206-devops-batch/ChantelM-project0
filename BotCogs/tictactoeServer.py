import sys
sys.path.append("..")
from random import randint
from copy import deepcopy
from Games.tictactoeGame import TicTacToe

ttt_games = {}
maxID = 1000 #TODO: set to num_of_members squared

def generate_game_id():
    gameID = str(randint(0,1000))

    while gameID in ttt_games:
        gameID = str(randint(0,sys.maxsize))

    return gameID


def find_game(player0, player1=None):
    all_games = []

    if player1:
        for key in ttt_games:
            if player0 in ttt_games[key]['players'] and player1 in ttt_games[key]['players']:
                return key
    else:
        for key in ttt_games:
            if player0 in ttt_games[key]['players']:
                all_games.append(key)
    
    return all_games if len(all_games) > 0 else None


def initiate_game_data(player0, player1): #challenge
    existing_game = find_game(player0, player1)
    
    if existing_game is None:
        ttt_games[generate_game_id()] = {"players": [player0, player1], "game": TicTacToe()}
        return (True, None)
    
    return (False, existing_game)


def player_move(player_moving, r, c, gameID=None): #move
    rcInts = [int(r), int(c)]
    if (rcInts[0] >= 3 or rcInts[1] >= 3): #hard coded since specific to tic tac toe
        return (False, 'Row or Column not within bounds')

    gameID = find_game(player_moving) if gameID is None else [gameID] 

    if  isinstance(gameID, list):

        if len(gameID) == 1:

            if ttt_games[gameID]["game"].board[r][c] is not None:
                return (False, "That position is occupied.")

            if ttt_games[gameID[0]]["players"].index(player_moving) in gameID['players'] == ttt_games[gameID[0]]['game'].cur_player:
                ttt_games[gameID[0]]["game"].make_move(rcInts[0], rcInts[1])
                opponent = ttt_games[gameID[0]]["players"][ttt_games[gameID[0]]['game'].cur_player]
                return (True, opponent, str(ttt_games[gameID[0]]["game"]))

            return False, 'Not your turn'

        return (False, f"Multiple games found: {gameID}") # TODO: pretty string print

    return (False, 'game not found')


def deny_game_start(player, gameID=None, attachBoard=False): #deny
    gameID = find_game(player) if gameID is None else [gameID] 

    if  isinstance(gameID, list):

        if len(gameID) == 1:
            board = deepcopy(ttt_games[gameID]["game"].board)
            del ttt_games[gameID]

            if attachBoard:
                return (True, board)
            return (True, None)
        
        return (False, f"Multiple games found: {gameID}")

    return (False, 'game not found')
    

def initiate_game_start(player_moving, r, c, gameID=None): #accept
    gameID = find_game(player_moving) if gameID is None else [gameID] 

    if  isinstance(gameID, list):

        if len(gameID) == 1:
            ttt_games[gameID]["game"].start_game()
            return player_move(player_moving, r, c, gameID[0])
        
        return (False, f"Multiple games found: {gameID}")

    return (False, 'game not found')

def end_game(player_moving, gameWon=False, gameID=None): #quit
    gameID = find_game(player_moving) if gameID is None else [gameID] 

    if gameID[0]:

        if gameWon:
            return (True, f"{player_moving} has won the game. {gameID[1]}")

        return (True, f"{player_moving} has terminated the game ")

    return (False, 'game not found')


