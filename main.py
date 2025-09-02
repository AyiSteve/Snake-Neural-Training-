import sys
import pygame
import constantV
from snake import snake
from map import map as Map
from apple import apple as Apple

class App:
    def __init__(self):
        pygame.init()

        # Resolve screen size (supports tiling via NUMBEROFMODEL if you need it)
        self.screen_w = constantV.SCREENWIDTH * getattr(constantV, "NUMBEROFMODEL", 1)
        self.screen_h = constantV.SCREENHEIGHT * getattr(constantV, "NUMBEROFMODEL", 1)
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))
        pygame.display.set_caption("SNAKE")
        self.clock = pygame.time.Clock()

        # Fonts/UI
        self.font_big = pygame.font.SysFont(None, 64)
        self.font = pygame.font.SysFont(None, 36)

        # Buttons (centered)
        w, h = 220, 60
        cx, cy = self.screen_w // 2, self.screen_h // 2
        self.btn_restart = pygame.Rect(0, 0, w, h); self.btn_restart.center = (cx, cy - 40)
        self.btn_exit    = pygame.Rect(0, 0, w, h); self.btn_exit.center    = (cx, cy + 40)

        # Game state
        self.state = "PLAYING"   # PLAYING | PAUSED | GAMEOVER
        self._start_new_game()

    def _start_new_game(self):
        """Create/Reset all game objects."""
        self.player = snake()
        self.matrix = Map()
        self.app = Apple()
        self.app.refresh(self.matrix.map)   # spawn first apple

    def run(self):
        while True:
            if self.state == "PLAYING":
                self.loop_playing()
            elif self.state == "PAUSED":
                self.loop_paused()
            elif self.state == "GAMEOVER":
                self.loop_gameover()
            else:
                pygame.quit(); sys.exit()

    # -------------------- STATE LOOPS --------------------

    def loop_playing(self):
        clk = 1
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_p, pygame.K_ESCAPE):
                    self.state = "PAUSED"
                # pass controls to snake and one key at a time
                else:
                    if clk:
                        clk = self.player.control(event)
                
        # Win/Lose condition (assumes it returns bool: True if still alive)
        alive = self.matrix.winLostCondition(self.player.body, self.player.direction)

        # Update snake (assumes snake.update(apple_pos) -> bool eaten)
        try:
            apple_eaten = self.player.update(self.app.apple)
        except RuntimeError:
            self.state = "GAMEOVER"
            apple_eaten = False
     
        if apple_eaten:
            self.app.refresh(self.matrix.map)

        # Draw world
        self.screen.fill((0, 0, 0))

        if not alive:
            self.state = "GAMEOVER"
            return
        #Draw Map
        self.matrix.drawMap(self.screen, self.player.body, self.app.apple)



        # HUD
        self._blit_text("Press P/Esc to Pause", (10, 10), self.font, (200, 200, 200))
 
        pygame.display.flip()
        self.clock.tick(6)   # game speed
    def loop_paused(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_p, pygame.K_ESCAPE):
                    self.state = "PLAYING"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.btn_restart.collidepoint(event.pos):
                    self._start_new_game()
                    self.state = "PLAYING"
                elif self.btn_exit.collidepoint(event.pos):
                    pygame.quit(); sys.exit()

        # Dim overlay
        overlay = pygame.Surface((self.screen_w, self.screen_h), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        self.screen.blit(overlay, (0, 0))

        self._blit_center("PAUSED", self.font_big, (255, 255, 255), y=self.screen_h // 2 - 120)
        self._draw_button(self.btn_restart, "Restart")
        self._draw_button(self.btn_exit, "Exit")

        pygame.display.flip()
        self.clock.tick(60)

    def loop_gameover(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.btn_restart.collidepoint(event.pos):
                    self._start_new_game()
                    self.state = "PLAYING"
                elif self.btn_exit.collidepoint(event.pos):
                    pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self._start_new_game(); self.state = "PLAYING"
                elif event.key == pygame.K_q:
                    pygame.quit(); sys.exit()

        self.screen.fill((20, 20, 20))
        self._blit_center("GAME OVER", self.font_big, (255, 80, 80), y=self.screen_h // 2 - 120)
        self._draw_button(self.btn_restart, "Restart (R)")
        self._draw_button(self.btn_exit, "Exit (Q)")
        pygame.display.flip()
        self.clock.tick(60)

    # -------------------- UI HELPERS --------------------

    def _draw_button(self, rect: pygame.Rect, label: str):
        mouse_over = rect.collidepoint(pygame.mouse.get_pos())
        bg = (80, 80, 80) if not mouse_over else (110, 110, 110)
        pygame.draw.rect(self.screen, bg, rect, border_radius=12)
        pygame.draw.rect(self.screen, (220, 220, 220), rect, width=2, border_radius=12)
        self._blit_center(label, self.font, (255, 255, 255), center=rect.center)

    def _blit_text(self, text, pos, font, color):
        surf = font.render(text, True, color)
        self.screen.blit(surf, pos)

    def _blit_center(self, text, font, color, center=None, y=None):
        surf = font.render(text, True, color)
        rect = surf.get_rect()
        if center is not None:
            rect.center = center
        elif y is not None:
            rect.centerx = self.screen_w // 2
            rect.centery = y
        else:
            rect.center = (self.screen_w // 2, self.screen_h // 2)
        self.screen.blit(surf, rect)

if __name__ == "__main__":
    App().run()
