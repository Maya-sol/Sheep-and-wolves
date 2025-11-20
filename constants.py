BOARD_SIZE = 8
INITIAL_SHEEP_POSITION = (0, 1)
INITIAL_WOLVES_POSITIONS = [(7, 0), (7, 2), (7, 4), (7, 6)]
WIDTH, HEIGHT = 704, 704
SQUARE_SIZE = WIDTH // BOARD_SIZE
FRAMES_PER_SECOND = 50
BROWN = (0x43, 0x26, 0x16)
LIGHT_BROWN = (0xfa, 0xd6, 0xa5)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MOVE_DIRECTIONS = {
    'e': (-1, 1),  
    'w': (-1, -1), 
    's': (1, 1),    
    'a': (1, -1)    
}