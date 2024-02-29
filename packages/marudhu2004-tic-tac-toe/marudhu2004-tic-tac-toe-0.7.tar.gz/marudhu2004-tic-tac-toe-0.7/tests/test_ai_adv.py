from tic_tac_toe.board import Board
from game_ai.advanced import Advanced
import unittest


class TestGetBestMove(unittest.TestCase):

    def setUp(self) -> None:
        
        self.moves = [(8,1), (7,0), (6,-1)]
        return super().setUp()

    def test_base_case_for_max(self):

        ai = Advanced(True)
        self.assertEqual(ai.get_best_move(self.moves), (8,1))

    def test_base_case_for_min(self):
        
        opp = Advanced(False)
        self.assertEqual(opp.get_best_move(self.moves), (6,-1))