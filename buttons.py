import pygame

from font import Font


class Button:
    """Create input buttons"""
    def __init__(self, game):
        self.board =game.board
        self.screen = game.screen
        self.settings = game.settings
        self.game = game
        #Input images and rect
        self.one_image = pygame.image.load('images/inputs/digit-1.png')
        self.two_image = pygame.image.load('images/inputs/digit-2.png')
        self.three_image = pygame.image.load('images/inputs/digit-3.png')
        self.four_image = pygame.image.load('images/inputs/digit-4.png')
        self.five_image = pygame.image.load('images/inputs/digit-5.png')
        self.six_image = pygame.image.load('images/inputs/digit-6.png')
        self.seven_image = pygame.image.load('images/inputs/digit-7.png')
        self.eight_image = pygame.image.load('images/inputs/digit-8.png')
        self.nine_image = pygame.image.load('images/inputs/digit-9.png')
        self.edit_image = pygame.image.load('images/inputs/edit.png')
        self.delete_image = pygame.image.load('images/inputs/stick-cross.png')
        self.check_image = pygame.image.load('images/inputs/stick-check.png')
        self.diff_fwd_arrow_image = pygame.image.load('images/inputs/arrow-block.png')
        self.diff_bck_arrow_image = pygame.transform.rotate(self.diff_fwd_arrow_image, 180)
        self.no_fwd_arrow_image = pygame.image.load('images/inputs/arrow-block.png')
        self.no_bck_arrow_image = pygame.transform.rotate(self.no_fwd_arrow_image, 180)
        self.one_rect = self.one_image.get_rect()
        self.two_rect = self.two_image.get_rect()
        self.three_rect = self.three_image.get_rect()
        self.four_rect = self.four_image.get_rect()
        self.five_rect = self.five_image.get_rect()
        self.six_rect = self.six_image.get_rect()
        self.seven_rect = self.seven_image.get_rect()
        self.eight_rect = self.eight_image.get_rect()
        self.nine_rect = self.nine_image.get_rect()
        self.edit_rect = self.edit_image.get_rect()
        self.delete_rect = self.delete_image.get_rect()
        self.check_rect = self.check_image.get_rect()
        self.diff_fwd_arrow_rect = self.diff_fwd_arrow_image.get_rect()
        self.diff_bck_arrow_rect = self.diff_bck_arrow_image.get_rect()
        self.no_fwd_arrow_rect = self.no_fwd_arrow_image.get_rect()
        self.no_bck_arrow_rect = self.no_bck_arrow_image.get_rect()
        self.default_image_size = (50,50)
        
        self.default_input_properties()
        #Circle properties
        self.circle_color = (0, 0, 0)
        self.circle_selected_color = (255, 255, 0)
        self.cricle_radius = 30
        self.circle_width = 3
        #Menu properties
        self.game_heading_color = (0,0,0)
        self.box_color = (0,0,0)
        self.start = None
        self.menu = None


    def default_input_properties(self, edit_selected=False):
        #Number selected properties
        self.one_selected = False
        self.two_selected = False
        self.three_selected = False
        self.four_selected = False
        self.five_selected = False
        self.six_selected = False
        self.seven_selected = False
        self.eight_selected = False
        self.nine_selected = False
        self.delete_selected = False
        self.check_selected = False

        if edit_selected:
            pass
        else:
            self.edit_selected = False

    def draw_input_buttons(self):

        #Draw Menu button
        pygame.draw.rect(self.screen, self.box_color, [self.board.board_width+ 50, self.board.square_height * 9, 140, 60], 5, border_radius=15)
        self.menu = Font("Menu",self.game_heading_color, 2)
        self.menu.number_rect.centerx = self.board.board_width +55 + 60
        self.menu.number_rect.centery = self.board.square_height * 9 + 30
        self.screen.blit(self.menu.number_image, self.menu.number_rect)

        
        #Draw number one
        self.one_rect.topleft =(self.board.board_width + 10, (self.board.square_height * 3)+ 10)
        if self.one_selected:
            pygame.draw.circle(self.screen, self.circle_selected_color, (self.board.board_width + 5 + self.cricle_radius, (self.board.square_height * 3)+ 10 + self.cricle_radius), self.cricle_radius, self.circle_width)
        else:
            pygame.draw.circle(self.screen, self.circle_color, (self.board.board_width + 5 + self.cricle_radius, (self.board.square_height * 3)+ 10 + self.cricle_radius), self.cricle_radius, self.circle_width)
        self.screen.blit(pygame.transform.scale(self.one_image, self.default_image_size), self.one_rect)

        #Draw number two
        self.two_rect.topleft = (self.board.board_width + 10 + self.board.square_width - 15, (self.board.square_height * 3)+ 10)
        if self.two_selected:
            pygame.draw.circle(self.screen, self.circle_selected_color, (self.board.board_width + 5 + self.cricle_radius +(1*self.board.square_width-15), (self.board.square_height * 3)+ 10 + self.cricle_radius), self.cricle_radius, self.circle_width)
        else:
            pygame.draw.circle(self.screen, self.circle_color, (self.board.board_width + 5 + self.cricle_radius +(1*self.board.square_width-15), (self.board.square_height * 3)+ 10 + self.cricle_radius), self.cricle_radius, self.circle_width)
        self.screen.blit(pygame.transform.scale(self.two_image, self.default_image_size), self.two_rect)
        

        #Draw number three
        self.three_rect.topleft = (self.board.board_width + 10 + (2*self.board.square_width-30), (self.board.square_height * 3)+ 10)
        if self.three_selected:
            pygame.draw.circle(self.screen, self.circle_selected_color, (self.board.board_width + 5 + self.cricle_radius +(2*self.board.square_width)-30, (self.board.square_height * 3)+ 10 + self.cricle_radius), self.cricle_radius, self.circle_width)
        else:
            pygame.draw.circle(self.screen, self.circle_color, (self.board.board_width + 5 + self.cricle_radius +(2*self.board.square_width)-30, (self.board.square_height * 3)+ 10 + self.cricle_radius), self.cricle_radius, self.circle_width)
        self.screen.blit(pygame.transform.scale(self.three_image, self.default_image_size), self.three_rect)

        #Draw number four
        self.four_rect.topleft =(self.board.board_width + 10, (self.board.square_height * 4)+ 10)
        if self.four_selected:
            pygame.draw.circle(self.screen, self.circle_selected_color, (self.board.board_width + 5 + self.cricle_radius, (self.board.square_height * 4)+ 10 + self.cricle_radius), self.cricle_radius, self.circle_width)
        else:
            pygame.draw.circle(self.screen, self.circle_color, (self.board.board_width + 5 + self.cricle_radius, (self.board.square_height * 4)+ 10 + self.cricle_radius), self.cricle_radius, self.circle_width)
        self.screen.blit(pygame.transform.scale(self.four_image, self.default_image_size), self.four_rect)

        #Draw number five
        self.five_rect.topleft = (self.board.board_width + 10 + self.board.square_width - 15, (self.board.square_height * 4)+ 10)
        if self.five_selected:
            pygame.draw.circle(self.screen, self.circle_selected_color, (self.board.board_width + 5 + self.cricle_radius +(1*self.board.square_width-15), (self.board.square_height * 4)+ 10 + self.cricle_radius), self.cricle_radius, self.circle_width)
        else:
            pygame.draw.circle(self.screen, self.circle_color, (self.board.board_width + 5 + self.cricle_radius +(1*self.board.square_width-15), (self.board.square_height * 4)+ 10 + self.cricle_radius), self.cricle_radius, self.circle_width)
        self.screen.blit(pygame.transform.scale(self.five_image, self.default_image_size), self.five_rect)

        #Draw number six
        self.six_rect.topleft = (self.board.board_width + 10 + (2*self.board.square_width-30), (self.board.square_height * 4)+ 10)
        if self.six_selected:
            pygame.draw.circle(self.screen, self.circle_selected_color, (self.board.board_width + 5 + self.cricle_radius +(2*self.board.square_width)-30, (self.board.square_height * 4)+ 10 + self.cricle_radius), self.cricle_radius, self.circle_width)
        else:
            pygame.draw.circle(self.screen, self.circle_color, (self.board.board_width + 5 + self.cricle_radius +(2*self.board.square_width)-30, (self.board.square_height * 4)+ 10 + self.cricle_radius), self.cricle_radius, self.circle_width)
        self.screen.blit(pygame.transform.scale(self.six_image, self.default_image_size), self.six_rect)

        #Draw number seven
        self.seven_rect.topleft =(self.board.board_width + 10, (self.board.square_height * 5)+ 10)
        if self.seven_selected:
            pygame.draw.circle(self.screen, self.circle_selected_color, (self.board.board_width + 5 + self.cricle_radius, (self.board.square_height * 5)+ 10 + self.cricle_radius), self.cricle_radius, self.circle_width)
        else:
            pygame.draw.circle(self.screen, self.circle_color, (self.board.board_width + 5 + self.cricle_radius, (self.board.square_height * 5)+ 10 + self.cricle_radius), self.cricle_radius, self.circle_width)
        self.screen.blit(pygame.transform.scale(self.seven_image, self.default_image_size), self.seven_rect)

        #Draw number eight
        self.eight_rect.topleft = (self.board.board_width + 10 + self.board.square_width - 15, (self.board.square_height * 5)+ 10)
        if self.eight_selected:
            pygame.draw.circle(self.screen, self.circle_selected_color, (self.board.board_width + 5 + self.cricle_radius +(1*self.board.square_width-15), (self.board.square_height * 5)+ 10 + self.cricle_radius), self.cricle_radius, self.circle_width)
        else:
            pygame.draw.circle(self.screen, self.circle_color, (self.board.board_width + 5 + self.cricle_radius +(1*self.board.square_width-15), (self.board.square_height * 5)+ 10 + self.cricle_radius), self.cricle_radius, self.circle_width)
        self.screen.blit(pygame.transform.scale(self.eight_image, self.default_image_size), self.eight_rect)

        #Draw number nine
        self.nine_rect.topleft = (self.board.board_width + 10 + (2*self.board.square_width-30), (self.board.square_height * 5)+ 10)
        if self.nine_selected:
            pygame.draw.circle(self.screen, self.circle_selected_color, (self.board.board_width + 5 + self.cricle_radius +(2*self.board.square_width)-30, (self.board.square_height * 5)+ 10 + self.cricle_radius), self.cricle_radius, self.circle_width)
        else:
            pygame.draw.circle(self.screen, self.circle_color, (self.board.board_width + 5 + self.cricle_radius +(2*self.board.square_width)-30, (self.board.square_height * 5)+ 10 + self.cricle_radius), self.cricle_radius, self.circle_width)
        self.screen.blit(pygame.transform.scale(self.nine_image, self.default_image_size), self.nine_rect)

        #Draw edit icon
        self.edit_rect.topleft =(self.board.board_width + 10, (self.board.square_height * 6)+ 10)
        if self.edit_selected:
            pygame.draw.circle(self.screen, self.circle_selected_color, (self.board.board_width + 5 + self.cricle_radius, (self.board.square_height * 6)+ 10 + self.cricle_radius), self.cricle_radius, self.circle_width)
        else:
            pygame.draw.circle(self.screen, self.circle_color, (self.board.board_width + 5 + self.cricle_radius, (self.board.square_height * 6)+ 10 + self.cricle_radius), self.cricle_radius, self.circle_width)
        self.screen.blit(pygame.transform.scale(self.edit_image, self.default_image_size), self.edit_rect)

        #Draw delete icon
        self.delete_rect.topleft = (self.board.board_width + 10 + self.board.square_width - 15, (self.board.square_height * 6)+ 10)
        if self.delete_selected:
            pygame.draw.circle(self.screen, self.circle_selected_color, (self.board.board_width + 5 + self.cricle_radius +(1*self.board.square_width-15), (self.board.square_height * 6)+ 10 + self.cricle_radius), self.cricle_radius, self.circle_width)
        else:
            pygame.draw.circle(self.screen, self.circle_color, (self.board.board_width + 5 + self.cricle_radius +(1*self.board.square_width-15), (self.board.square_height * 6)+ 10 + self.cricle_radius), self.cricle_radius, self.circle_width)
        self.screen.blit(pygame.transform.scale(self.delete_image, self.default_image_size), self.delete_rect)

        #Draw check nine
        self.check_rect.topleft = (self.board.board_width + 10 + (2*self.board.square_width-30), (self.board.square_height * 6)+ 10)
        pygame.draw.circle(self.screen, self.circle_color, (self.board.board_width + 5 + self.cricle_radius +(2*self.board.square_width)-30, (self.board.square_height * 6)+ 10 + self.cricle_radius), self.cricle_radius, self.circle_width)
        self.screen.blit(pygame.transform.scale(self.check_image, self.default_image_size), self.check_rect)


    def draw_menu(self):
        #title
        font = Font("Sudoku",self.game_heading_color, 3)
        font.number_rect.centerx = self.settings.screen_width // 2
        font.number_rect.centery = 100
        self.screen.blit(font.number_image, font.number_rect)
        #options

        #Draw difficulty   
        self.diff_bck_arrow_rect.centerx = self.settings.screen_width // 2 + 10
        self.diff_bck_arrow_rect.centery = 335
        self.diff_fwd_arrow_rect.centerx = self.settings.screen_width // 2 + 50 + 190
        self.diff_fwd_arrow_rect.centery = 335

        pygame.draw.circle(self.screen, self.box_color, (self.diff_bck_arrow_rect.centerx-5, self.diff_bck_arrow_rect.centery -5), self.cricle_radius, self.circle_width)
        pygame.draw.rect(self.screen, self.box_color, [self.settings.screen_width // 2 + 50, 300, 140, 60], 5, border_radius=15)
        pygame.draw.circle(self.screen, self.box_color, (self.diff_fwd_arrow_rect.centerx-5, self.diff_fwd_arrow_rect.centery -5), self.cricle_radius, self.circle_width)
        if self.game.difficulty == 0:
            font = Font("Easy",self.game_heading_color, 2)
        elif self.game.difficulty == 1:
            font = Font("Medium",self.game_heading_color, 2)
        elif self.game.difficulty ==2:
            font = Font("Hard",self.game_heading_color, 2)
        font.number_rect.centerx = self.settings.screen_width // 2 +55 + 60
        font.number_rect.centery = 330
        self.screen.blit(font.number_image, font.number_rect)
        self.screen.blit(pygame.transform.scale(self.diff_bck_arrow_image, self.default_image_size), self.diff_bck_arrow_rect)
        self.screen.blit(pygame.transform.scale(self.diff_fwd_arrow_image, self.default_image_size), self.diff_fwd_arrow_rect)
        font = Font("Difficultiy",self.game_heading_color, 2)
        font.number_rect.centerx = self.settings.screen_width // 2 -200
        font.number_rect.centery = 330
        self.screen.blit(font.number_image, font.number_rect)

        #Draw Game Number   
        self.no_bck_arrow_rect.centerx = self.settings.screen_width // 2 + 10
        self.no_bck_arrow_rect.centery = 435
        self.no_fwd_arrow_rect.centerx = self.settings.screen_width // 2 + 50 + 190
        self.no_fwd_arrow_rect.centery = 435

        pygame.draw.circle(self.screen, self.box_color, (self.no_bck_arrow_rect.centerx-5, self.no_bck_arrow_rect.centery -5), self.cricle_radius, self.circle_width)
        pygame.draw.rect(self.screen, self.box_color, [self.settings.screen_width // 2 + 50, 400, 140, 60], 5, border_radius=15)
        pygame.draw.circle(self.screen, self.box_color, (self.no_fwd_arrow_rect.centerx-5, self.no_fwd_arrow_rect.centery -5), self.cricle_radius, self.circle_width)
        if self.game.game_no == 0:
            font = Font("1",self.game_heading_color, 2)
        elif self.game.game_no == 1:
            font = Font("2",self.game_heading_color, 2)
        font.number_rect.centerx = self.settings.screen_width // 2 +55 + 60
        font.number_rect.centery = 430
        self.screen.blit(font.number_image, font.number_rect)
        self.screen.blit(pygame.transform.scale(self.no_bck_arrow_image, self.default_image_size), self.no_bck_arrow_rect)
        self.screen.blit(pygame.transform.scale(self.no_fwd_arrow_image, self.default_image_size), self.no_fwd_arrow_rect)
        font = Font("Game No",self.game_heading_color, 2)
        font.number_rect.centerx = self.settings.screen_width // 2 -200
        font.number_rect.centery = 430
        self.screen.blit(font.number_image, font.number_rect)

        #Draw start button
        pygame.draw.rect(self.screen, self.box_color, [self.settings.screen_width // 2 + 50, 500, 140, 60], 5, border_radius=15)
        self.start = Font("Start",self.game_heading_color, 2)
        self.start.number_rect.centerx = self.settings.screen_width // 2 +55 + 60
        self.start.number_rect.centery = 530
        self.screen.blit(self.start.number_image, self.start.number_rect)