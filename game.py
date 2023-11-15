import sys
import pygame
import pygame.freetype

from settings import Settings
from board import Board
from buttons import Button

class Game:
    def __init__(self):
        """ Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.font=pygame.freetype.SysFont(None, 34)
        self.font.origin=True
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

        #buttons
        self.buttons = Button(self)

        self.selected_value = None

        #error indicator
        self.error_number = False
        self.source = None
        self.target = None
        self.circle_radius = 30
        self.circle_width = 3

        #clock
        self.start_timer = True
        self.ticks = 0
        self.game_status = False
        

    def run_game(self):
        """Start the game"""

        while True:
            self.check_event()
            self.screen.fill(self.settings.bg_color)
    

            if self.game_status:
                self.rect.fit(self.screen_rect)
                self.screen.blit(self.image, self.rect)
                #Draw board
                self.board.draw_board()
                self.board.draw_numbers()

                #Draw input buttons
                self.buttons.draw_input_buttons()

                #Draw error line
                if self.error_number:
                    self.draw_error_line(self.source, self.target)

                #clock
                self.clock_timer()
            else:
                self.screen.fill(self.settings.bg_color)
                self.buttons.draw_menu()
            
            self.clock.tick(60)
            pygame.display.flip()

    def check_event(self):
        """Check events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.game_status:
                        self.check_input(mouse_pos)
                    else:
                        self.check_menu_input(mouse_pos)
    
    def check_menu_input(self, mouse_pos):
        """Check menu option selected"""

        pass

    def check_input(self,mouse_pos):
        self.check_input_buttons(mouse_pos)
        x, y = mouse_pos

        if x <=800 and y <= 800:
            col = x // self.board.square_width
            row = y // self.board.square_width
            if self.selected_value is not None and self.selected_value < 10 and self.buttons.edit_selected == False:
                #update number in board
                self.board.update_board(row, col, self.selected_value)
            elif self.selected_value is not None and self.selected_value < 10 and self.buttons.edit_selected == True:
                #Add notes
                self.board.update_possible(row, col , self.selected_value)
            elif self.selected_value is not None and self.selected_value == 12:
                #delete number in board
                self.board.delete_number_board(row, col)


    def check_input_buttons(self, mouse_pos):
        """Check input selected"""

        if self.buttons.one_rect.collidepoint(mouse_pos):
            self.buttons.default_input_properties(self.buttons.edit_selected)
            self.buttons.one_selected=True
            self.selected_value = 1
        elif self.buttons.two_rect.collidepoint(mouse_pos):
            self.buttons.default_input_properties(self.buttons.edit_selected)
            self.buttons.two_selected=True
            self.selected_value = 2
        elif self.buttons.three_rect.collidepoint(mouse_pos):
            self.buttons.default_input_properties(self.buttons.edit_selected)
            self.buttons.three_selected=True
            self.selected_value = 3
        elif self.buttons.four_rect.collidepoint(mouse_pos):
            self.buttons.default_input_properties(self.buttons.edit_selected)
            self.buttons.four_selected=True
            self.selected_value = 4
        elif self.buttons.five_rect.collidepoint(mouse_pos):
            self.buttons.default_input_properties(self.buttons.edit_selected)
            self.buttons.five_selected=True
            self.selected_value = 5
        elif self.buttons.six_rect.collidepoint(mouse_pos):
            self.buttons.default_input_properties(self.buttons.edit_selected)
            self.buttons.six_selected=True
            self.selected_value = 6
        elif self.buttons.seven_rect.collidepoint(mouse_pos):
            self.buttons.default_input_properties(self.buttons.edit_selected)
            self.buttons.seven_selected=True
            self.selected_value = 7
        elif self.buttons.eight_rect.collidepoint(mouse_pos):
            self.buttons.default_input_properties(self.buttons.edit_selected)
            self.buttons.eight_selected=True
            self.selected_value = 8
        elif self.buttons.nine_rect.collidepoint(mouse_pos):
            self.buttons.default_input_properties(self.buttons.edit_selected)
            self.buttons.nine_selected=True
            self.selected_value = 9
        elif self.buttons.edit_rect.collidepoint(mouse_pos):
            self.buttons.default_input_properties(self.buttons.edit_selected)
            if self.buttons.edit_selected:
                self.buttons.edit_selected = False
            else:
                self.buttons.edit_selected=True
            self.selected_value = None
        elif self.buttons.delete_rect.collidepoint(mouse_pos):
            self.buttons.default_input_properties()
            self.buttons.delete_selected=True
            self.selected_value = 12
        elif self.buttons.check_rect.collidepoint(mouse_pos):
            self.buttons.default_input_properties()
            self.buttons.check_selected=True
            self.selected_value = 13

    def draw_error_line(self, source, target):
        (row1, col1) = source
        (row2, col2) = target
        pygame.draw.circle(self.screen, self.board.number_red_color, (col1* self.board.square_height + self.board.square_height //2, row1* self.board.square_width + self.board.square_width // 2), self.circle_radius, self.circle_width)
        pygame.draw.circle(self.screen, self.board.number_red_color, (col2* self.board.square_height + self.board.square_height //2, row2* self.board.square_width + self.board.square_width // 2), self.circle_radius, self.circle_width)

    def clock_timer(self):
        if self.start_timer:
            self.ticks=pygame.time.get_ticks()
        seconds=int(self.ticks/1000 % 60)
        minutes=int(self.ticks/60000 % 24)
        out='{minutes:02d}:{seconds:02d}'.format(minutes=minutes, seconds=seconds)
        self.font.render_to(self.screen, (self.board.board_width+50, 50), out, self.board.border_color)


if __name__ =='__main__':
    sudoku = Game()
    sudoku.run_game()