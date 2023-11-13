import pygame

from tiles import Tiles
from font import Font
from sudoku import Sd
from buttons import Button
from data import data

class Board:
    def __init__(self, game):
        #Board parameters
        self.board_width = 800
        self.board_height = 800
        self.size = 9
        self.square_width = self.board_width //self.size
        self.square_height = self.board_height//self.size
        self.border_color = (0, 0, 0)
        self.number_color = (74,44,42)
        self.number_green_color = (0,255,0)
        self.number_red_color = (255,0,0)
        self.trim_size =9
        self.screen = game.screen
        self.settings = game.settings
        self.game = game
        self.sudoku = data
        
        self.board = []
        self.sd = Sd()
        self.create_board()

        self.sd.play()

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

    def create_board(self):
        """create board using sudoku"""

        for row in range(self.size):
            self.board.append([])
            for col in range(self.size):
                if self.sudoku[row][col]:
                    self.board[row].append(Tiles(self.sudoku[row][col]))
                    self.board[row][col].editable = False
                else:
                    self.board[row].append(Tiles(0))
                    self.board[row][col].editable = True

    def draw_numbers(self):
        """Draw the numbers"""


        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col].number:
                    if self.board[row][col].editable == False:
                        self.font = Font(self.board[row][col].number,self.number_color)
                    elif self.game.buttons.check_selected:
                        if self.sd.result[row][col] == self.board[row][col].number:
                            self.font = Font(self.board[row][col].number,self.number_green_color)
                        else:
                            self.font = Font(self.board[row][col].number,self.number_red_color)

                    else:
                        self.font = Font(self.board[row][col].number,self.border_color)
                    self.font.number_rect.centerx = (col * self.square_height) + self.square_height//2
                    self.font.number_rect.centery = (row * self.square_width) + self.square_width//2
                    self.screen.blit(self.font.number_image, self.font.number_rect)

    def update_board(self, row, col, val):
        """Update board with selected input if the square is empty"""

        if self.board[row][col].editable:
            self.board[row][col].number = val


    def delete_number_board(self, row, col):
        """Delete the number in the board"""

        if self.board[row][col].editable:
            self.board[row][col].number = 0

    def update_result(self):
        """Returns true if borad matches result"""

        for row in range(self.size):
            for col in range(self.size):
                if self.result[row][col] != self.board[row][col].numbers:
                    return False
                
        return True


