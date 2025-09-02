import random
import constantV
from pygame.math import Vector2

class apple:
    def refresh(self, map):
        tempx, tempy = constantV.v2t(Vector2(random.randint(1,constantV.SNAKEMAPWIDTH-2), random.randint(1,constantV.SNAKEMAPHEIGHT-2)))
        if not (map[tempx][tempy] == 0):
            self.refresh(map)
        else:
            self.apple = Vector2(tempx, tempy)
            return
    