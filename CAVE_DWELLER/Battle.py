####################
## Kelly Norris
##
## June 2016 Semester 2
##
## CAVE DWELLER Battle file
####################

import pygame
import random
from Player import *


pygame.init()

class Battle():
    def __init__(self):
        pass
    #needed variables
    beginBattlePhase = False
    endBattlePhase = False
    battle = False
    flee = False
    attack = False
    turn = 'player'
    event_text1 = ''
    event_text2 = ''
    battleEvent = ''
    enemy = 0

    #Begin Battle image
    def beginBattle(self, screen, color, font):
        BLACK = [0,0,0]
        pygame.draw.rect(screen, BLACK, [0,0,700,500], 0)
        pygame.draw.rect(screen, color, [245, 80, 200, 250], 2)
        pygame.draw.polygon(screen, color, [[330, 225],[355, 225],[355,250],[330,250]], 0)
        pygame.draw.polygon(screen, color, [[330, 200],[355,200],[355, 110],[330,110]], 0)
        text = font.render('BATTLE!', True, color)
        renderText = screen.blit(text, [275, 250])

    def endBattle(self, screen, color, font):
        BLACK = [0,0,0]
        pygame.draw.rect(screen, BLACK, [0,0,700,500], 0)
        pygame.draw.rect(screen, color, [200, 175, 300, 100], 2)
        text = font.render('Enemy Defeated!', True, color)
        renderText = screen.blit(text, [225, 200])
        

    #Battle menu box
    def drawBattleBox(self, screen, color):
        pygame.draw.rect(screen, color, [50, 350, 600, 125], 3)

    #Stat draws
    def drawStats(self, screen, font, color, enemy, player):
        pygame.draw.rect(screen, color, [50, 320, 100, 25], 2)
        playerhpequals = font.render('HP = ', True, color)
        playerhp = font.render(str(player.hp), True, color)
        renderPlayerhpequals = screen.blit(playerhpequals, [55, 318])
        renderPlayerhp = screen.blit(playerhp, [110, 318])

        pygame.draw.rect(screen, color, [50, 50, 100, 25], 2)
        enemyName = font.render('Enemy', True, color)
        enemyhpequals = font.render('HP = ', True, color)
        enemyhp = font.render(str(enemy.hp), True, color)
        
        renderEnemyName = screen.blit(enemyName, [55, 20])
        renderEnemyhpequals = screen.blit(enemyhpequals, [55, 48])
        renderEnemyhp = screen.blit(enemyhp, [110, 48])

    #Text for main battle menu
    def drawBattleMainText(self, screen, color, font):
        attack = font.render('Attack', True, color)
        renderAttack = screen.blit(attack, [130, 360])

        items = font.render('Items', True, color)
        renderItems = screen.blit(items, [130, 410])

        flee = font.render('Flee', True, color)
        renderFlee = screen.blit(flee, [400, 360])

    #battle>Item text
    def drawBattleItemText(self, screen, color, font, player):
        item1 = font.render(player.items[1], True, color)
        item2 = font.render(player.items[2], True, color)
        item3 = font.render(player.items[3], True, color)

        renderItem1 = screen.blit(item1, [130,360])
        renderItem2 = screen.blit(item2, [130,410])
        renderItem3 = screen.blit(item3, [400,360])

    def drawBattleEventText(self, screen, color, font):
        BLACK = [0, 0, 0]
        pygame.draw.rect(screen, BLACK, [100, 200, 500, 100], 0)
        pygame.draw.rect(screen, color, [100, 200, 500, 100], 3)
        text1 = font.render(self.event_text1, True, color)
        text2 = font.render(self.event_text2, True, color)

        renderText1 = screen.blit(text1, [130, 220])
        renderText2 = screen.blit(text2, [130, 240])

    def rollPlayerAttack(self, equip, enemy):
        if equip == 'Wooden Sword':
            dmg = random.randint(2, 5)
            enemy.hp -= dmg
            print('enemy health is',enemy.hp)
            self.attack = False
            self.event_text1 = "Your attack's damage was "
            self.event_text2 = str(dmg)
            self.battleEvent = 'player_attack'

    def drawEnemy(self, screen):
        if self.enemy == 1:
            image = pygame.image.load("img/enemy1.png").convert()
            screen.blit(image, [350, 100])
        if self.enemy == 2:
            image = pygame.image.load("img/enemy2.png").convert()
            screen.blit(image, [350, 100])
        if self.enemy == 3:
            image = pygame.image.load("img/enemy3.png").convert()
            screen.blit(image, [350, 100])


        
