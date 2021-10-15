# -*- coding: utf-8 -*-

import sprite


class Button(sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)


# Here I'll draw all buttons in menu
def draw_buttons():
    pass


# Create dict {button: (lambda) function}
