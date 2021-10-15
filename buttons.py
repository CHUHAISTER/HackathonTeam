# -*- coding: utf-8 -*-

import pygame
import sprite


class Button(sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        # self.surface = pygame.image.load("Art/button_start.png")
        # self.rect = self.surface.get_rect(topleft=coords)


# Here I'll draw all buttons in menu
def draw_buttons():
    pass


# Create dict {button: (lambda) function}
