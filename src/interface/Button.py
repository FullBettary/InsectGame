import pygame as pg
from src.Const import *


class Button:
    def __init__(self, sf, func, size, text, size_pt):
        pg.font.init()
        self.__font = pg.font.Font(None, size_pt)
        self.__sf = sf
        self.__rect = pg.Rect(size)
        self.__size = size
        self.__text = text
        self.__func = func
        self.__size_pt = size_pt

    def work(self, events):
        text = self.__font.render(self.__text, True, PASSIVE_FONT)
        rect = text.get_rect()
        coord_rect = (self.__size[0], self.__size[1], rect.size[0] + 20, self.__size[3])
        pg.draw.rect(self.__sf, BUTTON_COLOR, coord_rect)

        if self.__rect.collidepoint(pg.mouse.get_pos()):
            text = self.__font.render(self.__text, True, ACTIVE_FONT)

        self.__sf.blit(text, (self.__size[0] + 10, self.__size[1] + 10))

        for event in events:
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    if self.__rect.collidepoint(pg.mouse.get_pos()):
                        self.__func()



