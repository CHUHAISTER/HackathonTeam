# -*- coding: utf-8 -*-

import pygame
import config
from sprite import Player
from buttons import Button
import levelbuilder

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

        # Game State
        self.game_state = "Menu"
        # Pressed buttons on keyboard
        self.events = None

        # Set level1_surface
        self.level1_surface = pygame.Surface(levelbuilder.size_level("level1"))
        self.level1_surface.fill((150, 255, 255))

        # Temporary
        self.tileG = pygame.image.load("Art/G.png")

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

    def binds(self):
        for event in self.events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move player right
                    player.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # Move player left
                    player.moving_left = True
                elif event.key == pygame.K_UP:
                    # Move player up
                    player.moving_top = True
                elif event.key == pygame.K_DOWN:
                    # Move player down
                    player.moving_bottom = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.moving_right = False
                elif event.key == pygame.K_LEFT:
                    player.moving_left = False
                elif event.key == pygame.K_UP:
                    player.moving_top = False
                elif event.key == pygame.K_DOWN:
                    player.moving_bottom = False

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
        self.level1_surface.fill((150, 255, 255))
        self.screen_surface.blit(self.level1_surface, (0, 0))
        self.draw_map()
        self.screen_surface.blit(player.surface, player.rect)

    def build_menu(self):
        self.screen_surface.blit(button_start.surface, button_start.rect)
        self.screen_surface.blit(button_exit.surface, button_exit.rect)

    def draw_map(self):
        tile_list = levelbuilder.read_level("level1")
        for tile in tile_list:
            self.screen_surface.blit(self.tileG, (tile[0], tile[1]))


# Create game instance
game = Game()

# Create player
player = Player(500, 500, 5, 'test')

# Create buttons
button_start = Button("midtop", game.window_width/2, 100, 'button_start')
button_exit = Button("midtop", game.window_width/2, 500, 'button_exit')

# Start
game.mainloop()
