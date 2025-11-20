import pygame
from constants import*
import sys
from board import*

class SheepAndWolves:
    def __init__(self):
        self.board = Board()
        self.current_turn = 'sheep'
        self.screen = pygame.display.set_mode((HEIGHT, WIDTH))
        pygame.display.set_caption("Sheep and Wolves")
        self.clock = pygame.time.Clock()
        self.selected = False


    def draw_board(self):
        self.screen.fill(BROWN)
        for row in range(8):
            for col in range(8):
                x = col * SQUARE_SIZE
                y = row * SQUARE_SIZE
                cell_rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
           
                if ((row + col)%2 == 0):
                    pygame.draw.rect(self.screen, LIGHT_BROWN, cell_rect)
            
                pygame.draw.rect(self.screen, BLACK, cell_rect, 1)

    def draw_piece(self, piece):
        row, col = piece.position
        x = col * SQUARE_SIZE + SQUARE_SIZE // 2
        y = row * SQUARE_SIZE + SQUARE_SIZE // 2
    
        if piece.symbol == 'S':
            color = (255, 255, 255)
        else:  
            color = (128, 128, 128)
    
        pygame.draw.circle(self.screen, color, (x, y), 30)
        pygame.draw.circle(self.screen, BLACK, (x, y), 30, 2)
    
        if piece.selected == True:
            pygame.draw.circle(self.screen, (255, 215, 0), (x, y), 33, 3)

    def handle_click(self, position):
        row, col = position[0]//SQUARE_SIZE, position[1]//SQUARE_SIZE
        if (self.current_turn == 'sheep' and col == self.board.sheep.position[0] 
                        and row == self.board.sheep.position[1] and self.selected is False):
            self.board.sheep.selected = True
            self.selected = True
            return

        elif (self.selected is False):
            for wolf in self.board.wolves:
                if (self.current_turn == 'wolf' and col == wolf.position[0] and row == wolf.position[1]):
                    wolf.selected = True
                    self.selected = True
                    return
        
        if (self.current_turn == 'sheep' and self.board.sheep.selected and self.selected is True):
            if (self.board.is_valid_move(self.board.sheep, (col, row)) and 
                                                (col, row)in self.board.sheep.get_valid_moves(self.board)):
                self.board.sheep.move((col, row), self.board)
                self.current_turn = 'wolf'
        
        for wolf in self.board.wolves :
            if (self.current_turn == 'wolf' and wolf.selected and self.selected is True):
                if (self.board.is_valid_move(wolf, (col, row)) and 
                                                (col, row)in wolf.get_valid_moves(self.board)):
                    wolf.move((col, row), self.board)
                    self.current_turn = 'sheep'

        self.board.sheep.selected = False
        self.selected = False
        for wolf in self.board.wolves:
            wolf.selected = False

    def try_move(self, piece, piece_type, target_pos):
        target_row, target_col = target_pos
        if not (0 <= target_row < 8 and 0 <= target_col < 8):
            print("Move out of bounds")
            return False
            
        position_occupied = False
        if self.board.sheep.position == target_pos:
            position_occupied = True
        else:
            for wolf in self.board.wolves:
                if wolf.position == target_pos:
                    position_occupied = True
                    break
        
        if position_occupied:
            print("Target position occupied")
            return False

        current_row, current_col = piece.position
        if piece_type == 'sheep':
            if self.board.is_valid_move(self.board.sheep, target_pos):
                self.board.sheep.move(target_pos, self.board)
            return True
        
        elif piece_type == 'wolf':
            if (abs(target_row - current_row) == 1 and 
                abs(target_col - current_col) == 1):
                piece.position = target_pos
                print("Wolf moved")
                return True
        
        print("Invalid move for this piece")
        return False

    def check_sheep_win(self):
        if (self.board.sheep.position[0] == 7):
            return True
        sum = 0
        for wolf in self.board.wolves:
            sum += len(wolf.get_valid_moves(self.board))
        if (sum == 0):
            return True
        return False
    
    def check_wolves_win(self):
        return len(self.board.sheep.get_valid_moves(self.board)) == 0
    
    def is_over(self):
        if self.check_sheep_win():
            return 'Baaa! sheep wins'
        elif self.check_wolves_win():
            return 'Awoo! wolves win'
        return None

    def show_winner(self, text):
        font = pygame.font.Font(None, 100)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (WIDTH // 2, HEIGHT // 2)
        background_rect = pygame.Rect(0, HEIGHT//2 - SQUARE_SIZE, WIDTH, 2*SQUARE_SIZE)
        pygame.draw.rect(self.screen, (30,30,30), background_rect)
        self.screen.blit(text_surface, text_rect)

if __name__ == "__main__":
    pygame.init()
    game = SheepAndWolves()
    running = True
    while (game.is_over() is None) and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    game.handle_click(event.pos)

        game.draw_board()
        game.draw_piece(game.board.sheep)
        for wolf in game.board.wolves:
            game.draw_piece(wolf)
        pygame.display.update()
        game.clock.tick(FRAMES_PER_SECOND)
    winner = game.is_over()
    while(running):
        font = pygame.font.Font()
        try:
           game.show_winner(winner)
        except:
            winner is None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        game.clock.tick(FRAMES_PER_SECOND)
    pygame.quit()
    sys.exit()