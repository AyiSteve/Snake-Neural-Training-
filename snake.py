import constantV
import pygame
import sys
import collections
import random

#Variabe:
#body----body of snake
#body_set-----store all position of body purpose is for faster in search
class snake:
    def __init__(self):
        self.body = collections.deque()
        self.body_set = set()

        #Block one
        randomHead = (random.randint(1,constantV.SNAKEMAPWIDTH-2), random.randint(1,constantV.SNAKEMAPHEIGHT-2))
        self.body.append((randomHead.x,randomHead.y))
        self.body_set.add((randomHead.x,randomHead.y))
        
        #Block Two
        random

def randomPattern(x,y):
    pattern = [(x-1,y-1),(x+1,y-1),(x-1,y+1),(x+1,y+1)]
    return random.choice(pattern)