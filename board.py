import pygame

from font import Font

class Board:
    def __init__(self, game):
        #Board parameters
        self.board_width = 800
        self.board_height = 800
        self.size = 9
        self.square_width = self.board_width //self.size
        self.square_height = self.board_height//self.size
        self.border_color = (0, 0, 0)
        self.trim_size =9
        self.screen = game.screen
        self.settings = game.settings
        self.board = [[0,0,7,0,0,0,0,0,6],
                      [0,2,0,6,7,0,0,0,0],
                      [8,6,4,0,9,1,0,3,7],
                      [0,0,6,3,0,4,0,7,1],
                      [2,0,8,0,0,0,6,0,3],
                      [0,4,0,5,0,6,8,0,0],
                      [4,8,0,7,6,0,1,5,9],
                      [0,0,0,0,5,2,0,6,0],
                      [6,0,0,0,0,0,3,0,0]]
        
        self.font = 0

    def draw_board(self):
        """Draw border of board"""
        for i in range(self.size+1):
                if i%3 == 0:
                    pygame.draw.line(self.screen, self.border_color, (0,(i*self.square_height)), (self.board_width-self.trim_size,(i*self.square_height)), width=4 )
                else:
                    pygame.draw.line(self.screen, self.border_color, (0,(i*self.square_height)), (self.board_width-self.trim_size,(i*self.square_height)), width=1 )

        for j in range(self.size+1):
            if j%3 == 0:
                pygame.draw.line(self.screen, self.border_color, ((j*self.square_width),0), ((j*self.square_width),self.board_height-self.trim_size), width=4 )
            else:
                pygame.draw.line(self.screen, self.border_color, ((j*self.square_width),0), ((j*self.square_width),self.board_height-self.trim_size), width=1 )

    def draw_numbers(self):
        """Draw the numbers"""

        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col]:
                    self.font = Font(self.board[row][col])
                    self.font.number_rect.centerx = (col * self.square_height) + self.square_height//2
                    self.font.number_rect.centery = (row * self.square_width) + self.square_width//2
                    self.screen.blit(self.font.number_image, self.font.number_rect)
