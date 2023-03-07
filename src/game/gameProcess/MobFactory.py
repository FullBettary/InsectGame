from src.Const import *
from random import randint
from src.game.gameProcess.Mob import Mob


class Mob_Factory:

    __mob_list = []
    __count_mob = 16

    def __init__(self, player):
        self.__player = player

    def __create_mob(self):
        coord = self.__random_coord()
        self.__mob_list.append(Mob(mob_list_im[randint(0, len(mob_list_im) - 1)], coord[0], coord[1], self.__player))

    def __random_coord(self):
        random_side = ['left', 'top', 'right', 'bottom'][randint(0, 3)]
        coord = []
        if random_side == 'left':
            coord.append(0)
            coord.append(randint(0, SIZE_SCREEN[1] - 1))
        elif random_side == 'top':
            coord.append(randint(0, SIZE_SCREEN[0] - 1))
            coord.append(0)
        elif random_side == 'right':
            coord.append(SIZE_SCREEN[0] - 1)
            coord.append(randint(0, SIZE_SCREEN[1] - 1))
        elif random_side == 'bottom':
            coord.append(randint(0, SIZE_SCREEN[0] - 1))
            coord.append(SIZE_SCREEN[1] - 1)
        return coord

    def create_mobs(self):
        for i in range(self.__count_mob):
            self.__create_mob()
        return self.__mob_list

    def check_mob_count(self):
        if len(self.__mob_list) < self.__count_mob:
            for i in range(self.__count_mob - len(self.__mob_list)):
                coord = self.__random_coord()
                self.__mob_list.append(Mob(mob_list_im[randint(0, len(mob_list_im) - 1)], coord[0], coord[1], self.__player))
        if randint(1, 90) == 5:
            self.__create_mob()

    def clear_mob_list(self):
        self.__mob_list.clear()
