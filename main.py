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
        events = pygame.event.get()
        binds(events)
        window.update()
        mainloop()


def binds(events):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


pygame.init()
clock = pygame.time.Clock()

window = pygame.display
#window_width = window.Info().current_w
#window_height = window.Info().current_h

bg_test = pygame.image.load("Art/bg.png")

screen_surface = window.set_mode(size=(1024, 768), depth=32)
screen_surface.blit(bg_test, [0, 0])
window.set_caption('Game')

mainloop()

