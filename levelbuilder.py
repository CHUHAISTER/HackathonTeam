# -*- coding: utf-8 -*-

from json import load


def load_level(level):
    level_json = open("%s.json" % level, "r")
    level = load(level_json)
    level_json.close()
    level = level["level"]
    return level


def read_level(level):
    level = load_level(level)
    tile_list = []
    x = 0
    y = 0

    for row in range(0, len(level), 1):
        x = 0
        for character in range(0, len(level[row]), 1):
            if level[row][character] == "G":
                tile_list.append([x, y, level[row][character]])
            x += 64
        y += 64

    return tile_list


def size_level(level):
    level = load_level(level)
    level_size = [0, 0]
    for row in level:
        if len(row) > level_size[0]:
            level_size[0] = len(row)
    level_size[0] = level_size[0] * 64
    level_size[1] = len(level) * 64

    return level_size


def build_level(tile_list):
    pass
