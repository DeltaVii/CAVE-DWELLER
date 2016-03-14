import pygame
pygame.init()

class Menu():
    def __init__(self):
        self.x = 0

    def drawMenuBox(self,screen,color):
        return pygame.draw.rect(screen, color, [100, 350, 500, 125], 3)
