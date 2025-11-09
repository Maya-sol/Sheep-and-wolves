class SheepAndWolvesBoard:
    def __init__(self):

        self.board = [['.' for _ in range(8)] for _ in range(8)]
        self.sheep_pos = (0, 1)
        self.board[0][1] = 'S'
        self.wolves_pos = [ (7, 0), (7, 2), (7, 4), (7, 6) ]
        for pos in self.wolves_pos:
            self.board[pos[0]][pos[1]] = 'W'
    
    def display(self):
        for i in range(8):
            for j in range(8):
                print(self.board[i][j] + " ", end = "")
            print()
    
    def is_valid(self, row, colomn):
        if( (0 <= row < 8) and (0 <= colomn < 8)):
            return True
        return False
    
    def is_black(self, row, colomn):
        if (((row + colomn) % 2) == 1 and self.is_valid(row, colomn)):
            return True
        return False
    
    def get_piece(self, row, column):
        if self.is_valid_position(row, column):
            return self.board[row][column]
        return None
    
    def get_valid_moves(self, type, position):
        row, colomn = position
        valid_moves = []
    
        if type == 'S':
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        else: 
            directions = [(-1, -1), (-1, 1)]
    
        for d1, d2 in directions:
            new_row, new_column = row + d1, new_column + d2
            if (self.is_valid(new_row, new_column) and 
                self.is_black(new_row, new_column) and 
                self.board[new_row][new_column] == '.'):
                valid_moves.append((new_row, new_column))
    
        return valid_moves

def is_valid_move(self, from_position, new_position):
    from_row, from_column = from_position
    to_row, to_column = new_position
    
    piece = self.get_piece(from_row, from_column)
    if piece == ".":
        return False
    
    if (not self.is_valid(to_row, to_column) or 
        not self.is_black(to_row, to_column) or 
        self.get_piece_at(to_row, to_column) != '.'):
        return False

    valid_moves = self.get_valid_moves(piece, from_position)
    return new_position in valid_moves


if __name__ == "__main__":
    board = SheepAndWolvesBoard()
