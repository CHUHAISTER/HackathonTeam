# -*- coding: utf-8 -*-

"""
x, y - start position (top left corner)
image - image
"""
import pygame
import config


class Sprite:
    def __init__(self, x, y, image):
        self.surface = pygame.image.load("Art/%s.png" % image)
        self.x = x
        self.y = y
        self.rect = self.surface.get_rect(topleft=(x, y))

    def draw(self):
        pass


class MovableSprite(Sprite):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

        # Move indicators
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False


class Player(MovableSprite):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def move(self):
        if self.moving_right and self.rect.right < config.level1_width:
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
        if self.moving_bottom and self.rect.bottom < config.level1_height:
            self.rect.y += 1
        if self.moving_top and self.rect.top > 0:
            self.rect.y -= 1

    def collision(self):
        pass


class Mob(MovableSprite):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def behaviour(self):
        pass


class Tile(Sprite):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
