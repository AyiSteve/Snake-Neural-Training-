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
        #Initial Variable
        self.body = collections.deque()
        self.body_set = set()
        self.direction = pygame.math.Vector2(1,1)
        ###Create Body

        #Block one
        randomHead = pygame.math.Vector2(random.randint(1,constantV.SNAKEMAPWIDTH-2), random.randint(1,constantV.SNAKEMAPHEIGHT-2))
        self.body.append(randomHead)
        self.body_set.add(randomHead)
        
        #Block Two
        randomBody1 = randomPattern(randomHead)
        self.body.append(randomBody1)
        self.body_set.add(randomBody1)

        #Block Three
        randomBody2 = randomPattern(randomBody1)
        self.body.append(randomBody2)
        self.body_set.add(randomBody2)

    def update(self):
        head = self.body[0]
        self.body.pop()
        self.body.appendleft(head+self.direction)
        
def randomPattern(Leading):
    pattern = [pygame.math.Vector2(Leading.x-1,Leading.y-1),pygame.math.Vector2(Leading.x+1,Leading.y-1),pygame.math.Vector2(Leading.x-1,Leading.y+1),pygame.math.Vector2(Leading.x+1,Leading.y+1)]
    return random.choice(pattern)