import unittest
import minimax_for_student as minimax

class MinimaxFuncTest(unittest.TestCase):
    def test_win(self):
        result = minimax.win(['O', 'X', 'X', 0, 'O', 0, 0, 0, 'O'], minimax.computer)
        self.assertEqual(1, result)
        result = minimax.win(['O', 'X', 'X', 0, 'O', 0, 0, 0, 'O'], minimax.human)
        self.assertEqual(0, result)
        result = minimax.win([0, 0, 0, 0, 0, 0, 0, 0, 0], minimax.computer)
        self.assertEqual(0, result)
        result = minimax.win([0, 0, 0, 0, 0, 0, 0, 0, 0], minimax.human)
        self.assertEqual(0, result)

    def test_free_moves(self):
        result = minimax.free_moves([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8], result)
        result = minimax.free_moves(['O', 0, 0, 0, 'X', 0, 'O', 'X', 0])
        self.assertEqual([1, 2, 3, 5, 8], result)
        result = minimax.free_moves(['O', 'O', 'X', 'X', 'O', 'X', 'O', 'X', 'O'])
        self.assertEqual([], result)

    def test_minimax(self):
        result = minimax.minimax(['O', 'O', 0, 'X', 0, 'X', 'X', 0, 'O'], minimax.computer)
        self.assertEqual((2, 10), result)
        result = minimax.minimax([0, 0, 0, 0, 0, 0, 0, 0, 0], minimax.computer)
        self.assertEqual((0, 0), result)
        result = minimax.minimax(['X', 'X', 'X', 0, 0, 'O', 'O', 0, 0], minimax.computer)
        self.assertEqual((-1, -10), result)

if __name__ == '__main__':
    unittest.main()
