import pygame
import basegame
from Rooms import *
rooms = Rooms()

pygame.init()


class Menu():
    def __init__(self):
        pass

    
    def drawMenuBox(self,screen,color):
        return pygame.draw.rect(screen, color, [50, 350, 600, 125], 3)

    def drawMenuText(self, screen, font, color):
        menu = font.render('Menu', True, color)
        interact = font.render('Interact', True, color)
        move = font.render('Move', True, color)
        renderMenu = screen.blit(menu, [150, 360])
        renderInteract = screen.blit(interact, [420, 360])
        renderMove = screen.blit(move, [150, 410])
        return (renderMenu, renderInteract, renderMove)

    def drawMoveMenuText(self, screen, font, color):
        north = font.render('North', True, color)
        east = font.render('East', True, color)
        south = font.render('South', True, color)
        west= font.render('West', True, color)
        renderNorth = screen.blit(north, [150, 360])
        renderEast = screen.blit(east, [420, 360])
        renderSouth = screen.blit(south, [150, 410])
        renderWest = screen.blit(west, [420, 410])
        return (renderNorth, renderEast, renderSouth, renderWest)
        

    '''
        def drawMenuCursor(self, screen, color, x1, x2, x3, y1, y2, y3):
        cursor = pygame.draw.polygon(screen, color, [[x1,y1],[x2,y2],[x3,y3]], 0)
        return cursor
    '''
    
    def drawMenuCursorSimple(self, cursor_position, screen, color):
        if cursor_position == 'topLeft':
            #draw = drawMenuCursor(screen, WHITE, 130,130,140,375,395,385)
            return pygame.draw.polygon(screen, color, [[130,375],[130,395],[140,385]], 0)
        if cursor_position == 'botLeft':
            #menu.drawMenuCursor(screen, WHITE, 130,130,140,425,445,435)
            return pygame.draw.polygon(screen, color, [[130,425],[130,445],[140,435]], 0)
        if cursor_position == 'topRight':
            #menu.drawMenuCursor(screen, WHITE, 400,400,410,375,395,385)
            return pygame.draw.polygon(screen, color, [[400,375],[400,395],[410,385]], 0)
        if cursor_position == 'botRight':
            return pygame.draw.polygon(screen, color, [[400,425],[400,445],[410,435]], 0)
        
    def drawRoom0Text(self, screen, font, color):
        text = font.render('Room 0: House', True, color)
        render1 = screen.blit(text, [200,300])
        render2 = screen.blit(text, [200,310])
        return (render1, render2)

    def drawRoomText(self, screen, font, color, current_room):
        text = font.render(rooms.roomTextList[current_room], True, color)



        
