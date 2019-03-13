import unittest
import minimax_for_student

class MinimaxFuncTest(unittest.TestCase):
    def test_win(self):
        result = minimax_for_student.win(['C', 'H', 'H', 0, 'C', 0, 0, 0, 'C'], minimax_for_student.computer)
        self.assertEqual(1, result)
        result = minimax_for_student.win(['C', 'H', 'H', 0, 'C', 0, 0, 0, 'C'], minimax_for_student.human)
        self.assertEqual(0, result)
        result = minimax_for_student.win([0, 0, 0, 0, 0, 0, 0, 0, 0], minimax_for_student.computer)
        self.assertEqual(0, result)
        result = minimax_for_student.win([0, 0, 0, 0, 0, 0, 0, 0, 0], minimax_for_student.human)
        self.assertEqual(0, result)

    def test_free_moves(self):
        result = minimax_for_student.free_moves([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8], result)
        result = minimax_for_student.free_moves(['C', 0, 0, 0, 'H', 0, 'C', 'H', 0])
        self.assertEqual([1, 2, 3, 5, 8], result)
        result = minimax_for_student.free_moves(['C', 'C', 'H', 'H', 'C', 'H', 'C', 'H', 'C'])
        self.assertEqual([], result)

if __name__ == '__main__':
    unittest.main()