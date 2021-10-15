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
        self.rect = self.surface.get_rect(topleft=(x, y))

    def draw(self):
        pass


class MovableSprite(Sprite):
    def __init__(self, x, y, speed, image):
        super().__init__(x, y, image)

        self.speed = speed

        # Move indicators
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False


class Player(MovableSprite):
    def __init__(self, x, y, speed, image):
        super().__init__(x, y, speed, image)

    def move(self):
        if self.moving_right and self.rect.right < config.level1_width:
            self.rect.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.speed
        if self.moving_bottom and self.rect.bottom < config.level1_height:
            self.rect.y += self.speed
        if self.moving_top and self.rect.top > 0:
            self.rect.y -= self.speed

    def collision(self):
        pass


class Mob(MovableSprite):
    def __init__(self, x, y, speed, image):
        super().__init__(x, y, speed, image)

    def behaviour(self):
        pass


class Tile(Sprite):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
