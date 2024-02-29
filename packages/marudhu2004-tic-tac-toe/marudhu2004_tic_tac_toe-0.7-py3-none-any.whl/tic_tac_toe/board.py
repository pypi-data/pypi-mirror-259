from . import errors

class Board:

    def __init__(self, player: bool) -> None:
        self.board = [0 for _ in range(9)]
        self.player = player

    def make_move(self, move):
        
        if (not 0 <= move <= 8) or (move not in self.list_free_moves()):
            raise errors.IllegalMove
        
        self.board[move] = 1 if self.player else -1
        self.player = not self.player

    def list_free_moves(self):
        return [i for i, x in enumerate(self.board) if x == 0]

    def has_winner(self):
        
        # Checking rows
        rows = False
        for i in range(0, 9, 3):
            
            e = [self.board[i + 0], self.board[i + 1], self.board[i + 2]]
            
            if 0 in e:
                continue

            if e[0] == e[1] == e[2]:
                rows = True

        # Checking columns
        columns = False
        for i in range(0, 3):
            
            e = [self.board[i + 0], self.board[i + 3], self.board[i + 6]]
            
            if 0 in e:
                continue

            if e[0] == e[1] == e[2]:
                columns = True
        
        # Checking diagonals
        diagonals = False

        d1 = [self.board[0], self.board[4], self.board[8]]
        d2 = [self.board[2], self.board[4], self.board[6]]

        if not 0 in d1:
            d1 = (d1[0] == d1[1] == d1[2])
        else:
            d1 = False

        if not 0 in d2:
            d2 = (d2[0] == d2[1] == d2[2])  
        else:
            d2 = False

        diagonals = d1 or d2
        
        return rows or columns or diagonals
    
    def game_over(self):
        return self.has_winner() or self.list_free_moves() == []

    def get_player(self):
        return self.player

    def get_board(self):
        return self.board
    
    def get_winner(self):
        if not self.game_over():
            raise errors.GameNotOver
        return 1 if not self.player else -1
    
    def make_copy(self):
        board = Board(self.player)
        board.board = self.board[::]
        return board