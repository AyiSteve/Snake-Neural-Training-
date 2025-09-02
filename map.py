import constantV
import pygame
import sys
import snake

class map:
    def __init__(self):
        self.map = [[0 for _ in range(constantV.SNAKEMAPWIDTH)] for _ in range(constantV.SNAKEMAPHEIGHT)]

    def drawMap(self,screen, deque, apple):
        #Reset map
        self.map = [[0 for _ in range(constantV.SNAKEMAPWIDTH)] for _ in range(constantV.SNAKEMAPHEIGHT)]
        
        #Set up the apple in map
        AppleLocationX, AppleLocationY = constantV.v2t(apple)
        self.map[AppleLocationY][AppleLocationX] = 2

        #Set up the snake in map
        for block in deque:
            x,y = constantV.v2t(block)
            self.map[y][x] = 1


        #Draw map
        for i in range(constantV.SNAKEMAPHEIGHT):
            for j in range(constantV.SNAKEMAPWIDTH):
                DrawColor = (0,0,0)
                if self.map[i][j] == 1:
                    DrawColor = (0,255,0)
                if self.map[i][j] == 2:
                    DrawColor = (255,0,0)
                pygame.draw.rect(screen, DrawColor, (j*constantV.SNAKEWIDTH, i*constantV.SNAKEHEIGHT, constantV.SNAKEWIDTH, constantV.SNAKEHEIGHT))

    def winLostCondition(self, deque, direction):
        head = deque[0]
        nextMovex, nextMovey = constantV.v2t(head+direction)
        if not ((nextMovex <= constantV.SNAKEMAPWIDTH - 1) and (nextMovex >= 0) and (nextMovey <= constantV.SNAKEMAPHEIGHT - 1) and (nextMovey >= 0)): 
            return False
        if (self.map[nextMovex][nextMovey] == 1):
            return False
        return True