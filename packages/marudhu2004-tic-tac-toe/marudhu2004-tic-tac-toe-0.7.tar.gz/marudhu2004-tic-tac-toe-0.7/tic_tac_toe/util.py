import random
from .board import Board

toss_coin = lambda: random.choice([True, False])

def parse_positions(board: Board):

    positions = []

    for pos in board.get_board():
        if pos == 1:
            positions.append("x")
        elif pos == 0:
            positions.append("")
        elif pos == -1:
            positions.append("o")    
    
    return positions