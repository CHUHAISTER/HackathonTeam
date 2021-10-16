# -*- coding: utf-8 -*-

import pygame
from json import load
import config


class Level:
    def __init__(self, name):
        self.tile_list = []
        self.level_size = [0, 0]

        # Load Level
        level_json = open("%s.json" % name, "r")
        self.level = load(level_json)["level"]
        level_json.close()

        # Get level size
        self.size_level()
        # Get tile list
        self.read_level()

        self.surface = pygame.Surface(self.level_size)

    def read_level(self):
        x = 0
        y = 0

        for row in range(0, len(self.level), 1):
            x = 0
            for character in range(0, len(self.level[row]), 1):
                if self.level[row][character] == "G":
                    self.tile_list.append([x, y, self.level[row][character]])
                x += 64
            y += 64

    def size_level(self):
        for row in self.level:
            if len(row) > self.level_size[0]:
                self.level_size[0] = len(row)
        self.level_size[0] = self.level_size[0] * 64
        self.level_size[1] = len(self.level) * 64

        return self.level_size

    def build_level(self, destination):
        for tile in self.tile_list:
            destination.blit(config.tile_textures[tile[2]], (tile[0], tile[1]))
