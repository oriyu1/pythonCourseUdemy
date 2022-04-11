'''
To keep the code readble, 
we sould'nt define classes inside our main file.
To be able to import classes from a directory
we need to add empty file with the name "__init__.py
'''

# A realtive import:
from classes.enemy import Enemy


enemy = Enemy(200, 60)
print("HP:", enemy.get_hp())