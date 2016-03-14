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

rooms = Rooms()
menu = Menu()

#making main loop variables:
#done for loop
done = False
#clock for screen updates
clock = pygame.time.Clock()

#Other variables for looping:

#-----Main Loop-----#
while not done:
    #Event loop, looking for inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User asked to quit")
            done = True
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key")
        elif event.type == pygame.KEYUP:
            print("User let go of a key")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
    #Game logic goes here

    #clear screen
    screen.fill(BLACK)

    #Draws go here
    
    menu.drawMenuBox(screen, WHITE)
    if basegame.current_room == 0:
        rooms.drawHouse(screen, WHITE)
        #menu.drawRoom0Text(

    #Make sure draws go on screen
    pygame.display.flip()

    #set frames per second
    clock.tick(60)
#when loop is done, close window
pygame.quit()

