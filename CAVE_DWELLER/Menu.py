import pygame
import basegame
from Rooms import *
from Player import *
rooms = Rooms()
player = Player()
pygame.init()

#create class
class Menu():
    def __init__(self):
        pass

    #draw the box for the menu
    def drawMenuBox(self,screen,color):
        return pygame.draw.rect(screen, color, [50, 350, 600, 125], 3)

    def drawTextBox(self, screen, color):
        BLACK = (0, 0, 0)
        return (pygame.draw.rect(screen, BLACK, [50, 50, 600, 125], 0),
                pygame.draw.rect(screen, color, [50, 50, 600, 125], 3))

    #Text draws for different menus
    def drawMenuText(self, screen, font, color):
        menu = font.render('Menu', True, color)
        interact = font.render('Interact', True, color)
        move = font.render('Move', True, color)
        
        renderMenu = screen.blit(menu, [130, 360])
        renderInteract = screen.blit(interact, [400, 360])
        renderMove = screen.blit(move, [130, 410])
        return (renderMenu, renderInteract, renderMove)

    def drawMoveMenuText(self, screen, font, color):
        north = font.render('North', True, color)
        east = font.render('East', True, color)
        south = font.render('South', True, color)
        west= font.render('West', True, color)
        
        renderNorth = screen.blit(north, [130, 360])
        renderEast = screen.blit(east, [400, 360])
        renderSouth = screen.blit(south, [130, 410])
        renderWest = screen.blit(west, [400, 410])
        return (renderNorth, renderEast, renderSouth, renderWest)
        
    def drawPlayerMenuText(self, screen, font, color):
        items = font.render('Items', True, color)
        stats = font.render('Stats', True, color)
        renderItems = screen.blit(items, [130, 360])
        renderStats = screen.blit(stats, [400, 360])

    def drawItemsPlayerMenuText(self, screen, font, color):
        item1 = font.render(player.items[0], True, color)
        item2 = font.render(player.items[1], True, color)
        item3 = font.render(player.items[2], True, color)
        item4 = font.render(player.items[3], True, color)
        
        renderItem1 = screen.blit(item1, [130, 360])
        renderitem2 = screen.blit(item2, [400, 360])
        renderitem3 = screen.blit(item3, [130, 410])
        renderitem4 = screen.blit(item4, [400, 410])
        

    #Cursor placement    
    def drawMenuCursorSimple(self, cursor_position, screen, color):
        if cursor_position == 'topLeft':
            #draw = drawMenuCursor(screen, WHITE, 130,130,140,375,395,385)
            return pygame.draw.polygon(screen, color, [[110,375],[110,395],[120,385]], 0)
        if cursor_position == 'botLeft':
            #menu.drawMenuCursor(screen, WHITE, 130,130,140,425,445,435)
            return pygame.draw.polygon(screen, color, [[110,425],[110,445],[120,435]], 0)
        if cursor_position == 'topRight':
            #menu.drawMenuCursor(screen, WHITE, 400,400,410,375,395,385)
            return pygame.draw.polygon(screen, color, [[380,375],[380,395],[390,385]], 0)
        if cursor_position == 'botRight':
            return pygame.draw.polygon(screen, color, [[380,425],[380,445],[390,435]], 0)
        

    def drawRoomText(self, screen, font, color, current_room):
        text = font.render(rooms.room_list[rooms.current_room][0], True, color)
        renderText = screen.blit(text, [60, 60])
        return renderText



        
