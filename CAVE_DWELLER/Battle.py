import pygame
from Player import *
player = Player()
enemy = Enemy()
pygame.init()

class Battle():
    def __init__(self):
        pass
    beginBattlePhase = False
    battle = False
    flee = False
    attack = False
    turn = 'player'

    def beginBattle(self, screen, color, font):
        BLACK = [0,0,0]
        pygame.draw.rect(screen, BLACK, [0,0,700,500], 0)
        pygame.draw.rect(screen, color, [200, 100, 300, 250], 2)
        pygame.draw.polygon(screen, color, [[330, 225],[355, 225],[355,250],[330,250]], 0)
        pygame.draw.polygon(screen, color, [[330, 200],[355,200],[355, 110],[330,110]], 0)
        text = font.render('An enemy appears!', True, color)
        renderText = screen.blit(text, [209, 250])

    def drawBattleBox(self, screen, color):
        pygame.draw.rect(screen, color, [50, 350, 600, 125], 3)

    def drawStats(self, screen, font, color):
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
        
    def drawBattleMainText(self, screen, color, font):
        attack = font.render('Attack', True, color)
        renderAttack = screen.blit(attack, [130, 360])

        items = font.render('Items', True, color)
        renderItems = screen.blit(items, [130, 410])

        flee = font.render('Flee', True, color)
        renderFlee = screen.blit(flee, [400, 360])

    def drawBattleItemText(self, screen, color, font):
        item1 = font.render(player.items[1], True, color)
        item2 = font.render(player.items[2], True, color)
        item3 = font.render(player.items[3], True, color)

        renderItem1 = screen.blit(item1, [130,360])
        renderItem2 = screen.blit(item2, [130,410])
        renderItem3 = screen.blit(item3, [400,360])



        
