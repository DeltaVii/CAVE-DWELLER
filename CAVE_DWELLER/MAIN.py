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
#import other files
from Rooms import *
from Menu import *
#Declare colors for draws
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

#initialize pygame
pygame.init()
#get font
font = pygame.font.SysFont('adobehebrew', 12)

#Create window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Window Title goes here")

#making instances of logic files
rooms = Rooms()
menu = Menu()

#making main loop variables:
#done for loop
done = False
#clock for screen updates
clock = pygame.time.Clock()

#Other variables for looping:
font = pygame.font.Font('AdobeArabic-Regular.otf', 50)
cursor_position = 'topLeft'
current_menu = "main"

#-----Main Loop-----#
while not done:
    #Event loop, looking for inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User asked to quit")
            done = True
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key")
            #main menu logic
            if current_menu == "main":
                if cursor_position == 'topLeft':
                    if event.key == pygame.K_DOWN:
                        cursor_position = 'botLeft'
                    if event.key == pygame.K_RIGHT:
                        cursor_position = 'topRight'
                        
                if cursor_position == 'botLeft':
                    if event.key == pygame.K_UP:
                        cursor_position = 'topLeft'
                    if event.key == pygame.K_RETURN:
                        current_menu = 'move'
                        
                if cursor_position == 'topRight':
                    if event.key == pygame.K_LEFT:
                        cursor_position = 'topLeft'
            #move menu logic
            if current_menu == 'move':
                if event.key == pygame.K_BACKSPACE:
                    current_menu = 'main'
                    cursor_position = 'topLeft'
                if cursor_position == 'topLeft':
                    if event.key == pygame.K_DOWN:
                        cursor_position = 'botLeft'
                    if event.key == pygame.K_RIGHT:
                        cursor_position = 'topRight'
                    if event.key == pygame.K_RETURN:
                        rooms.go = 'n'
                        
                if cursor_position == 'botLeft':
                    if event.key == pygame.K_UP:
                        cursor_position = 'topLeft'
                    if event.key == pygame.K_RIGHT:
                        cursor_position = 'botRight'
                    if event.key == pygame.K_RETURN:
                        rooms.go = 's'
                        
                if cursor_position == 'topRight':
                    if event.key == pygame.K_LEFT:
                        cursor_position = 'topLeft'
                    if event.key == pygame.K_DOWN:
                        cursor_position = 'botRight'
                    if event.key == pygame.K_RETURN:
                        rooms.go = 'e'
                        #print("go is now east.")
                        
                if cursor_position == 'botRight':
                    if event.key == pygame.K_UP:
                        cursor_position = 'topRight'
                    if event.key == pygame.K_LEFT:
                        cursor_position = 'botLeft'
                    if event.key == pygame.K_RETURN:
                        rooms.go = 'w'
                        print("go is now west")
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
    #Game logic goes here
    rooms.checkDirection()
    rooms.setDirection()
    '''
    if rooms.go == None:
        print("go is None")
    if rooms.next_room == None:
        print("next_room is None")
    '''
    #clear screen
    screen.fill(BLACK)

    #Draws go here
    
    
    menu.drawMenuBox(screen, WHITE)
    if current_menu == 'main':
        menu.drawMenuText(screen, font, WHITE)
    elif current_menu == 'move':
        menu.drawMoveMenuText(screen, font, WHITE)
    menu.drawMenuCursorSimple(cursor_position, screen, WHITE)
    
    if rooms.current_room == 0:
        rooms.drawHouse(screen, WHITE)
    
    #Make sure draws go on screen
    pygame.display.flip()

    #set frames per second
    clock.tick(60)
#when loop is done, close window
pygame.quit()

