import pygame as pg
from src.Const import *
from math import atan2, pi


class Bullet(pg.sprite.Sprite):

    def __init__(self, filename, x1, y1, x2, y2):
        pg.sprite.Sprite.__init__(self)
        real_x, real_y = x2 - x1, y2 - y1
        angle = (180 / pi) * -atan2(real_y, real_x) - 90
        self.image = pg.image.load(filename).convert_alpha()
        self.image = pg.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=(x1, y1))
        self.x = x1
        self.y = y1
        self.dx = x2 - x1
        self.dy = y2 - y1
        t = max(abs(self.dx), abs(self.dy)) * 0.21
        speed = 3
        self.dx, self.dy = self.dx * speed / t, self.dy * speed / t

    def action(self):

        self.rect.x += round(self.dx, 4)
        self.rect.y += round(self.dy, 4)

        if self.x < 0 or self.x > SIZE_SCREEN[0] or self.y < 0 or self.y > SIZE_SCREEN[1]:
            del self
            return None
        else:
            return self.image, self.rect

    def collide(self):
        del self
