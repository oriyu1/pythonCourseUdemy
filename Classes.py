import random


# Class variables and instance variables
class Enemy:
    hp = 200  # This is class variable

    def __init__(self, atkl, atkh):
        # These are instance variables
        self.atkl = atkl
        self.atkh = atkh


    def getAtk(self):
        print("atk is", self.atkl)

    def getHp(self):
        print("Hp is", self.hp)


enemy1 = Enemy(40, 49)
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(75, 90)
enemy2.getAtk()
enemy2.getHp()

'''
playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30: # setting minimum value of points
        playerhp = 30

    print("Enemy strikes for", dmg, "points of damage. Current hp is", playerhp)

    if playerhp > 30:
        continue # it will jump from here to the begining of the loop
        # pass # if you want empty "if" statement you can write "pass". Otherwise, it will be an error.

    print("You have low health. You've been teleported to the nearest inn.")
    break
'''