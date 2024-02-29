from tic_tac_toe.board import Board
from tic_tac_toe.ai import AiTemplate

import random

class Beginner(AiTemplate):

    def __init__(self, player):
        self.player = player
        self.target = self.__target(player)

    @staticmethod
    def __target(player):
        return 1 if player else -1
    
    def make_move(self, board: Board):
        available_moves = board.list_free_moves()

        # Return a winning move if it exist
        for move in available_moves:

            next_board = board.make_copy()
            next_board.make_move(move)

            if next_board.has_winner():
                if next_board.get_winner() == self.target:
                    return move
            
        # Return move to counter opponent
        target = self.__target(not board.player)
        for move in available_moves:

            next_board = board.make_copy()
            next_board.player = not board.player
            next_board.make_move(move)

            if next_board.has_winner():
                if next_board.get_winner() == target:
                    return move
            
        # Return a random move if none of the above 
        return random.choice(available_moves)