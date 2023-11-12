import sys
import pygame

from settings import Settings
from board import Board

class Game:
    def __init__(self):
        """ Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("SUDOKU")

        #Load the background image
        self.image = pygame.image.load('images/seamless.jpg')
        self.rect = self.image.get_rect()
        # self.rect.midbottom = self.screen_rect.midbottom
        
        #Board
        self.board = Board(self)
        

    def run_game(self):
        """Start the game"""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
    
            self.screen.fill(self.settings.bg_color)
            self.rect.fit(self.screen_rect)
            self.screen.blit(self.image, self.rect)
            #Draw board
            self.board.draw_board()
            self.board.draw_numbers()


            self.clock.tick(40)
            pygame.display.flip()


if __name__ =='__main__':
    sudoku = Game()
    sudoku.run_game()