import pygame
pygame.init()

class Battle():
    def __init__(self):
        pass
    beginBattlePhase = False
    battle = False

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
        
    def drawBattleMainText(self, screen, color, font):
        attack = font.render('Attack', True, color)
        renderAttack = screen.blit(attack, [130, 360])

        items = font.render('Items', True, color)
        renderItems = screen.blit(items, [130, 410])

        flee = font.render('Flee', True, color)
        renderFlee = screen.blit(items, [400, 360])
