
import pygame
pygame.init()

class Rooms():
    def __init__(self):
        self.x = 0
    #Room 0: House
    def drawHouse(self, screen, color):
        return pygame.draw.rect(screen, color, [100,100, 250, 100], 2)
    #Room 1: Cave

    #Room 2: Cave Hallway

    #Room 3: Mansion

    #Room 4: Bedroom 1

    #Room 5: Bedroom 2

    #Room 6: Mansion Hallway 1

    #Room 7: Mansion Hallway 2

    #Room 8: Washing Room

    #Room 9: Library

    #Room 10: End
