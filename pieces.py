from constants import MOVE_DIRECTIONS
from board import*
class Piece:
    def __init__(self, symbol, position):
        self.symbol = symbol
        self.position = position
        self.selected = False
    
    def get_valid_moves(self, board):
        raise NotImplementedError()
    
    def move(self, new_position, board):
        old_position = self.position
        self.position = new_position
        board.update_piece_position(old_position, new_position, self.symbol)
        return True

class Sheep(Piece):
    def __init__(self, position):
        super().__init__('S', position)
    
    def get_valid_moves(self, board):
        row, column = self.position
        valid_moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        for d1, d2 in directions:
            new_row, new_column = row + d1, column + d2
            if (board.is_valid_position(new_row, new_column) and 
                board.is_black_square(new_row, new_column) and 
                board.is_empty(new_row, new_column)):
                valid_moves.append((new_row, new_column))
        
        return valid_moves

class Wolf(Piece):
    def __init__(self, position):
        super().__init__('W', position)
        self.number = position[1]/2 + 1
    
    def get_valid_moves(self, board):
        row, column = self.position
        valid_moves = []
        directions = [(-1, -1), (-1, 1)] 
        
        for d1, d2 in directions:
            new_row, new_column = row + d1, column + d2
            if (board.is_valid_position(new_row, new_column) and 
                board.is_black_square(new_row, new_column) and 
                board.is_empty(new_row, new_column)):
                valid_moves.append((new_row, new_column))
        
        return valid_moves