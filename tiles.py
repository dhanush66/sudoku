import pygame


class Tiles:
    def __init__(self,number):
        self.number = number
        self.editable = None
        self.possible = set()
