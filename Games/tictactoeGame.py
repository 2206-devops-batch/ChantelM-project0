class Board:
    """
    Board class
    Parameters: (int)r, (int)c
    Each instance will have (int)row, (int)column, and (list)board variables
    the board variable can be reduced to a 1D list by including 0 for the r parameter
    """

    def __init__(self, r, c):
        self.rows = r
        self.cols = c
        self.board = [[None for x in range(self.cols)] for y in range(self.rows)]

    def display_board(self):
        for y in self.board:
            for x in y:
                if x is not None:
                    print(x, end=' | ')
                else:
                    print(' ', end=' | ')

            print()
            print('------------')

    def update_board(self, row, col, marker):
        self.board[row][col] = marker

    def board_full(self):
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
        next_player = self.cur_player + 1
        self.cur_player = next_player if next_player < self.num_players else 0


class TicTacToe(Board, Players):
    """
    TicTacToe class subclass of Board and Markers
    Parameters: mark1 and mark2 (assumed to be characters)
    TODO: how to enforce parameter type to ensure string
    TODO: remove internal print statements and use tuples to signal specific error?
    """

    def __init__(self, mark1, mark2):
        Board.__init__(self, 3, 3)
        Players.__init__(self, (mark1, mark2))
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
        print("end game")
        self.active = False
        self.cur_player = None

    def make_move(self, row, col):
        if (row >= self.rows or col >= self.cols):
            print('Row or Column not within bounds')
            return False
        
        if self.board[row][col] is not None:
            print("There's already a marker there.")
            return False
        
        self.update_board(row, col, self.markers[self.cur_player])
        self.update_player()
        return True

    def check_rows(self):
        for y in range(self.rows):
            if self.board[y][0] is not None and self.board[y][0] == self.board[y][1] == self.board[y][2]:
                self.winner = self.board[y][0]
                return True

        return False

    def check_columns(self):
        for x in range(self.cols):
            if self.board[0][x] is not None and self.board[0][x] == self.board[1][x] == self.board[2][x]:
                self.winner = self.board[0][x]
                return True

        return False

    def check_diagonals(self):
        if self.board[1][1] is not None:
            lr_diagonal = self.board[0][0] == self.board[1][1] == self.board[2][2]
            rl_diagonal = self.board[0][2] == self.board[1][1] == self.board[2][0]
            if lr_diagonal or rl_diagonal:
                self.winner = self.board[1][1]
                return True
        return False

    def check_for_winner(self):
        if not self.check_rows():
            if not self.check_columns():
                return self.check_diagonals()
        
        return True

    def update_game(self):
        if self.check_for_winner(): # update winner to player # and stop game
            self.winner = self.markers.index(self.winner)
            self.end_game()

        elif self.board_full():
            print(f'board is full')
            self.end_game()


# Example game play
if __name__ == '__main__':
    t3 = TicTacToe('x', 'o')
    # print(t3)
    t3.start_game()
    while t3.active:
        
        moved = False
        while not moved:
            req_move = input(f'Player {t3.cur_player}, enter your move: ').split(' ')
            
            if len(req_move) != 2:
                print('Expected 2 values separated by a space(ex: 1 2). Try again')
                continue

            if not req_move[0].isdigit() or not req_move[1].isdigit():
                print('Received a non-numeric input. Try again')
                continue

            move = [int(x) for x in req_move]
            moved = t3.make_move(move[0], move[1])
    
        t3.update_game()
        t3.display_board()
        print()

    print(f'')