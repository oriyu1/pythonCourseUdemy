import random


class Enemy:   # classes good if we want to create more than one of the same (or almost same) object/instance
    atkl = 60
    atkh = 80

    def getAtk(self):     # self if - this instance of the object
        print(self.atkl)  # atkl is not variable of the function so we need self

# getAtk() # This won't work because it does'nt exit in the global scope

enemy1 = Enemy()
enemy1.getAtk()

enemy2 = Enemy()
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