import unittest
import sys
sys.path.append("..")
import src.server.tictactoe.tictactoeGame as tttG

"""
unittest provides framework for unit testing (the flow of testing) for plug and play testing.
TestCase is a base class for testing individual unit functionality
"""

class TestTicTacToeBoardClass(unittest.TestCase):
    """
    Board Class Unit Tests
    """
    
    @classmethod
    def setUpClass(cls):
        cls.rows = 4
        cls.cols = 3
        cls.test_board = tttG.Board(cls.rows, cls.cols)

    def test_rows_created(self):
        expected = (self.rows, self.rows)
        results = (self.test_board.rows, len(self.test_board.board))
        self.assertEqual(results, expected)

    def test_columns_created(self):
        expected = (self.cols, self.cols)
        results = (self.test_board.cols, len(self.test_board.board[0]))
        self.assertEqual(results, expected)

    def test_board_update(self):
        expected = True, False

        for i in expected:
            with self.subTest():
                result=self.test_board.update_board(0, 0, 'x')
                self.assertEqual(result, i)

    def test_board_not_full(self):
        self.assertEqual(self.test_board.board_full(), False)

    def test_board_full(self):
        full_board = tttG.Board(self.rows, self.cols)
        full_board.board = [['x' for _ in range(self.test_board.cols)] for _ in range(self.test_board.rows)]
        self.assertEqual(full_board.board_full(), True)

    @classmethod
    def tearDownClass(cls):
        cls.test_board = None

class TestTicTacToePlayersClass(unittest.TestCase):
    """
    Players Class Unit Tests
    """

    @classmethod
    def setUpClass(cls):
        cls.marks = ('x', 'o')
        cls.test_players = tttG.Players(cls.marks)

    def test_init_settings(self):
        expected = [2, None, None, self.marks]
        results = [self.test_players.num_players, 
            self.test_players.cur_player, 
            self.test_players.winner, 
            self.test_players.markers]
        
        for i in range(4):
            with self.subTest():
                self.assertEqual(results[i], expected[i])

    def test_update_player(self):
        self.test_players.cur_player = 0
        expected = 1, 0

        for i in range(2):
            self.test_players.update_player()
            with self.subTest():
                self.assertEqual(self.test_players.cur_player, expected[i])

    @classmethod
    def tearDownClass(cls):
        cls.test_players = None

class TestTicTacToeGameClass(unittest.TestCase):
    """
    TicTacToe Class Unit Tests
    """

    def setUp(self):
        self.test_game = tttG.TicTacToe()

    def test_start_game(self):
        self.test_game.start_game()
        expected= 0, True
        results = self.test_game.cur_player, self.test_game.active

        for i in range(2):
            with self.subTest():
                self.assertEqual(results[i], expected[i])

    def test_end_game(self):
        self.test_game.start_game()
        self.test_game.end_game()

        expected= None, False
        results = self.test_game.cur_player, self.test_game.active

        for i in range(2):
            with self.subTest():
                self.assertEqual(results[i], expected[i])

    def test_check_in_range_true(self):
        
        for i in range(3):
            with self.subTest():
                self.assertTrue(self.test_game.check_in_range(i))

    def test_check_in_range_false(self):
        testValues = [-3, -1, 3, 5]

        for i in range(len(testValues)):
            with self.subTest():
                self.assertFalse(self.test_game.check_in_range(testValues[i]))

    def test_make_moves_true(self):
        testMoves = [(0,0), (1,1), (2,1), (2,2)]
        self.test_game.start_game()

        for i in testMoves:
            with self.subTest():
                self.assertTrue(self.test_game.make_move(i[0], i[1]))

    def test_make_moves_false(self):
        testMoves = [(-1, 0), (0, 3), (0, 0), (2, -5)]
        self.test_game.start_game()
        self.test_game.make_move(0,0)

        for i in testMoves:
            with self.subTest():
                self.assertFalse(self.test_game.make_move(i[0], i[1]))

    def test_check_rows_true(self):
        self.test_game.board = [['x', 'x', 'x'], ['o', 'x', 'o'], ['x', 'o', 'x']]
        self.assertTrue(self.test_game.check_rows())

    def test_check_rows_false(self):
        self.test_game.board = [['x', 'o', 'x'], ['o', 'x', 'o'], ['x', 'o', 'x']]
        self.assertFalse(self.test_game.check_rows())

    def test_check_columns_true(self):
        self.test_game.board = [['x', 'o', 'x'], ['x', 'x', 'o'], ['x', 'o', 'x']]
        self.assertTrue(self.test_game.check_columns())

    def test_check_columns_false(self):
        self.test_game.board = [['x', 'o', 'o'], ['x', 'o', 'x'], ['o', 'x', 'o']]
        self.assertFalse(self.test_game.check_columns())

    def test_check_diagonals_true(self):
        self.test_game.board = [['x', 'o', 'x'], ['x', 'x', 'o'], ['o', 'x', 'x']]
        self.assertTrue(self.test_game.check_diagonals())

    def test_check_diagonals_false(self):
        self.test_game.board = [['x', 'o', 'o'], ['x', 'o', 'x'], ['x', 'x', 'o']]
        self.assertFalse(self.test_game.check_diagonals())

    def test_check_for_winner_true(self):
        self.test_game.board = [['x', 'o', 'x'], ['x', 'x', 'o'], ['o', 'x', 'x']]
        self.assertTrue(self.test_game.check_for_winner())

    def test_check_for_winner_false(self):
        self.test_game.board = [['x', 'x', 'o '], ['o', 'o', 'x'], ['x', 'o', 'x']]
        self.assertFalse(self.test_game.check_for_winner())
    
    def test_update_game_true(self):
        self.test_game.board = [['x', None, None], [None, None, None], [None, None, None]]
        expected = (True, None)
        self.assertEqual(self.test_game.update_game(), expected)
    
    def test_update_game_false_winner(self):
        self.test_game.board = [['x', 'x', 'x'], [None, None, None], [None, None, None]]
        expected = (False, 0)
        self.assertEqual(self.test_game.update_game(), expected)

    def test_update_game_false_full(self):
        self.test_game.board = [['x', 'x', 'o '], ['o', 'o', 'x'], ['x', 'o', 'x']]
        expected = (False, 'full')
        self.assertEqual(self.test_game.update_game(), expected)

    def tearDown(self):
        self.test_game = None


# def suite():
#    suite = unittest.TestSuite()
# ##   suite.addTest (simpleTest3("testadd"))
# ##   suite.addTest (simpleTest3("testsub"))
#    suite.addTest(unittest.makeSuite(simpleTest3))
#    return suite


if __name__ == '__main__':
    unittest.main()