import pygame

class Font:
    def __init__(self, number):
        self.number = str(number)
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.number_image = self.font.render(self.number, True, self.text_color)
        self.number_rect = self.number_image.get_rect()