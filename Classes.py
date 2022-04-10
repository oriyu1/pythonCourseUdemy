import random


class Enemy:
    
    # This code runs when the class is been innitiation or instaciated
    # It helps us make it more dydamic so we can send arguments into the class
    # and that helps us for example initiate to instances of this class with the same
    # objects with different properties
    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh



    def getAtk(self):
        print(self.atkl)


enemy1 = Enemy(40, 49)
enemy1.getAtk()

enemy2 = Enemy(75, 90)
enemy2.getAtk()


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