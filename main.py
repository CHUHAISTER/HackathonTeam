import os
import pygame


class Sprite:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Player(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y)
        pass

    def move(self):
        pass

    def collision(self):
        pass


class Mob(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y)
        pass

    def behaviour(self):
        pass


class Tile(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y)
        pass


def mainloop():
    while True:
        clock.tick(60)
        window.update()
        mainloop()


pygame.init()
clock = pygame.time.Clock()

window = pygame.display
#window_width = window.Info().current_w
#window_height = window.Info().current_h
screenSurface = window.set_mode(size=(1080, 768), depth=32)
window.set_caption('Game')

mainloop()

