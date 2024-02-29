from tic_tac_toe.board import Board
from tic_tac_toe.ai import AiTemplate

class Advanced(AiTemplate):

    def __init__(self, player):
        self.player = player
        self.target = self.__target(player)

    
    @staticmethod
    def __target(player):
        return 1 if player else -1
    
    def calculate_moves(self, board :Board):

        # getting the node value
        if board.game_over():
            if board.has_winner():
                value = board.get_winner()
            else:
                value = 0
        
            return value
        
        # Recurse with the other player
        values = []
        opponent = Advanced(not self.player)
        possible_moves = board.list_free_moves()
        for move in possible_moves:
            next_board = board.make_copy()
            next_board.make_move(move)
            calc_value = opponent.calculate_moves(next_board)
            values.append((move, calc_value))
    
        return self.get_best_move(values)[1]

    def get_best_move(self, values :list):

        max_value = (0, -2)
        min_value = (0, 2)
        
        for value in values:

            if value[1] > max_value[1]:
                max_value = value
            
            if value[1] < min_value[1]:
                min_value = value

        return max_value if self.player else min_value

    def make_move(self, board: Board):

        available_moves = board.list_free_moves()
        values = []
        for move in available_moves:
            values.append((move,self.calculate_moves(board)))
        
        return self.get_best_move(values)[0]


if __name__ == "__main__":

    ad = Advanced(True)
    board = Board(True)
