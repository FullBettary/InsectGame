import pygame as pg
from math import atan2, pi


class Creature(pg.sprite.Sprite):
    def __init__(self, filename, x, y, hp=100, dmg=50):
        pg.sprite.Sprite.__init__(self)
        self._image = pg.image.load(filename).convert_alpha()
        self.rect = self._image.get_rect(center=(x, y))
        self._x = x
        self._y = y
        self._hp = hp
        self._dmg = dmg

    def move(self, x, y):
        self.rect.x += round(x, 4)
        self.rect.y += round(y, 4)
        self._x += round(x, 4)
        self._y += round(y, 4)

    def rotation(self, x, y):
        real_x, real_y = x - self._x, y - self._y
        angle = (180 / pi) * -atan2(real_y, real_x) - 90
        im = pg.transform.rotate(self._image, angle)
        self.rect = im.get_rect(center=(self._x, self._y))
        return im, self.rect

    def move_and_rot(self, x, y, m_x, m_y):
        self.move(x, y)
        return self.rotation(m_x, m_y)

    def get_hp(self):
        return self._hp

    def get_dmg(self, dmg):
        self._hp -= dmg

    def get_coord(self):
        return self._x, self._y

