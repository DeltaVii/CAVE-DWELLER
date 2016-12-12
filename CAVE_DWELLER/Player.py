####################
## Kelly Norris
##
## December 2016 Semester 2
##
## CAVE DWELLER EX Player Class
####################

#start player class
class Player():
    #nothing for init
    def __init__(self):
        pass
    #creating vars
    hp = 20
    xp = 0
    items = []
    items.append('Wooden Sword')
    items.append('Healing Potion')
    items.append('Healing Potion')
    items.append('')
    equip = items[0]

#start enemy class
class Enemy():
    #nothing for init
    def __init__(self):
        pass
    #creating vars
    name = ''
    hp = 5
    attacks = []
    attack1 = []
    attack2 = []

    #run with each encounter for new stats
    def statgen(self, hp, attack1, attack2):
        self.hp = hp
        self.attacks.append(attack1)
        self.attacks.append(attack2)
        
