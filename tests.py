import unittest

from tictactoe import EMPTY, O, X, InvalidActionError, initial_state, player, result


class test_tictactoe(unittest.TestCase):
    def test_player(self):
        board = initial_state()

        self.assertEqual(player(board), X)

        board[0][0] = X
        self.assertEqual(player(board), O)

        board[0][1] = O
        self.assertEqual(player(board), X)

        board[1][1] = O
        self.assertEqual(player(board), X)

    def test_result(self):
        board = initial_state()

        action = (0, 1)
        after = [[EMPTY, X, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(result(board, action), after)

        self.assertRaises(InvalidActionError, result, after, action)

        action = (5, 1)
        self.assertRaises(IndexError, result, board, action)
        action = (1, 6)
        self.assertRaises(IndexError, result, board, action)


if __name__ == "__main__":
    unittest.main()
