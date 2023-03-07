import pygame as pg
from src.Const import *
from sys import exit
from src.interface.Button import *

__pause = True


def __change_pause():
    global __pause
    __pause = not __pause


def pause_menu(sf):
    global __pause
    __pause = True

    resume_butt = Button(sf, __change_pause, (500, 250, 550, 100), "CONTINUE", 140)

    clock = pg.time.Clock()

    while __pause:

        events = pg.event.get()

        for event in events:
            if event.type == pg.QUIT:
                exit()

        resume_butt.work(events)
        pg.display.update()
        clock.tick(FPS)
