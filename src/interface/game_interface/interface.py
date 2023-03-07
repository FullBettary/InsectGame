import pygame as pg
from src.Const import *
import time


class Interface:
    def __init__(self, sf):
        self.__image_bull = pg.image.load(bullet_ico).convert_alpha()
        self.__rect_bull = self.__image_bull.get_rect(bottomright=(SIZE_SCREEN[0] - 10, SIZE_SCREEN[1] - 10))
        self.__sf = sf
        self.__hp_line = pg.Surface((260, 30))
        pg.font.init()
        self.__font = pg.font.Font(None, 50)
        self.__reload = 0

    def show(self, player_hp, score, seconds, amo):
        # draw health line
        pg.draw.rect(self.__hp_line, COLOR, (0, 0, 260, 30))
        hp_text = self.__font.render("HP", True, GREEN)
        self.__hp_line.blit(hp_text, (0, 0))
        pg.draw.rect(self.__hp_line, GREEN, (60, 0, player_hp * 2, 30))

        # draw score
        score_disp = self.__font.render(f"SCORE: {score}", True, PASSIVE_FONT)

        # draw timer
        time_disp = self.__font.render(f"{seconds}", True, PASSIVE_FONT)

        # draw count amo
        if amo == 0:
            amo = " ." * (int(time.time()) % 4)
        count_amo = self.__font.render(f"{amo}", True, YELLOW)
        rect_amo = count_amo.get_rect(bottomright=(SIZE_SCREEN[0] - 38, SIZE_SCREEN[1] - 10))

        # show all on display
        self.__sf.blit(self.__hp_line, (5, 5))
        self.__sf.blit(score_disp, (5, 40))
        self.__sf.blit(time_disp, (SIZE_SCREEN[0] - 100, 0))

        self.__sf.blit(self.__image_bull, self.__rect_bull)
        self.__sf.blit(count_amo, rect_amo)


