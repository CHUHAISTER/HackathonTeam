# -*- coding: utf-8 -*-

"""
x, y - start position (top left corner)
image - image
"""

import pygame


class Sprite:
    def __init__(self, x, y, image):
        self.surface = pygame.image.load("Art/%s.png" % image)
        self.rect = self.surface.get_rect(topleft=(x, y))

    def draw(self):
        pass


class MovableSprite(Sprite):
    def __init__(self, x, y, max_speed, image):
        super().__init__(x, y, image)

        self.ax = 1
        self.ay = 1
        self.max_speed = max_speed
        self.dx = 0
        self.dy = 0

    def collision(self, tile_list):
        for tile in tile_list:
            if self.rect[0] + self.rect[2] + self.dx < tile[0]+1 or self.rect[0] + self.dx > tile[0]+63:
                continue
            if self.rect[1] + self.rect[3] + self.dy < tile[1]+1 or self.rect[1] + self.dy > tile[1]+63:
                continue
            self.dx = 0
            self.dy =0


class Player(MovableSprite):
    def __init__(self, x, y, max_speed, image):
        super().__init__(x, y, max_speed, image)

    def move(self, tile_list):
        # Get all pressed keys on keyboard
        keys = pygame.key.get_pressed()
        # Move Ox
        if keys[pygame.K_RIGHT] and abs(self.dx) != self.max_speed:
            self.dx += self.ax
        elif keys[pygame.K_LEFT] and abs(self.dx) != self.max_speed:
            self.dx -= self.ax
        # Decrease dx
        elif self.dx > 0:
            self.dx -= self.ax
        elif self.dx < 0:
            self.dx += self.ax
        # Move Oy
        if keys[pygame.K_DOWN] and abs(self.dy) != self.max_speed:
            self.dy += self.ay
        elif keys[pygame.K_UP] and abs(self.dy) != self.max_speed:
            self.dy -= self.ay
        # Decrease dy
        elif self.dy > 0:
            self.dy -= self.ay
        elif self.dy < 0:
            self.dy += self.ay

        self.collision(tile_list)
        self.rect[0] = self.rect[0] + self.dx
        self.rect[1] = self.rect[1] + self.dy


class Mob(MovableSprite):
    def __init__(self, x, y, speed_x, speed_y, image):
        super().__init__(x, y, speed_x, speed_y, image)

    def behaviour(self):
        pass


class Tile(Sprite):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
