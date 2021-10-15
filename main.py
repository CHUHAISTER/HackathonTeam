# -*- coding: utf-8 -*-

import pygame
import config
import sprite
import buttons

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

        # Set level_surface
        self.level_surface = pygame.Surface((self.window_width, self.window_height))
        self.level_surface.fill((150, 255, 255))

        # Start Button
        self.button_start_surface = pygame.image.load("Art/start.jpg")
        self.button_start_rect = self.button_start_surface.get_rect(topleft=(400, 100))
        self.screen_surface.blit(self.button_start_surface, self.button_start_rect)

        # Exit Button
        self.button_exit_surface = pygame.image.load("Art/exit.jpg")
        self.button_exit_rect = self.button_exit_surface.get_rect(topleft=(420, 500))
        self.screen_surface.blit(self.button_exit_surface, self.button_exit_rect)

    def mainloop(self):
        while True:
            self.clock.tick(60)
            self.events = pygame.event.get()
            self.binds()
            if self.game_state == "Menu":
                self.mouse_on_button()
            elif self.game_state == "Playing":
                player.move()
                self.draw_screen()
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
                if self.button_start_rect[0] < event.pos[0] < self.button_start_rect[0] + self.button_start_rect[2] and \
                self.button_start_rect[1] < event.pos[1] < self.button_start_rect[1] + self.button_start_rect[3]:
                    self.game_state = "Playing"
                    self.window.update()
            if event.type == 1025 and event.button == 1:
                if self.button_exit_rect[0] < event.pos[0] < self.button_exit_rect[0] + self.button_exit_rect[2] and \
                self.button_exit_rect[1] < event.pos[1] < self.button_exit_rect[1] + self.button_exit_rect[3]:
                    pygame.quit()
                    exit()

    def draw_screen(self):
        self.screen_surface.blit(self.level_surface, (0, 0))
        self.screen_surface.blit(player.surface, player.rect)


player = sprite.Player(500, 500, 'test')

# Create game instance
game = Game()
# Start
game.mainloop()
