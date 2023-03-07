import sys
import pygame as pg
from src.Const import *
from src.interface.Button import *

__in_menu = True


def __change_status():
    global __in_menu
    __in_menu = not __in_menu


def info_menu(main_sf):

    global __in_menu
    __in_menu = True

    surface = pg.Surface(SIZE_SCREEN)
    surface.fill(COLOR)
    clock = pg.time.Clock()

    pg.font.init()

    font = pg.font.Font(None, 50)

    control_t = font.render("CONTROL . . . . . W/A/S/D adn MOUSE", True, PASSIVE_FONT)
    control_rect = control_t.get_rect(topleft=(200, 200))
    surface.blit(control_t, control_rect)

    back_to_menu_t = font.render("BACK TO MAIN MENU . . . P", True, PASSIVE_FONT)
    back_to_menu_rect = back_to_menu_t.get_rect(topleft=(200, 250))
    surface.blit(back_to_menu_t, back_to_menu_rect)

    info = font.render("Yor target survive as long as possible and kill as much as possible insect", True, PASSIVE_FONT)
    info_rect = info.get_rect(topleft=(200, 350))
    surface.blit(info, info_rect)

    back_to_menu = Button(surface, __change_status, (10, 10, 150, 35), 'BACK TO MENU', 30)

    while __in_menu:
        events = pg.event.get()

        for event in events:
            if event.type == pg.QUIT:
                sys.exit()

        back_to_menu.work(events)

        main_sf.blit(surface, (0, 0))
        pg.display.update()
        clock.tick(FPS)
