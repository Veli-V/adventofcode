#!/usr/bin/env python3
import sys
import numpy as np
import asyncio
from collections import deque

from nurses_2.app import App
from nurses_2.colors import Color, ColorPair, ColorTheme
from nurses_2.widgets.text_widget import TextWidget
from nurses_2.widgets.scroll_view import ScrollView

# Lot's of this code is taken from
# https://github.com/salt-die/Advent-of-Code/blob/main/2022/visuals/day_14/fast_reservoir/__main__.py
# this is my first time trying nurses_2
#
input_file = 'test_input.txt'
input_file = 'input.txt'
#input_file = "test2.txt"

AIR, ROCK, SAND = 0, 1, 2
MINX, MAXX, MAXY = 300, 700, 173  # From inspection
AIR_COLOR = Color.from_hex("211e1e")
ROCK_COLOR = Color.from_hex("64626b")
SAND_COLOR = Color.from_hex("af803a")
AOC_GREEN = Color.from_hex("009900")
AOC_BRIGHT_GREEN = Color.from_hex("99ff99")
AOC_BLUE = Color.from_hex("0f0f23")
AOC_GREY = Color.from_hex("cccccc")
GREY_ON_BLUE = ColorPair.from_colors(AOC_GREY, AOC_BLUE)
AOC_THEME = ColorTheme(
    primary_fg=AOC_BRIGHT_GREEN,
    primary_bg=AOC_BRIGHT_GREEN,
    primary_fg_light=AOC_GREEN,
    primary_bg_light=AOC_GREEN,
    primary_fg_dark=AOC_BLUE,
    primary_bg_dark=AOC_BLUE,
    secondary_fg=AOC_BRIGHT_GREEN,
    secondary_bg=AOC_BRIGHT_GREEN,
)

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]
data = [d.split("->") for d in data]

def addCoord(x, y):
    return [x[0]+y[0], x[1]+y[1]]

def parseInput():
    cave = np.zeros((MAXY +1, MAXX - MINX +1 ), int)
    for d in data:
        for i in range(1, len(d)):
            start = d[i-1].split(",")
            end = d[i].split(",")
            start = [int(s) for s in start]
            end = [int(e) for e in end]
            if start[1] == end[1]:
                if start[0] < end[0]:
                    for j in range(start[0], end[0]+1):
                        cave[start[1], j-MINX] = ROCK
                else:
                    for j in range(end[0], start[0]+1):
                        cave[start[1], j-MINX] = ROCK
            elif start[0] == end[0]:
                if start[1] < end[1]:
                    for j in range(start[1], end[1]+1):
                        cave[j, start[0]-MINX] = ROCK
                else:
                    for j in range(end[1], start[1]+1):
                        cave[j, start[0]-MINX] = ROCK
    cave[-1] = ROCK
    return cave

class CaveApp(App):
    async def on_start(self):
        cave = parseInput()
        print(cave)

        cave_widget = TextWidget(size=cave.shape, default_color_pair=GREY_ON_BLUE)
        cave_widget.canvas[cave==AIR] = "."
        cave_widget.colors[..., :3][cave==AIR] = AIR_COLOR
        cave_widget.canvas[cave==ROCK] = "#"
        cave_widget.colors[..., :3][cave==ROCK] = ROCK_COLOR

        cave_view = ScrollView(size_hint=(1.0, 1.0), disable_ptf=True)
        cave_view.view = cave_widget
        cave_view.horizontal_proportion = .5

        sand_count_label = TextWidget(
            size=(1, 17),
            pos_hint=(None, .5),
            anchor="center",
            default_color_pair=GREY_ON_BLUE,
        )

        self.add_widgets(cave_view, sand_count_label)

        particles = deque()

        def update_cave(old, new):
            if old is not None:
                cave[old] = AIR
                cave_widget.canvas[old] = "."
                cave_widget.colors[old][:3] = AIR_COLOR

            cave[new] = SAND
            cave_widget.canvas[new] = "o"
            cave_widget.colors[new][:3] = SAND_COLOR
            particles.append(new)


        tick = sand_count = 0
        while cave[0, 500 - MINX] != SAND:
            if tick % 4 == 0:
                update_cave(None, (0, 500 - MINX))
                sand_count += 1
                sand_count_label.add_text(f"Sand count: {sand_count:<5}")

            for _ in range(len(particles)):
                pos = y, x = particles.popleft()
                for dx in (0, -1, 1):
                    if cave[y + 1, x + dx] == AIR:
                        update_cave(pos, (y + 1, x + dx))
                        break

            tick += 1
            await asyncio.sleep(0)


CaveApp(
    title="Test",
    color_theme=AOC_THEME,
    background_color_pair=GREY_ON_BLUE,
).run()
#sand = [500, 0]
#lasts = (500,0)
#rested = True
#falls = [[0,1], [-1,1], [1,1]]
#sands = 0
#part1 = 0
#part1done = False
#
#while rested:
#    stillFalling = False
#    for f in falls:
#        toTest = addCoord(sand, f)
#        toTest = (toTest[0], toTest[1])
#        if toTest not in cave:
#            stillFalling = True
#            sand = toTest
#            break
#    if not stillFalling or sand[1] == maxy+1:
#        if part1done == False and sand[1] == maxy+1:
#            part1done = True
#            part1 = sands
#        cave[sand] = "x"
#        cave[lasts] = "o"
#        lasts = sand
#        sands += 1
#        sand = (500, 0)
#    if cave.get((500,0))== "x": break
#    if sand[1] > 200: break
#
#
#
#cave[(500,0)] = "S"
#print()
#for i in range(0, maxy+10):
#    print(str(i).zfill(3), end=" ")
#    for j in range(minx-10, maxx+10):
#        if cave.get((j, i)) == None: print(".", end="")
#        else: print(cave.get((j,i)), end="")
#    print()
#
#print("Part1:")
#print("It dropped {} before going to void".format(part1))
#print("Part2:")
#print("It dropped {} before blocking start".format(sands))
