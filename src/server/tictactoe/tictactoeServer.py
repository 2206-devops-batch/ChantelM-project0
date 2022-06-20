import sys
sys.path.append("./src/server/tictactoe")
import tictactoeGame as tttG
from random import randint, randrange

class TicTacToeSrvr():
    """
    TicTacToeSrvr class
    Each instance will have (dict) ttt_games and (int)maxID=1000.
    Serves as a wrapper class TicTacToe
    
    """

    maxID = 1000
    def __init__(self):
        self.ttt_games = {}
    
    def generate_game_id(self):
        gameID = randint(0, self.maxID)

        while gameID in self.ttt_games:
            gameID = randint(0,self.maxID)

        return str(gameID)

    def find_game(self, player0, player1=None):
        # returns a list of games with 1 or 2 players or None if not found
        all_games = []

        if player1:
            for key in self.ttt_games:
                if player0 in self.ttt_games[key]['players'] and player1 in self.ttt_games[key]['players']:
                    return key
        else:
            for key in self.ttt_games:
                if player0 in self.ttt_games[key]['players']:
                    all_games.append(key)
        
        return all_games if len(all_games) > 0 else None

    def initiate_game_data(self, players_data):
        # supports bot challenge subcommand by instantiating TicTacToe object and saving player data
        player0, player1, id0, id1 = players_data.split()
        
        existing_game = self.find_game(player0, player1)
        
        if existing_game is None:
            self.ttt_games[self.generate_game_id()] = {"players": [player0, player1], "ids": [ id0, id1], "game": tttG.TicTacToe()}
            return (f"True {id0} {id1}")

        return (f"False Found existing gameid: {existing_game}. Please add at the end of the command to proceed")

    def move_player(self, req_move):
        # supports bot move subcommand by correlating data with make_move
        player_moving, r, c, gameID = req_move.split()

        gameID = self.find_game(player_moving) if gameID == "None" else [gameID] 

        if  isinstance(gameID, list):
            
            if len(gameID) == 1:
   
                # verify correct player's move
                if self.ttt_games[gameID[0]]["players"].index(player_moving) == self.ttt_games[gameID[0]]['game'].cur_player:
        #             
                    if self.ttt_games[gameID[0]]["game"].make_move(int(r), int(c)):
                        update = self.ttt_games[gameID[0]]["game"].update_game()
                        if update[0]:
                            opponent = self.ttt_games[gameID[0]]["ids"][self.ttt_games[gameID[0]]['game'].cur_player]
                            return (f"True False {opponent} {player_moving} has made a move:\n {self.ttt_games[gameID[0]]['game']}")

                        elif update[1] == "full":
                            return self.end_game(f"{player_moving} False {gameID[0]} True")
                        else:
                            return self.end_game(f"{player_moving} True {gameID[0]} False")
                    
                    return (f"False Requested move contains values outside of the range [0, 3] or that square is occupied")
                
                return (f"False Not your turn")

            return (f"False Multiple games found: {gameID}")

        return (f"False game not found")

    def deny_game_start(self, denied): #deny
        # deletes game if user denies request
        msg = denied.split()
        player = msg.pop(0) 
        gameID = msg[0] 
        msg = " ".join(msg[1:]) if len(msg) > 1 else ""
    
        gameID = self.find_game(player) if gameID == "None" else [gameID] 

        if  isinstance(gameID, list):

            if len(gameID) == 1:

                opponent = self.ttt_games[gameID[0]]["ids"][0] if self.ttt_games[gameID[0]]["players"][1] == player else self.ttt_games[gameID[0]]["ids"][1]
                del self.ttt_games[gameID[0]]
    
                return (f"True True {opponent} {msg}")
            
            return (f"False Multiple games found: {gameID}")

        return (f"False game not found")
    

    def initiate_game_start(self, move_data): #accept
        # player who accepts makes the first move
        player_moving, r, c, gameID = move_data.split()

        gameID = self.find_game(player_moving) if gameID == "None" else [gameID] 

        if  isinstance(gameID, list):

            if len(gameID) == 1:

                if self.ttt_games[gameID[0]]["players"].index(player_moving) == 0:
                    self.ttt_games[gameID[0]]["game"].start_game()
                    return self.move_player(f"{player_moving} {r} {c} {gameID[0]}")
                
                return (f"False Waiting on challenger to accept or you should try tictactoe move command")
            
            return (f"False Multiple games found: {gameID}")

        return (f"False game not found")


    def end_game(self, ending_data): #quit
        player_moving, gameWon, gameID, boardFull = ending_data.split()
        gameID = self.find_game(player_moving) if gameID == "None" else [gameID]

        if isinstance(gameID, list):

            if len(gameID) == 1:
                board = self.ttt_games[gameID[0]]["game"]
                opponent = self.ttt_games[gameID[0]]["ids"][0] if self.ttt_games[gameID[0]]["players"][1] == player_moving else self.ttt_games[gameID[0]]["ids"][1]
                del self.ttt_games[gameID[0]]
                
                if gameWon == 'True':
                    return (f"True True {opponent} {player_moving} has won the game. {board}")
                elif boardFull == 'True':
                    return (f"True True {opponent} It's a draw!. {board}")

                return (f"True True {opponent} {player_moving} has terminated the tic-tac-toe game ")
            
            return (f"False Multiple games found: {gameID}")

        return (f"False game not found")

    def autoplay(self, data):
        # example game play using TicTacToe class from tictactoeGame
        game = tttG.TicTacToe()
        game.start_game()

        while game.active:
            move = randrange(3), randrange(3)

            game.make_move(move[0], move[1])
            game.update_game()

        if game.winner is None:
            return (f"No winner this game. {str(game)}")
        return (f"Player {game.winner} using '{game.markers[game.winner]}' won! {str(game)}")
        
    