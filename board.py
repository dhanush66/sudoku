import pygame
import copy

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
        self.possible_square_width = self.square_width // 3
        self.possible_square_height = self.square_height // 3
        self.border_color = (0, 0, 0)
        self.number_color = (74,44,42)
        self.number_green_color = (0,255,0)
        self.number_red_color = (255,0,0)
        self.trim_size =9
        self.screen = game.screen
        self.settings = game.settings
        self.game = game


    def create_board_play(self, game):
        """Create board from selected difficulty and game no and solve the sudoku using play method"""
        self.sudoku = copy.deepcopy(data[game.difficulty][game.game_no])

        self.board = []
        self.sd = Sd()
        self.sd.result = self.sudoku

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
                #draw possibles (notes)
                if len(self.board[row][col].possible) > 0:
                    i=j=1
                    for val in self.board[row][col].possible:
                        self.font = Font(val,self.border_color, 1)
                        self.font.number_rect.centerx = (col * self.square_height) + i* self.possible_square_height //2 + (i-1) * 12
                        self.font.number_rect.centery = (row * self.square_width) + j* self.possible_square_width //2 + (j-1) * 12
                        self.screen.blit(self.font.number_image, self.font.number_rect)
                        i +=1
                        if i==4:
                            j +=1
                            i =1
                #Draw game numbers
                elif self.board[row][col].number:
                    if self.board[row][col].editable == False and self.board[row][col].number == self.game.selected_value:
                        self.font = Font(self.board[row][col].number,self.game.buttons.circle_selected_color, 2)
                    elif self.board[row][col].editable == False:
                        self.font = Font(self.board[row][col].number,self.number_color, 2)
                    elif self.game.start_timer == False:
                        self.font = Font(self.board[row][col].number,self.number_green_color, 2)
                    elif self.game.buttons.check_selected:
                        if self.sd.result[row][col] == self.board[row][col].number:
                            self.font = Font(self.board[row][col].number,self.number_green_color, 2)
                        else:
                            self.font = Font(self.board[row][col].number,self.number_red_color, 2)
                    # draw user numbers
                    elif self.board[row][col].number == self.game.selected_value:
                        self.font = Font(self.board[row][col].number,self.game.buttons.circle_selected_color, 2)
                    else:
                        self.font = Font(self.board[row][col].number,self.border_color, 2)
                    self.font.number_rect.centerx = (col * self.square_height) + self.square_height//2
                    self.font.number_rect.centery = (row * self.square_width) + self.square_width//2
                    self.screen.blit(self.font.number_image, self.font.number_rect)

    def update_board(self, row, col, val):
        """Update board with selected input if the square is empty"""

        if self.board[row][col].editable and self.game.error_number == False:
            self.board[row][col].number = val
            self.board[row][col].possible.clear()
            #remove input number from possible number of corresponding row, column and square
            self.add_possible_row(row,col) 
            self.add_possible_column(row,col)
            self.add_possible_square(row,col)
            # Check and highlight duplicate number in corresponding row, column and square
            self.check_duplicates(row, col)
            #check game ends
            if self.update_result():
                self.game.start_timer = False

    def update_possible(self, row, col, val):
        """Update board with possible"""
        if self.board[row][col].editable and self.game.error_number == False and self.board[row][col].number == 0:
            self.board[row][col].possible.add(val)

    def delete_number_board(self, row, col):
        """Delete the number in the board"""
        if self.board[row][col].editable:
            if self.game.error_number and self.game.source == (row,col):
                self.board[row][col].number = 0
                self.board[row][col].possible.clear()
                # Check and highlight duplicate number in corresponding row, column and square
                self.check_duplicates(row, col)
            elif self.game.error_number == False:
                self.board[row][col].number = 0
                self.board[row][col].possible.clear()

    def update_result(self):
        """Returns true if borad matches result"""

        for row in range(self.size):
            for col in range(self.size):
                if self.sd.result[row][col] != self.board[row][col].number:
                    return False
                
        return True

    def add_possible_row(self, a,b):
        for m in range(9):
            if len(self.board[a][m].possible) > 0:
                if self.board[a][b].number in self.board[a][m].possible:
                    self.board[a][m].possible.remove(self.board[a][b].number)
          

    def add_possible_column(self, a,b):
        
        for m in range(9):
            if len(self.board[m][b].possible) > 0:
                if self.board[a][b].number in self.board[m][b].possible:
                    self.board[m][b].possible.remove(self.board[a][b].number)


    def add_possible_square(self,a,b):
        m = (a//3) *3
        n = (b//3) * 3
        for m in range(m, m+3):
            for n in range(n, n+3):
                if len(self.board[m][n].possible) > 0:
                    if self.board[a][b].number in self.board[m][n].possible:
                        self.board[m][n].possible.remove(self.board[a][b].number)
            n = (b//3) * 3


    def check_row(self, a,b):
        for m in range(9):
            if m != b:
                if self.board[a][b].number == self.board[a][m].number and self.board[a][b].number != 0:
                    return (a,m)
        return False
          

    def check_column(self, a,b):
        
        for m in range(9):
            if m != a:
                if self.board[a][b].number == self.board[m][b].number and self.board[a][b].number != 0:
                    return (m,b)
            
        return False


    def check_square(self,a,b):
        m = (a//3) *3
        n = (b//3) * 3
        for m in range(m, m+3):
            for n in range(n, n+3):
                if a != m or b != n:
                    if self.board[a][b].number == self.board[m][n].number and self.board[a][b].number != 0:
                        return (m,n)
            n = (b//3) * 3

        return False

    def check_duplicates(self, row, col):
        # Check and highlight duplicate number in corresponding row, column and square

        if self.check_row(row, col) != False:
            self.game.target= self.check_row(row, col)
            self.game.source= (row,col)
            self.game.error_number = True
        elif self.check_column(row, col) != False:
            self.game.target= self.check_column(row, col)
            self.game.source= (row,col)
            self.game.error_number = True
        elif self.check_square(row, col) != False:
            self.game.target= self.check_square(row, col)
            self.game.source= (row,col)
            self.game.error_number = True
        else:
            self.game.error_number = False

    def create_current_board(self):
        """Create 2D arrary with current board numbers"""
        temp = []
        for i in range(self.size):
            temp.append([])
            for j in range(self.size):
                temp[i].append(self.board[i][j].number)

        return temp

    def get_hint(self):
        test = Sd()
        test.result = self.create_current_board()
        print(test.check_next())
