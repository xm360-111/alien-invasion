import sys
import pygame
from settings import Settings
from ship import Ship
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.setting = Settings()
        self.screen = pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                self.screen.fill(self.setting.bg_color)
                self.ship.blitme()
            pygame.display.flip()
            """刷新"""
            self.clock.tick(60)
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
