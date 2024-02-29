import unittest
from tic_tac_toe.board import Board
from tic_tac_toe.errors import *

class TestMakeMove(unittest.TestCase):

    def setUp(self) -> None:
        self.board = Board(True)
        return super().setUp()
    
    def test_valid_move(self):
        
        self.board.make_move(0)

    def test_invalid_move(self):
        
        with self.assertRaises(IllegalMove):
            self.board.make_move(-1)

        with self.assertRaises(IllegalMove):
            self.board.make_move(10)

    def test_same_move_over_and_over(self):

        self.board.make_move(0)

        with self.assertRaises(IllegalMove):
            self.board.make_move(0)


class TestFreeMoves(unittest.TestCase):
    
    def setUp(self) -> None:
        self.board = Board(True)
        return super().setUp()
    
    def test_empty_board(self):
        
        self.assertEqual(self.board.list_free_moves(), [0,1,2,3,4,5,6,7,8])

    def test_no_empty(self):
        
        self.board.board = [1 for _ in range(9)]

        self.assertEqual(self.board.list_free_moves(), [])

    def test_has_some_moves(self):

        self.board.make_move(5)

        self.assertEqual(self.board.list_free_moves(), [0,1,2,3,4,6,7,8])
