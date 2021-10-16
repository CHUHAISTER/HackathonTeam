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
    def __init__(self, x, y, speed_x, speed_y, image):
        super().__init__(x, y, image)

        self.speed_x = speed_x
        self.speed_y = speed_y
        self.dx = speed_x
        self.dy = speed_y


class Player(MovableSprite):
    def __init__(self, x, y, speed_x, speed_y, image):
        super().__init__(x, y, speed_x, speed_y, image)

    def move(self):
        # Get all pressed keys on keyboard
        keys = pygame.key.get_pressed()
        # Move Ox
        if keys[pygame.K_RIGHT]:
            self.rect[0] = self.rect[0] + self.dx
        if keys[pygame.K_LEFT]:
            self.rect[0] = self.rect[0] - self.dx
        # Move Oy
        if keys[pygame.K_DOWN]:
            self.rect[1] = self.rect[1] + self.dy
        if keys[pygame.K_UP]:
            self.rect[1] = self.rect[1] - self.dy

    def collosion_x(self, tile_list):
        for tile in tile_list:
            if tile[0]:
                pass

    def collision(self, tile_list):
        character = self
        for tile in tile_list:
            if tile[0] < character.rect[0] + self.dx < tile[0] + 64 and tile[1] < character.rect[1] + self.dy < tile[1] + 64:
                print("tile: ", tile, "character: ", character.rect)
                return True     # Don't move


class Mob(MovableSprite):
    def __init__(self, x, y, speed_x, speed_y, image):
        super().__init__(x, y, speed_x, speed_y, image)

    def behaviour(self):
        pass


class Tile(Sprite):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
