import constantV
import pygame
import sys
import collections
import random
from pygame.math import Vector2

#Variabe:
#body----body of snake
#body_set-----store all position of body purpose is for faster in search

class snake:
    def __init__(self):
        #Initial Variable
        self.body = collections.deque()
        self.direction = Vector2(1,0)
        ###Create Body

        #Block one
        randomHead = Vector2(random.randint(1,constantV.SNAKEMAPWIDTH-2), random.randint(1,constantV.SNAKEMAPHEIGHT-2))
        self.body.append(randomHead)
        
        #Block Two
        randomBody1 = randomPattern(randomHead)
        self.body.append(randomBody1)

        #Block Three
        randomBody2 = randomPattern(randomBody1)
        self.body.append(randomBody2)

    def control(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.direction != Vector2(0, 1):
                self.direction = Vector2(0, -1)
                return 0
            elif event.key == pygame.K_DOWN and self.direction != Vector2(0, -1):
                self.direction = Vector2(0, 1)
                return 0
            elif event.key == pygame.K_LEFT and self.direction != Vector2(1, 0):
                self.direction = Vector2(-1, 0)
                return 0
            elif event.key == pygame.K_RIGHT and self.direction != Vector2(-1, 0):
                self.direction = Vector2(1, 0)
                return 0
            return 1

    def update(self, apple):
        appleEaten = True
        head = self.body[0]
        print(apple)
        print(head)
        print('\n')
        if not head == apple:
            self.body.pop()
            appleEaten = False

        self.body.appendleft(head+self.direction)
        return appleEaten
        

def randomPattern(Leading):
    pattern = [Vector2(Leading.x,Leading.y-1),Vector2(Leading.x,Leading.y+1),Vector2(Leading.x-1,Leading.y), Vector2(Leading.x+1,Leading.y)]
    return random.choice(pattern)