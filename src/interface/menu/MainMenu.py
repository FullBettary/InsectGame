import pygame as pg
import sys
from src.Const import *
import src.game.Game as Game
from src.interface.Button import Button
from src.interface.menu.Record_menu import record_menu
from src.interface.menu.InfoMenu import info_menu


def main_menu():
    surface = pg.display.set_mode(SIZE_SCREEN)
    clock = pg.time.Clock()

    surface.fill(COLOR)

    play_butt = Button(surface, lambda: Game.Game.start(surface), (600, 150, 270, 100), 'PLAY', 140)
    r_menu = Button(surface, lambda: record_menu(surface), (500, 350, 270, 100), 'RECORDS', 140)
    inf_menu = Button(surface, lambda: info_menu(surface), (600, 500, 270, 100), "INFO", 140)
    exit_butt = Button(surface, sys.exit, (600, 650, 270, 100), 'EXIT', 140)

    while True:
        surface.fill(COLOR)

        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                sys.exit()

        play_butt.work(events)
        r_menu.work(events)
        inf_menu.work(events)
        exit_butt.work(events)

        pg.display.update()
        clock.tick(FPS)
