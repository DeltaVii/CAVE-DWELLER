####################
## Kelly Norris
##
## April 2016 Semester 2
##
## CAVE DWELLER Player Class
####################

class Player():
    hp = 20
    xp = 0
    items = []
    items.append('Wooden Sword')
    items.append('Healing Potion')
    items.append('Healing Potion')
    items.append('')
    equip = items[0]

class Enemy():
    def __init__(self):
        pass
    name = ''
    hp = 5
    attacks = []
    attack1 = []
    attack2 = []

    def statgen(self, hp, attack1, attack2):
        self.hp = hp
        self.attacks.append(attack1)
        self.attacks.append(attack2)
        
