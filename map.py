import constantV
import pygame
import sys

class map:
    def __init__(self):
        self.map = [[0 for _ in range(constantV.SNAKEMAPWIDTH)] for _ in range(constantV.SNAKEMAPHEIGHT)]

    def drawMap(self, screen):
        for i in range(constantV.SCREENHEIGHT):
            for j in range(constantV.SCREENWIDTH):
                DrawColor = (0,0,0)
                if(self.map([i][j] == 1)):
                    DrawColor = (0,255,0)

                
                pygame.draw.rect(screen, DrawColor, (j*constantV.SNAKEWIDTH, i*constantV.SNAKEHEIGHT, constantV.SNAKEWIDTH, constantV.SNAKEHEIGHT))
