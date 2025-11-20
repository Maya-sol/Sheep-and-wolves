# board.py
from constants import BOARD_SIZE, INITIAL_SHEEP_POSITION, INITIAL_WOLVES_POSITIONS
from pieces import Sheep, Wolf

class Board:
    def __init__(self):
        self.grid = [['.' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.sheep = Sheep(INITIAL_SHEEP_POSITION)
        self.wolves = [Wolf(pos) for pos in INITIAL_WOLVES_POSITIONS]
        
        self.update_piece_position(None, self.sheep.position, self.sheep.symbol)
        for wolf in self.wolves:
            self.update_piece_position(None, wolf.position, wolf.symbol)
    
    def display(self):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                print(self.grid[i][j] + " ", end="")
            print()
    
    def is_valid_position(self, row, column):
        return 0 <= row < BOARD_SIZE and 0 <= column < BOARD_SIZE
    
    def is_black_square(self, row, column):
        return ((row + column) % 2) == 1 and self.is_valid_position(row, column)
    
    def is_empty(self, row, column):
        return self.grid[row][column] == '.'
    
    def get_piece_at(self, row, column):
        if self.is_valid_position(row, column):
            return self.grid[row][column]
        return None
    
    def update_piece_position(self, old_position, new_position, symbol):
        if old_position:
            old_row, old_col = old_position
            self.grid[old_row][old_col] = '.'
        
        new_row, new_col = new_position
        self.grid[new_row][new_col] = symbol
    
    def is_valid_move(self, piece, new_position):
        if not self.is_valid_position(*new_position):
            return False
        
        if not self.is_black_square(*new_position):
            return False
        
        if not self.is_empty(*new_position):
            return False
        
        return (new_position in piece.get_valid_moves(self))