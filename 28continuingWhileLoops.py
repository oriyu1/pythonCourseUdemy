import random


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

