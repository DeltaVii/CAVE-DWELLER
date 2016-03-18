####################
## Kelly Norris
##
## March 2016 Semester 2
##
## CAVE DWELLER Main File
####################

#Import files as needed
import pygame
#import basegame
import basegame
#import rooms
from Rooms import *
from Menu import *
#Declare colors for draws
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

#initialize pygame
pygame.init()
font = pygame.font.SysFont('adobehebrew', 12)

#Create window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Window Title goes here")

#importing classes
rooms = Rooms()
menu = Menu()

#making main loop variables:
#done for loop
done = False
#clock for screen updates
clock = pygame.time.Clock()

#Other variables for looping:
font = pygame.font.Font('AdobeArabic-Regular.otf', 50)
cursor_position = 'menu'
#-----Main Loop-----#
while not done:
    #Event loop, looking for inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User asked to quit")
            done = True
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key")
            if cursor_position == 'menu':
                if event.key == pygame.K_DOWN:
                    cursor_position = 'move'
                if event.key == pygame.K_RIGHT:
                    cursor_position = 'interact'
            if cursor_position == 'move':
                if event.key == pygame.K_UP:
                    cursor_position = 'menu'
            if cursor_position == 'interact':
                if event.key == pygame.K_LEFT:
                    cursor_position = 'menu'
        elif event.type == pygame.KEYUP:
            print("User let go of a key")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
    #Game logic goes here
    
    #clear screen
    screen.fill(BLACK)

    #Draws go here
    
    
    menu.drawMenuBox(screen, WHITE)
    menu.drawMenuText(screen, font, WHITE)
    #if cursor_position == 'menu':
        #menu.drawMenuCursor(screen, WHITE, 130,130,140,375,395,385)
    #if cursor_position == 'move':
        #menu.drawMenuCursor(screen, WHITE, 130,130,140,425,445,435)
    #if cursor_position == 'interact':
        #menu.drawMenuCursor(screen, WHITE, 400,400,410,375,395,385)
    menu.drawMenuCursorSimple(screen, WHITE)
    if basegame.current_room == 0:
        rooms.drawHouse(screen, WHITE)
        menu.drawRoom0Text(screen, font, WHITE)
    
    #Make sure draws go on screen
    pygame.display.flip()

    #set frames per second
    clock.tick(60)
#when loop is done, close window
pygame.quit()

