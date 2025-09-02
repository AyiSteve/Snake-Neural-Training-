from pygame.math import Vector2

NUMBEROFMODEL = 1
SCREENWIDTH = 400
SCREENHEIGHT = 400
SNAKEWIDTH = 20
SNAKEHEIGHT = 20
SNAKEMAPWIDTH = (int)(SCREENWIDTH/SNAKEWIDTH)
SNAKEMAPHEIGHT = (int)(SCREENHEIGHT/SNAKEHEIGHT)

# As I initial them it'll be float and just wanted to make it as integer
def v2t(v: Vector2):
    return (int(v.x), int(v.y))
