import pygame

class Font:
    def __init__(self, number, color, Type=False):
        self.number = str(number)
        self.text_color = color
        if Type == 1:
            self.font = pygame.font.SysFont(None, 32)
        elif Type == 2:
            self.font = pygame.font.SysFont(None, 48)
        elif Type == 3:
            self.font = pygame.font.SysFont('Lavanderia Sturdy', 100)
        self.number_image = self.font.render(self.number, True, self.text_color)
        self.number_rect = self.number_image.get_rect()

