import sys
sys.path.append("..")
from random import randint
from games.TictactoeGame import TicTacToe
import discord
#TODO: reduce conditionals ? maybe use error pool

ttt_games = {}
maxID = 1000 

def generate_game_id():
    gameID = str(randint(0,1000))

    while gameID in ttt_games:
        gameID = str(randint(0,sys.maxsize))

    return gameID


def find_game(player0, player1=None): #TODO: pull player0, player1, gameID from file
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


def initiate_game_data(players_data): #challenge #TODO: pull player0, player1, gameID from file
    player0, player1, id0, id1 = players_data.split()
    
    existing_game = find_game(player0, player1)
    
    if existing_game is None:
        ttt_games[generate_game_id()] = {"players": [player0, player1], "ids": [ id0, id1], "game": TicTacToe()}
        return (f"True {id0} {id1}")

    return (f"False Found existing gameid: {existing_game}")


def move_player(req_move): #move
    player_moving, r, c, gameID = req_move.split()
    rcInts = [int(r), int(c)]
    
    if (rcInts[0] >= 3 or rcInts[1] >= 3): #TODO: remove hardcoded limits
        return (f"False Row or Column not within bounds")

    gameID = find_game(player_moving) if gameID == "None" else [gameID] 

    if  isinstance(gameID, list):
        
        if len(gameID) == 1:
            if ttt_games[gameID[0]]["game"].board[rcInts[0]][rcInts[1]] !=None:
                return (f"False That position is occupied.")

            if ttt_games[gameID[0]]["players"].index(player_moving) == ttt_games[gameID[0]]['game'].cur_player:
                ttt_games[gameID[0]]["game"].make_move(rcInts[0], rcInts[1])
                update = ttt_games[gameID[0]]["game"].update_game()
  
                if update[0]:
                    opponent = ttt_games[gameID[0]]["ids"][ttt_games[gameID[0]]['game'].cur_player]
                    return (f"True False {opponent} {player_moving} has made a move:\n {ttt_games[gameID[0]]['game']}")

                elif update[1] == "full":
                    return end_game(f"{player_moving} False {gameID[0]} True")
                else:
                    return end_game(f"{player_moving} True {gameID[0]} False")

            return (f"False Not your turn")

        return (f"False Multiple games found: {gameID}")

    return (f"False game not found")


def deny_game_start(denied): #deny
    msg = denied.split()
    player = denied.pop(0) 
    gameID = denied.pop(0) 
    msg = " ".join(msg)
    gameID = find_game(player) if gameID == "None" else [gameID] 

    if  isinstance(gameID, list):

        if len(gameID) == 1:

            opponent = gameID[0]["ids"][0] if gameID[0]["players"][1] == player else gameID[0]["ids"][1]
            del ttt_games[gameID[0]]
 
            return (f"True True {opponent} {msg}")
        
        return (f"False Multiple games found: {gameID}")

    return (f"False game not found")
    

def initiate_game_start(move_data): #accept
    player_moving, r, c, gameID = move_data.split()

    gameID = find_game(player_moving) if gameID == "None" else [gameID] 

    if  isinstance(gameID, list):

        if len(gameID) == 1:

            if ttt_games[gameID[0]]["players"].index(player_moving) == 0:
                ttt_games[gameID[0]]["game"].start_game()
                return move_player(f"{player_moving} {r} {c} {gameID[0]}")
            
            return (f"False Waiting on challenger to accept or you should try tictactoe move command")
        
        return (f"False Multiple games found: {gameID}")

    return (f"False game not found")

def end_game(ending_data): #quit
 
    player_moving, gameWon, gameID, boardFull = ending_data.split()
    gameID = find_game(player_moving) if gameID == "None" else [gameID]

    if isinstance(gameID, list):

        if len(gameID) == 1:

            if gameWon:
                board = str(ttt_games[gameID[0]]["game"])
                return deny_game_start(f"player_moving gameID {player_moving} has won the game. {board}")
            
            elif boardFull:
                return deny_game_start(f"player_moving gameID Stalemate!. {board}")
            
            return deny_game_start(f"player_moving gameID {player_moving} has terminated the tic-tac-toe game ")
        
        return (f"False Multiple games found: {gameID}")

    return (f"False game not found")

