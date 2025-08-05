import sys
import pygame
import constantV


#Class that hold the main cases and controlling usage of function
class snake:

    def __init__(self):
        #Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((constantV.SCREENWIDTH,constantV.SCREENHEIGHT))
        pygame.display.set_caption("SNAKE")
        self.clock = pygame.time.Clock()

        #Set Up display
    def main(self):
        running = True
        while running:
            self.screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


if __name__=="__main__":
    app = snake()
    app.main()