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

    if playerhp == 30:
        #print("You have died. You cannot respawn, as you are dead.")
        print("You have low health. You've been teleported to the nearest inn.")
        break

