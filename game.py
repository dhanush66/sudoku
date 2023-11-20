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

        #menu
        self.difficulty = 0
        self.game_no = 0

        #clock
        self.start_timer = True
        self.ticks = 0
        self.prev_ticks = 0
        self.game_status = False

        #error indicator
        self.error_number = False
        self.source = None
        self.target = None
        self.circle_radius = 20
        self.circle_width = 3

        #stores hint messages
        self.hint_message = None
        
        #Board
        self.board_created = False
        self.board = Board(self)

        #buttons
        self.selected_value = None
        self.buttons = Button(self)
        

    def run_game(self):
        """Start the game"""
        while True:
            self.check_event()
            self.screen.fill(self.settings.bg_color)
    

            if self.game_status:
                #create board
                if self.board_created == False:
                    self.board.create_board_play(self)
                    self.board_created = True

                self.rect.fit(self.screen_rect)
                self.screen.blit(self.image, self.rect)
                #Draw board
                self.board.draw_board()
                self.board.draw_numbers()

                #Draw input buttons
                self.buttons.draw_input_buttons()

                #Draw error line if same no available in same row, column and square
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

        if self.buttons.diff_bck_arrow_rect.collidepoint(mouse_pos):
            self.difficulty -=1
        elif self.buttons.diff_fwd_arrow_rect.collidepoint(mouse_pos):
            self.difficulty +=1
        elif self.buttons.no_bck_arrow_rect.collidepoint(mouse_pos):
            self.game_no -=1
        elif self.buttons.no_fwd_arrow_rect.collidepoint(mouse_pos):
            self.game_no +=1
        elif self.buttons.start.number_rect.collidepoint(mouse_pos):
            self.game_status = True
            self.start_timer = True
            self.prev_ticks = pygame.time.get_ticks()

        if self.difficulty < 0:
            self.difficulty =0
        if self.difficulty > 3:
            self.difficulty = 3
        if self.game_no < 0:
            self.game_no = 0
        if self.game_no > 9:
            self.game_no =9

    def check_input(self,mouse_pos):
        self.check_input_buttons(mouse_pos)
        x, y = mouse_pos

        if x <=self.board.board_width and y <= self.board.board_height:
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
        elif self.buttons.menu.number_rect.collidepoint(mouse_pos):
            self.game_status = False
            self.start_timer = False
            self.board_created = False
            self.prev_ticks = pygame.time.get_ticks()
        elif self.buttons.hint.number_rect.collidepoint(mouse_pos):
            # store the hint message
            self.hint_message = self.board.get_hint()
            if self.buttons.hint_selected:
                self.buttons.hint_selected = False
                self.hint_message = None
            else:
                self.buttons.hint_selected=True
        elif self.buttons.possible.number_rect.collidepoint(mouse_pos):
            self.board.get_possible()

    def draw_error_line(self, source, target):
        (row1, col1) = source
        (row2, col2) = target
        pygame.draw.circle(self.screen, self.board.number_red_color, (col1* self.board.square_height + self.board.square_height //2, row1* self.board.square_width + self.board.square_width // 2), self.circle_radius, self.circle_width)
        pygame.draw.circle(self.screen, self.board.number_red_color, (col2* self.board.square_height + self.board.square_height //2, row2* self.board.square_width + self.board.square_width // 2), self.circle_radius, self.circle_width)

    def clock_timer(self):
        if self.start_timer:
            self.ticks=pygame.time.get_ticks()
            self.ticks -= self.prev_ticks
        seconds=int(self.ticks/1000 % 60)
        minutes=int(self.ticks/60000 % 24)
        out='{minutes:02d}:{seconds:02d}'.format(minutes=minutes, seconds=seconds)
        self.font.render_to(self.screen, (self.board.board_width+50, 50), out, self.board.border_color)


if __name__ =='__main__':
    sudoku = Game()
    sudoku.run_game()