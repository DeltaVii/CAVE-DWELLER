
import pygame
pygame.init()

class Rooms():
    def __init__(self):
        self.x = 0
    def drawHouse(self, screen, color):
        return pygame.draw.rect(screen, color, [100,100, 250, 100], 2)
