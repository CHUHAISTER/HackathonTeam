# -*- coding: utf-8 -*-

import pygame
import config
from sprite import Player
from buttons import Button
from level import Level

"""
pygame.image.load() - returns Surface
Surface() - It's like plot on which I place pictures
Surface.get_rect() - returns Rect
Rect(left, top, width, height) - Saves coords of Surface
Surface.blit(surface, coords) = on_this.draw(this, coords) (coords=(x,y) or Rect) 

if event.type == pygame.MOUSEMOTION: event return (pos)
"""


class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        self.clock = pygame.time.Clock()

        # Set window
        self.window = pygame.display
        self.window.set_caption('Game')

        # Get user screen resolution
        self.window_width = self.window.Info().current_w
        self.window_height = self.window.Info().current_h

        # Set screen_surface
        self.screen_surface = self.window.set_mode(size=(self.window_width, self.window_height), flags=pygame.FULLSCREEN, depth=32)
        self.screen_surface.fill((150, 30, 0))

        # Camera_surface
        self.camera_surface = pygame.Surface((self.window_width, self.window_height))

        # Game State
        self.game_state = "Menu"
        # Pressed buttons on keyboard
        self.events = None

    def mainloop(self):
        while True:
            self.clock.tick(60)
            self.events = pygame.event.get()
            self.binds()
            if self.game_state == "Menu":
                self.build_menu()
                self.mouse_on_button()
            elif self.game_state == "Playing":
                player.move()
                self.draw_level()
            self.window.update()
            pygame.display.flip()

    def binds(self):
        for event in self.events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def mouse_on_button(self):
        for event in self.events:
            if event.type == 1025 and event.button == 1:
                if button_start.rect[0] < event.pos[0] < button_start.rect[0] + button_start.rect[2] and \
                button_start.rect[1] < event.pos[1] < button_start.rect[1] + button_start.rect[3]:
                    self.game_state = "Playing"
                    self.window.update()
            if event.type == 1025 and event.button == 1:
                if button_exit.rect[0] < event.pos[0] < button_exit.rect[0] + button_exit.rect[2] and \
                button_exit.rect[1] < event.pos[1] < button_exit.rect[1] + button_exit.rect[3]:
                    pygame.quit()
                    exit()

    def draw_level(self):
        level1.surface.fill((150, 255, 255))
        level1.build_level()
        level1.surface.blit(player.surface, player.rect)
        self.screen_surface.blit(self.camera_surface, (0, 0))
        self.camera_surface.blit(level1.surface, (0, 0), area=(player.rect[0]-(self.window_width/2),
                                                               player.rect[1]-(self.window_height/2),
                                                               self.window_width, self.window_height))

    def build_menu(self):
        self.screen_surface.blit(button_start.surface, button_start.rect)
        self.screen_surface.blit(button_exit.surface, button_exit.rect)


# Create game instance
game = Game()

# Create player
player = Player(500, 500, 10, 10, 'test')

# Create buttons
button_start = Button("midtop", game.window_width/2, 100, 'button_start')
button_exit = Button("midtop", game.window_width/2, 500, 'button_exit')

# Create level instances
level1 = Level("level1")

# Start
game.mainloop()
