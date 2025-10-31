import unittest
from core.board import Board


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_initial_state(self):
        """Поле должно быть пустое, первый ход X"""
        self.assertEqual(self.board.current, 'X')
        for row in self.board.grid:
            for cell in row:
                self.assertIsNone(cell)

    def test_make_move_and_switch(self):
        """После хода игрок должен меняться"""
        self.assertTrue(self.board.make_move(0, 0))
        self.assertEqual(self.board.grid[0][0], 'X')
        self.assertEqual(self.board.current, 'O')

    def test_invalid_move(self):
        """Нельзя ходить в занятую клетку"""
        self.board.make_move(0, 0)
        self.assertFalse(self.board.make_move(0, 0))

    def test_winner_row(self):
        """Победа по строке"""
        self.board.grid = [['X', 'X', None],
                           [None, None, None],
                           [None, None, None]]
        self.board.make_move(0, 2)  # X завершает ряд
        self.assertEqual(self.board.winner, 'X')

    def test_winner_column(self):
        """Победа по колонке"""
        self.board.grid = [['O', None, None],
                           ['O', None, None],
                           [None, None, None]]
        self.board.current = 'O'
        self.board.make_move(2, 0)
        self.assertEqual(self.board.winner, 'O')

    def test_winner_diagonal(self):
        """Победа по диагонали"""
        self.board.grid = [['X', None, None],
                           [None, 'X', None],
                           [None, None, None]]
        self.board.make_move(2, 2)
        self.assertEqual(self.board.winner, 'X')

    def test_draw(self):
        """Ничья на заполненном поле"""
        self.board.grid = [['X', 'O', 'X'],
                           ['X', 'O', 'O'],
                           ['O', 'X', None]]
        self.board.current = 'X'
        self.board.make_move(2, 2)  # последний ход
        self.assertEqual(self.board.winner, 'Draw')

    def test_reset(self):
        """После reset поле чистое"""
        self.board.make_move(0, 0)
        self.board.reset()
        self.assertIsNone(self.board.winner)
        for row in self.board.grid:
            for cell in row:
                self.assertIsNone(cell)


if __name__ == '__main__':
    unittest.main()
