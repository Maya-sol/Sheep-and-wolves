from board import Board
from pieces import Sheep, Wolf
from constants import MOVE_DIRECTIONS

class SheepAndWolvesGame:
    def __init__(self):
        self.board = Board()
        self.current_turn = 'sheep'
    
    def get_move_input(self):
        choice = input("Enter move (e/w/s/a): ")[0].lower()
        return MOVE_DIRECTIONS.get(choice, (0, 0))
    
    def calculate_new_position(self, current_position, move):
        row, column = current_position
        d1, d2 = move
        return (row + d1, column + d2)
    
    def check_sheep_win(self):
        return self.board.sheep.position[0] == 7
    
    def check_wolves_win(self):
        return len(self.board.sheep.get_valid_moves(self.board)) == 0
    
    def is_game_over(self):
        if self.check_sheep_win():
            return 'sheep wins'
        elif self.check_wolves_win():
            return 'wolves win'
        return None
    
    def make_sheep_move(self):
        move = self.get_move_input()
        new_position = self.calculate_new_position(self.board.sheep.position, move)
        
        if self.board.is_valid_move(self.board.sheep, new_position):
            self.board.sheep.move(new_position, self.board)
            return True
        return False
    
    def make_wolf_move(self):
        try:
            choice = int(input("enter wolf number: "))
            if choice in range(1,4):
                move = self.get_move_input()
                for wolf in self.board.wolves:
                    if wolf.number == choice:
                        new_position = self.calculate_new_position(wolf.position, move)
                        if self.board.is_valid_move(wolf, new_position):
                            wolf.move(new_position, self.board)
                            return True
                        return False
            return False
        except ValueError:
            return False
    
    def play(self):
        while True:
            self.board.display()
            result = self.is_game_over()
            if result:
                print(f"Game over! {result}")
                break
            
            if self.current_turn == 'sheep':
                print("Sheep's turn:")
                if not self.make_sheep_move():
                    print("Invalid move! Try again.")
                    continue
                self.current_turn = 'wolves'
            else:
                print("Wolves' turn:")
                if not self.make_wolf_move():
                    print("Invalid! Try again.")
                    continue
                self.current_turn = 'sheep'

if __name__ == "__main__":
    game = SheepAndWolvesGame()
    game.play()