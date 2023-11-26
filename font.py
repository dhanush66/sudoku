import pygame

class Font:
    def __init__(self, number, color, Type=False):
        self.number = str(number)
        self.text_color = color
        if Type == 1:
            self.font = pygame.font.SysFont(None, 28)
        elif Type == 2:
            self.font = pygame.font.SysFont(None, 34)
        elif Type == 3:
            self.font = pygame.font.SysFont(None, 100)
        self.number_image = self.font.render(self.number, True, self.text_color)
        self.number_rect = self.number_image.get_rect()

