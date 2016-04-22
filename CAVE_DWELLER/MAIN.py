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
from Player import *
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
player = Player()
#making main loop variables:
#done for loop
done = False
#clock for screen updates
clock = pygame.time.Clock()

#Other variables for looping:
font = pygame.font.Font('AdobeArabic-Regular.otf', 50)
roomFont = pygame.font.Font('AdobeArabic-Regular.otf', 30)
cursor_position = 'topLeft'
current_menu = "main"
text = True
#Locks
lock1 = True
lock2 = True
key1 = False
key2 = False
#First Visit checks
room0_first = True
room2_first = True
room8_first = True
room9_first = True
#Room images
roomimage_list = []
roomimage0 = pygame.image.load("img/room0.png").convert()
roomimage_list.append(roomimage0)
roomimage1 = pygame.image.load("img/room1.png").convert()
roomimage_list.append(roomimage1)
roomimage2 = pygame.image.load("img/room2.png").convert()
roomimage_list.append(roomimage2)
roomimage3 = pygame.image.load("img/room3.png").convert()
roomimage_list.append(roomimage3)
roomimage4 = pygame.image.load("img/room4.png").convert()
roomimage_list.append(roomimage4)
roomimage5 = pygame.image.load("img/room5.png").convert()
roomimage_list.append(roomimage5)
roomimage6 = pygame.image.load("img/room6.png").convert()
roomimage_list.append(roomimage6)
roomimage7 = pygame.image.load("img/room7.png").convert()
roomimage_list.append(roomimage7)
roomimage8 = pygame.image.load("img/room8.png").convert()
roomimage_list.append(roomimage8)
roomimage9 = pygame.image.load("img/room9.png").convert()
roomimage_list.append(roomimage9)
roomimage10 = pygame.image.load("img/room10.png").convert()
roomimage_list.append(roomimage10)
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
                    if event.key == pygame.K_RETURN:
                        current_menu = 'player'
                        print("The current menu is player")
                        cursor_position = 'topLeft'
                        
                if cursor_position == 'botLeft':
                    if event.key == pygame.K_UP:
                        cursor_position = 'topLeft'
                    if event.key == pygame.K_RETURN:
                        current_menu = 'move'
                        
                if cursor_position == 'topRight':
                    if event.key == pygame.K_LEFT:
                        cursor_position = 'topLeft'
                    if event.key == pygame.K_RETURN:
                        interact = True
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
            #Player menu
            if current_menu == 'player':
                if event.key == pygame.K_BACKSPACE:
                    current_menu = 'main'
                if cursor_position == 'topLeft':
                    if event.key == pygame.K_RIGHT:
                        cursor_position = 'topRight'
                    if event.key == pygame.K_RETURN:
                        current_menu = 'items'
                        print("The current menu is items")
                if cursor_position == 'topRight':
                    if event.key == pygame.K_LEFT:
                        cursor_position = 'topLeft'
                    if event.key == pygame.K_RETURN:
                        current_menu = 'stats'

            if current_menu == 'items':
                if event.key == pygame.K_BACKSPACE:
                    current_menu = 'player'
            
            if current_menu == 'stats':
                if event.key == pygame.K_BACKSPACE:
                    current_menu = 'player'
                
           
            if event.key == pygame.K_z:
                rooms.text = False
                print("text is false")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
    #Game logic goes here
    rooms.checkDirection()
    rooms.setDirection()
    ##Checking for locked doors and their keys##
    if rooms.current_room == 3 and lock1 == True and key1 == True:
        lock1 = False
        menu.drawEventBox(screen)
    
    #clear screen
    screen.fill(BLACK)

    #Draws go here
    screen.blit(roomimage_list[rooms.current_room], [0, 0])

    if rooms.text == True:
        menu.drawTextBox(screen, WHITE)
        menu.drawRoomText(screen, roomFont, WHITE, rooms.current_room)
        
        
        

    pygame.draw.rect(screen, BLACK, [50, 350, 600, 125], 0)
    menu.drawMenuBox(screen, WHITE)
    if current_menu == 'main':
        menu.drawMenuText(screen, font, WHITE)
    elif current_menu == 'move':
        menu.drawMoveMenuText(screen, font, WHITE)
    elif current_menu == 'player':
        menu.drawPlayerMenuText(screen, font, WHITE)
    elif current_menu == 'items':
        menu.drawItemsPlayerMenuText(screen, font, WHITE)
    
    menu.drawMenuCursorSimple(cursor_position, screen, WHITE)
    
    
    #Make sure draws go on screen
    pygame.display.flip()

    #set frames per second
    clock.tick(60)
#when loop is done, close window
pygame.quit()

