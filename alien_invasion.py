import sys
import pygame
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200,500))
        pygame.display.set_caption("Alien Invasion")
        #设置背景色
        self.bg_color = (139,34,139)
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                self.screen.fill(self.bg_color)
            pygame.display.flip()
            """刷新"""
            self.clock.tick(60)
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
