import sys
sys.path.append("..")
from random import randint
from Games.tictactoeGame import TicTacToe
import discord
#TODO: reduce conditionals ? maybe use error pool

ttt_games = {}
maxID = 1000 

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


def initiate_game_data(player0, player1, id0, id1): #challenge
    existing_game = find_game(player0, player1)
    
    if existing_game is None:
        ttt_games[generate_game_id()] = {"players": [player0, player1], "ids": [ id0, id1], "game": TicTacToe()}
        return (True, [ id0, id1])

    return (False, existing_game)


def player_move(player_moving, r, c, gameID=None): #move
    rcInts = [int(r), int(c)]
    if (rcInts[0] >= 3 or rcInts[1] >= 3): #hard coded since specific to tic tac toe
        return (False, 'Row or Column not within bounds')

    gameID = find_game(player_moving) if gameID is None else [gameID] 

    if  isinstance(gameID, list):

        if len(gameID) == 1:
            if ttt_games[gameID[0]]["game"].board[rcInts[0]][rcInts[1]] is not None:
                return (False, "That position is occupied.")

            if ttt_games[gameID[0]]["players"].index(player_moving) == ttt_games[gameID[0]]['game'].cur_player:
                ttt_games[gameID[0]]["game"].make_move(rcInts[0], rcInts[1])
                update = ttt_games[gameID[0]]["game"].update_game()
  
                if update[0]:
                    opponent = ttt_games[gameID[0]]["ids"][ttt_games[gameID[0]]['game'].cur_player]
                    return (True, False, f"{player_moving} has made a move:\n {ttt_games[gameID[0]]['game']}", opponent)

                elif update[1] == "full":
                    return end_game(player_moving, False, gameID[0], True)
                else:
                    return end_game(player_moving, True, gameID[0])

            return False, 'Not your turn'

        return (False, f"Multiple games found: {gameID}") # TODO: pretty string print

    return (False, 'game not found')


def deny_game_start(player, gameID=None, attachBoard=False, msg=None): #deny
    gameID = find_game(player) if gameID is None else [gameID] 

    if  isinstance(gameID, list):

        if len(gameID) == 1:

            opponent = gameID[0]["ids"][0] if gameID[0]["players"][1] == player else gameID[0]["ids"][1]
            del ttt_games[gameID[0]]
 
            return (True, True, msg, opponent)
        
        return (False, f"Multiple games found: {gameID}")

    return (False, 'game not found')
    

def initiate_game_start(player_moving, r, c, gameID=None): #accept
    gameID = find_game(player_moving) if gameID is None else [gameID] 

    if  isinstance(gameID, list):

        if len(gameID) == 1:

            if ttt_games[gameID[0]]["players"].index(player_moving) == 0:
                ttt_games[gameID[0]]["game"].start_game()
                return player_move(player_moving, r, c, gameID[0])
            
            return (False, f'Waiting on challenger to accept or you should try tictactoe move command')
        
        return (False, f"Multiple games found: {gameID}")

    return (False, 'game not found')

def end_game(player_moving, gameWon=False, gameID=None, boardFull=False): #quit
    # TODO:pretty print board
    gameID = find_game(player_moving) if gameID is None else [gameID]

    if isinstance(gameID, list):

        if len(gameID) == 1:

            if gameWon:
                board = str(ttt_games[gameID[0]]["game"])
                return deny_game_start(player_moving, gameID, True, f"{player_moving} has won the game. {board}")
            
            elif boardFull:
                return deny_game_start(player_moving, gameID, True, f"Stalemate!. {board}")
            
            return deny_game_start(player_moving, gameID, False, f"{player_moving} has terminated the tic-tac-toe game ")
        
        return (False, f"Multiple games found: {gameID}")

    return (False, 'game not found')


if __name__ == "__main__":
    initiate_game_data("t2", "t1")
    initiate_game_data("t4", "t3")
    print(ttt_games)
    gID1, gID2 = list(ttt_games.keys())
    print(gID1, gID2)
    print(initiate_game_data("t1", "t2"))
    print(deny_game_start("t2"))
    print(initiate_game_start("t2", "0", "0"))
    print(initiate_game_start("t4", "0", "0"))
    print(initiate_game_start("t3", "0", "0"))
    print(player_move("t3", "0", "0"))
    print(player_move("t3", "1", "1"))
    print(ttt_games[gID2])
    print(end_game("t3", True, gID2))
    print(end_game("t3"))





    



