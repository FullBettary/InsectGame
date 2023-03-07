import pygame as pg
from src.game.gameProcess.Creature import Creature
from src.game.gameProcess.Bullet import Bullet
from src.Const import bullet_im, SIZE_SCREEN
import time


class Player(Creature):

    __bullet_count = 35
    __amo = __bullet_count
    __for_reload = 0

    def __int__(self, filename, x, y):
        super().__init__(filename, x, y)

    def __check_amo(self):
        if self.__amo == 0:
            t = time.time()
            if t - self.__for_reload > 3:  # reload lasts 3 second
                self.__amo = self.__bullet_count

    def handler_event_to_move(self):
        step = 3
        keys = pg.key.get_pressed()

        if keys[pg.K_w] and self._y > 10: self.move(0, -step)
        if keys[pg.K_s] and self._y < SIZE_SCREEN[1] - 10: self.move(0, step)
        if keys[pg.K_a] and self._x > 10: self.move(-step, 0)
        if keys[pg.K_d] and self._x < SIZE_SCREEN[0] - 10: self.move(step, 0)

    def handler_event_to_rotation(self):
        mouse_pos = pg.mouse.get_pos()

        return self.rotation(mouse_pos[0], mouse_pos[1])

    def event_move_and_rot(self):

        self.__check_amo()

        self.handler_event_to_move()
        return self.handler_event_to_rotation()

    def event_shooting(self, x, y):
        if self.__amo != 0:
            self.__amo -= 1
            if self.__amo == 0:
                self.__for_reload = time.time()
            return Bullet(bullet_im, self._x, self._y, x, y)

    def is_alive(self):
        if self._hp <= 0:
            return False
        else:
            return True

    def hit(self):
        return self._dmg

    def get_count_amo(self):
        return self.__amo


