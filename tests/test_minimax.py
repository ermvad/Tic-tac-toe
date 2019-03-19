import unittest
import minimax_for_student

class MinimaxFuncTest(unittest.TestCase):
    def test_win(self):
        result = minimax_for_student.win(['O', 'X', 'X', 0, 'O', 0, 0, 0, 'O'], minimax_for_student.computer)
        self.assertEqual(1, result)
        result = minimax_for_student.win(['O', 'X', 'X', 0, 'O', 0, 0, 0, 'O'], minimax_for_student.human)
        self.assertEqual(0, result)
        result = minimax_for_student.win([0, 0, 0, 0, 0, 0, 0, 0, 0], minimax_for_student.computer)
        self.assertEqual(0, result)
        result = minimax_for_student.win([0, 0, 0, 0, 0, 0, 0, 0, 0], minimax_for_student.human)
        self.assertEqual(0, result)

    def test_free_moves(self):
        result = minimax_for_student.free_moves([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8], result)
        result = minimax_for_student.free_moves(['O', 0, 0, 0, 'X', 0, 'O', 'X', 0])
        self.assertEqual([1, 2, 3, 5, 8], result)
        result = minimax_for_student.free_moves(['O', 'O', 'X', 'X', 'O', 'X', 'O', 'X', 'O'])
        self.assertEqual([], result)

    def test_minimax(self):
        result = minimax_for_student.minimax(['O', 'O', 0, 'X', 0, 'X', 'X', 0, 'O'], minimax_for_student.computer)
        self.assertEqual([4, 10], result)
        result = minimax_for_student.minimax([0, 0, 0, 0, 0, 0, 0, 0, 0], minimax_for_student.computer)
        self.assertEqual([0, 10], result)
        result = minimax_for_student.minimax(['X', 'X', 'X', 0, 0, 'O', 'O', 0, 0], minimax_for_student.computer)
        self.assertEqual(10, result)

if __name__ == '__main__':
    unittest.main()