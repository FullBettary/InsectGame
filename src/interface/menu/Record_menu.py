import pygame as pg
import sys
from src.Const import *
from src.interface.Button import Button
from src.serialization.Serialization import *
import time

__in_menu = True
__data = read()


def __change_data():
    global __data
    reset()
    __data = read()


def __change_status():
    global __in_menu
    __in_menu = False


def record_menu(main_sf):
    global __in_menu
    __in_menu = True

    global __data
    __data = read()

    surface = pg.Surface(SIZE_SCREEN)
    surface.fill(COLOR)

    clock = pg.time.Clock()

    back_to_menu = Button(surface, __change_status, (10, 10, 150, 35), 'BACK TO MENU', 30)
    reset_butt = Button(surface, __change_data, (600, 450, 270, 45), "RESET", 40)

    pg.font.init()
    font = pg.font.Font(None, 50)

    while __in_menu:
        surface.fill(COLOR)

        events = pg.event.get()

        for event in events:
            if event.type == pg.QUIT:
                sys.exit()

        score = str(__data[0])
        text_score = font.render(f'MAX SCORE . . . . . {score}', True, PASSIVE_FONT)
        t_sc_rect = text_score.get_rect(topleft=(400, 250))
        surface.blit(text_score, t_sc_rect)

        t = time.strftime("%M:%S", time.gmtime(__data[1]))
        text_time = font.render(f'MAX TIME . . . . . {t}', True, PASSIVE_FONT)
        t_ti_rect = text_score.get_rect(topleft=(400, 350))
        surface.blit(text_time, t_ti_rect)

        back_to_menu.work(events)
        reset_butt.work(events)

        clock.tick(FPS)
        main_sf.blit(surface, (0, 0))
        pg.display.update()

