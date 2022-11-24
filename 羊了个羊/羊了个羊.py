import pgzrun
import pygame
import random
import math
import os


TITLE = '羊了个羊' 
WIDTH = 600
HEIGHT = 720

T_WIDTH = 60
T_HEIGHT = 66

DOCK = Rect((90, 564), (T_WIDTH*7, T_HEIGHT))

tiles = []

docks = []
x =7#7

ts = list(range(1, 13))*12
random.shuffle(ts)
n = 0
for k in range(x): 
    for i in range(7-k):
        for j in range(7-k):
            t = ts[n]
            n += 1
            tile = Actor(f'tile{t}')
            tile.pos = 120 + (k * 0.5 + j) * tile.width, 100 + (k * 0.5 + i) * tile.height * 0.9
            tile.tag = t
            tile.layer = k
            tile.status = 1 if k ==x-1 else 0
            tiles.append(tile)
for i in range(4):#4
    t = ts[n]
    n += 1
    tile = Actor(f'tile{t}')
    tile.pos = 210 + i * tile.width, 516
    tile.tag = t
    tile.layer = 0
    tile.status = 1
    tiles.append(tile)



def draw():
    screen.clear()
    screen.blit('back', (0, 0))
    for tile in tiles:

        tile.draw()
        if tile.status == 0:
            screen.blit('mask', tile.topleft)
    for i, tile in enumerate(docks):

        tile.left = (DOCK.x + i * T_WIDTH)
        tile.top = DOCK.y
        tile.draw()

    if len(docks) >= 7:
        screen.blit('end', (0, 0))

    if len(tiles) == 0:
        screen.blit('win', (0, 0))


def on_mouse_down(pos):
    global docks
    if len(docks) >= 7 or len(tiles) == 0:
        return
    for tile in reversed(tiles):
        if tile.status == 1 and tile.collidepoint(pos):

            tile.status = 2
            tiles.remove(tile)
            diff = [t for t in docks if t.tag != tile.tag]
            if len(docks) - len(diff) < 2:
                docks.append(tile)
            else:
                docks = diff
            for down in tiles:
                if down.layer == tile.layer - 1 and down.colliderect(tile):
                    for up in tiles:
                        if up.layer == down.layer + 1 and up.colliderect(down):
                            break
                    else:
                        down.status = 1
            return



pgzrun.go()
