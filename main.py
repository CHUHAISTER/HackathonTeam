# -*- coding: utf-8 -*-

import os
import pygame

"""
pygame.image.load() - returns Surface
Surface() - It's like plot on which I place pictures
Surface.get_rect() - returns Rect
Rect(left, top, width, height) - Saves coords of Surface
Surface.blit(surface, coords) = on_this.draw(this, coords) (coords=(x,y) or Rect) 

if event.type == pygame.MOUSEMOTION: event return (pos)
"""


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
        if game_state == "Menu":
            mouse_on_button(events)
        elif game_state == "Playing":
            pass
        window.update()
        mainloop()


def binds(events):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def mouse_on_button(events):
    for event in events:
        if event.type == 1025 and event.button == 1:
            if button_start_rect[0] < event.pos[0] < button_start_rect[0] + button_start_rect[2] and \
            button_start_rect[1] < event.pos[1] < button_start_rect[1] + button_start_rect[3]:
                global game_state
                game_state = "Playing"
                screen_surface.blit(level_surface, (0, 0))


pygame.init()
clock = pygame.time.Clock()

window = pygame.display

window_width = 1366
window_height = 768

# Set screen_surface
screen_surface = window.set_mode(size=(window_width, window_height), flags=pygame.FULLSCREEN, depth=32)
screen_surface.fill((150, 30, 0))
window.set_caption('Game')

# Set level_surface
level_surface = pygame.Surface((window_width, window_height))
level_surface.fill((255, 255, 255))

# Start Button
button_start_surface = pygame.image.load("Art/button_start.png")
button_start_rect = button_start_surface.get_rect(topleft=(100, 100))
screen_surface.blit(button_start_surface, button_start_rect)

game_state = "Menu"

mainloop()
