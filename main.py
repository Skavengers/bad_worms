from math import *
from kandinsky import *
from ion import *
from time import *

WOOD = (64, 4, 16)
WHITE = (248, 252, 248)
EAU = (0, 148, 200)
SAND = (248, 228, 144)
POISON = (0, 252, 0)
POISOND = (0, 152, 0)
fill_rect(0, 218, 150, 10, (0,) * 3)

class Gravity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.nb = 0

    def paint(self, x, y, w, h):
        c = input("")
        cc = tuple(c)
        self.xs = self.x + 2
        self.ys = self.y + 6
        fill_rect(self.xs, self.ys, w, h, c)

    def zwood(self, x, y, w, h):
        self.nb += 1
        self.xs = self.x + 2
        self.ys = self.y + 6
        fill_rect(self.xs, self.ys, w, h, WOOD)
        pos1 = get_pixel(self.xs, self.ys + h)
        pos2 = get_pixel(self.xs + w, self.ys + h)
        while pos1 == WHITE and pos2 == WHITE:
            fill_rect(self.xs, self.ys, w, h, WHITE)
            self.ys += 1
            fill_rect(self.xs, self.ys, w, h, WOOD)
            pos1 = get_pixel(self.xs, self.ys + h)
            if w != 1:
                pos2 = get_pixel(self.xs + w, self.ys + h)

    def wood(self, x, y, w, h):
        self.nb += 1
        self.xs = self.x + 2
        self.ys = self.y + 6
        fill_rect(self.xs, self.ys, w, h, WOOD)
        posm = get_pixel(self.xs, self.ys + h)
        while posm == WHITE:
            fill_rect(self.xs, self.ys, w, h, WHITE)
            self.ys += 1
            fill_rect(self.xs, self.ys, w, h, WOOD)
            posm = get_pixel(self.xs, self.ys + h)

    def poison(self, x, y):
        self.nb += 1
        self.xs = self.x + 2
        self.ys = self.y + 6
        posm = get_pixel(self.xs, self.ys)
        while posm == WHITE:
            set_pixel(self.xs, self.ys, WHITE)
            self.ys += 1
            set_pixel(self.xs, self.ys, POISON)
            posm = get_pixel(self.xs, self.ys + 1)
        self.ys += 1
        while posm == POISON or posm == POISOND:
            set_pixel(self.xs, self.ys, POISOND)
            self.ys += 2
            set_pixel(self.xs, self.ys, POISON)
            posm = get_pixel(self.xs, self.ys + 1)
            # if posm==WHITE:
            # try:
            # self.poison(self.x,self.y)

    def zand(self, x, y):
        self.nb += 1
        self.xs = self.x + 2
        self.ys = self.y + 6
        set_pixel(self.xs, self.ys, SAND)
        posm = get_pixel(self.xs, self.ys + 1)
        posd = get_pixel(self.xs - 1, self.ys + 1)
        posg = get_pixel(self.xs + 1, self.ys + 1)
        while posm == WHITE:
            set_pixel(self.xs, self.ys, WHITE)
            self.ys += 1
            set_pixel(self.xs, self.ys, SAND)
            posm = get_pixel(self.xs, self.ys + 1)
        while posd == WHITE and posg == WHITE:
            if self.nb % 2 == 0:
                while posd == WHITE and self.nb % 2 == 0:
                    set_pixel(self.xs, self.ys, SAND)
                    self.ys += 1
                    self.xs -= 1
                    set_pixel(self.xs, self.ys, SAND)
                    posd = get_pixel(self.xs - 1, self.ys + 1)
            while posg == WHITE:
                set_pixel(self.xs, self.ys, SAND)
                self.ys += 1
                self.xs += 1
                set_pixel(self.xs, self.ys, SAND)
                posg = get_pixel(self.xs + 1, self.ys + 1)

    def cursor(self, x, y):
        if keydown(KEY_UP):
            fill_rect(self.x, self.y, 5, 5, (255,) * 3)
            self.y -= 1
        if keydown(KEY_DOWN):
            fill_rect(self.x, self.y, 5, 5, (255,) * 3)
            self.y += 1
        if keydown(KEY_RIGHT):
            fill_rect(self.x, self.y, 5, 5, (255,) * 3)
            self.x += 1
        if keydown(KEY_LEFT):
            fill_rect(self.x, self.y, 5, 5, (255,) * 3)
            self.x -= 1
        fill_rect(self.x, self.y, 5, 5, (0,) * 3)
        return self.x, self.y


def loop():
    x = 160
    y = 100
    p = Gravity(x, y)
    while True:
        qq = p.cursor(p.x, p.y)
        if keydown(KEY_OK):
            aa = p.paint(p.x, p.y, 5, 5)
        if keydown(KEY_ONE):
            # sleep(0.1)
            bb = p.zand(p.x, p.y)
        if keydown(KEY_TWO):
            cc = p.zwood(p.x, p.y, 5, 5)
        if keydown(KEY_THREE):
            dd = p.wood(p.x, p.y, 1, 1)
        if keydown(KEY_FOUR):
            ee = p.poison(p.x, p.y)


fill_rect(150, 60, 80, 10, (0,) * 3)
fill_rect(100, 100, 20, 20, (0,) * 3)
loop()
