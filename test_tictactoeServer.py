from curses.ascii import isdigit
import unittest
import sys
# sys.path.append("..")
import src.server.tictactoe.tictactoeServer as tttS
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
    def setUp(self):
        self.test_tttS = tttS.TicTacToeSrvr()
        self.challenged = tttS.TicTacToeSrvr()
        self.challenged.ttt_games['0'] = {"players": ["p0", "p1"], "ids": [ "id0", "id1"], "game": tttG.TicTacToe()}

    def test_generate_game_id(self):
        self.assertTrue(self.test_tttS.generate_game_id().isdigit())

    def test_find_game_none(self):
        self.assertIsNone(self.test_tttS.find_game("player0", "player1"))
 
    def test_find_game_2_players(self):
        self.test_tttS.ttt_games['0'] = {"players": ["player0", "player1"], "ids": [ "id0", "id1"], "game": None}
        self.assertEqual(self.test_tttS.find_game("player0", "player1"), "0")

    def test_find_game_1_player(self):
        self.test_tttS.ttt_games['0'] = {"players": ["player0", "player1"], "ids": [ "id0", "id1"], "game": None}
        self.test_tttS.ttt_games['1'] = {"players": ["player0", "player3"], "ids": [ "id2", "id3"], "game": None}
        self.assertEqual(self.test_tttS.find_game("player0"), ["0", "1"])
    
    def test_initiate_game_data(self):
        test_data = "someP1 someP2 00 01"
        result = [self.test_tttS.initiate_game_data(test_data), self.test_tttS.initiate_game_data(test_data)]
        expected = ['True 00 01', 'False Found existing gameid: ']

        for i in range(2):
            with self.subTest():
                self.assertIn(expected[i], result[i])

    def test_deny_game_start(self):
        test_data = "someP1 someP2 00 01"
        result = self.test_tttS.initiate_game_data(test_data)
        expected = "True 00 01"
        self.assertEqual(result, expected)

    def test_initiate_game(self):
        testStrs = ["p80 0 0 None", "p1 0 0 None", "p0 0 0 None"]
        expected = ["False", "False", "True"]

        for i in range(3):
            with self.subTest():
                self.assertIn(expected[i], self.challenged.initiate_game_start(testStrs[i]))
    
    def test_move_player(self):
        self.challenged.initiate_game_start("p0 0 0 None")
        result = self.challenged.move_player("p1 1 1 None")
        expected = "True False id0 p1 has made a move:"
        self.assertIn(expected, result)

    def tearDown(self):
        self.test_tttS = None
        self.challenged = None

def main(out = sys.stdout, verbosity=1):
    """
    https://www.geeksforgeeks.org/python-logging-test-output-to-a-file/
    The instance of TestLoader class is similar to defaultTestLoader.
    It creates test suites from the specified module by using loadTestsFromModule method
    to search the module for classes derived from unittest's TestCase class and returns a test suite.
    unittest TextTestRunner streams the output to stdout with verbosity set to 1
    """
    loader = unittest.TestLoader()
  
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)

if __name__ == '__main__':
    # unittest.main()
    with open("test_results.txt", "a") as f:
        main(f)