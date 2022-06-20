class Board:
    """
    Board class
    Parameters: (int)r, (int)c
    Each instance will have (int)row, (int)column, and (list)board variables
    the board variable can be reduced to a 1D list by including 0 for the r parameter
    """

    def __init__(self, r, c):
        # stores specified row and column values and instantiates @d list using nested list comprehension
        
        self.rows = r
        self.cols = c
        self.board = [[None for x in range(self.cols)] for y in range(self.rows)]

    def display_board(self):
        # displays board by row by row and replaces None value with a space

        for y in self.board:
            for x in y:
                print(f"{x if x is not None else ' '}", end=' |')

            print()
            print('------------')

    def update_board(self, row, col, marker):
        # if request row and column is open, updates board with marker and return True. Otherwise returns False
        if self.board[row][col] is not None:
            return False
        
        self.board[row][col] = marker
        return True

    def board_full(self):
        # returns True if all board elements are occupied with a marker
        for y in self.board:
            for x in y:
                if x is None:
                    return False
        return True


class Players():
    """
    Players class
    Each instance will have (int)numPlayers, (list)markers.
    Parameters: (tuple)marks
    Contains (int)num_players and (tuple)marks. num_players is default to set to length of marks
    """

    def __init__(self, marks):
        self.num_players = len(marks)
        self.cur_player = None
        self.winner = None
        self.markers = marks
    
    def update_player(self):
        # updates cur_player by cycling through num_players
        next_player = self.cur_player + 1
        self.cur_player = next_player if next_player < self.num_players else 0


class TicTacToe(Board, Players):
    """
    TicTacToe class subclass of Board and Markers
    """

    def __init__(self):
        Board.__init__(self, 3, 3)
        Players.__init__(self, ('x', 'o'))
        self.active = False

    def __str__ (self): #TODO: condense
        boardStr = 'TicTacToe Board\n'
        for y in self.board:
            for x in y:
                if x is not None:
                    boardStr += f'{x} | '
                else:
                    boardStr += f'  | '
            boardStr += '\n-------------\n'
        return boardStr

    def start_game(self):
        self.cur_player = 0
        self.active = True

    def end_game(self):
        self.active = False
        self.cur_player = None

    def check_in_range(self, num):
        # verifies value is within row and column range

        if 0 > num or num >= 3:
            return False

        return True

    def make_move(self, row, col):
        # facilitates game play by updating board and current player when a player moves
        if self.check_in_range(row) and self.check_in_range(col):
            if self.update_board(row, col, self.markers[self.cur_player]):
                self.update_player()
                return True

        return False
        

    def check_rows(self):
        # if any row has 3 matches, updates self.winner and returns True
        for y in range(self.rows):
            if self.board[y][0] is not None and self.board[y][0] == self.board[y][1] == self.board[y][2]:
                self.winner = self.board[y][0]
                return True

        return False

    def check_columns(self):
        # if any column has 3 matches, updates self.winner and returns True
        for x in range(self.cols):
            if self.board[0][x] is not None and self.board[0][x] == self.board[1][x] == self.board[2][x]:
                self.winner = self.board[0][x]
                return True

        return False

    def check_diagonals(self):
        # if any diagonal has 3 matches, updates self.winner and returns True
        if self.board[1][1] is not None:
            lr_diagonal = self.board[0][0] == self.board[1][1] == self.board[2][2]
            rl_diagonal = self.board[0][2] == self.board[1][1] == self.board[2][0]
            if lr_diagonal or rl_diagonal:
                self.winner = self.board[1][1]
                return True
        return False

    def check_for_winner(self):
        # returns True if winner found
        if not self.check_rows():
            if not self.check_columns():
                return self.check_diagonals()
        
        return True

    def update_game(self):
        if self.check_for_winner(): # update winner to player # and stop game
            self.winner = self.markers.index(self.winner)
            self.end_game()
            return (False, self.winner)

        elif self.board_full():
            self.end_game()
            return (False, 'full')

        return (True, None)
