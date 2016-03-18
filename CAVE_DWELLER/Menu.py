import pygame
import basegame

pygame.init()


class Menu():
    def __init__(self):
        self.x = 0

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

    def drawMenuCursor(self, screen, color, x1, x2, x3, y1, y2, y3):
        cursor = pygame.draw.polygon(screen, color, [[x1,y1],[x2,y2],[x3,y3]], 0)
        return cursor

    def drawMenuCursorSimple(self, cursor_position, screen, color):
        if cursor_position == 'menu':
            #draw = drawMenuCursor(screen, WHITE, 130,130,140,375,395,385)
            return pygame.draw.polygon(screen, color, [[130,375],[130,395],[140,385]], 0)
        if cursor_position == 'move':
            #menu.drawMenuCursor(screen, WHITE, 130,130,140,425,445,435)
            return pygame.draw.polygon(screen, color, [[130,425],[130,445],[140,435]], 0)
        if cursor_position == 'interact':
            #menu.drawMenuCursor(screen, WHITE, 400,400,410,375,395,385)
            return pygame.draw.polygon(screen, color, [[400,375],[400,395],[410,385]], 0)
            
        
    def drawRoom0Text(self, screen, font, color):
        text = font.render('Room 0: House', True, color)
        render1 = screen.blit(text, [200,300])
        render2 = screen.blit(text, [200,310])
        return (render1, render2)
