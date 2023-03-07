import sys
import pygame as pg
from src.Const import *
from src.game.gameProcess.Player import Player
from src.game.gameProcess.DrawModule import draw
from src.game.gameProcess.CollideModule import check_collide
from src.game.gameProcess.MobFactory import Mob_Factory
from src.interface.game_interface.interface import Interface
from src.interface.Button import Button
from src.interface.menu.PauseMenu import pause_menu
from src.serialization import Serialization
import time


class Game:
    @staticmethod
    def start(main_sf):

        clock = pg.time.Clock()

        surface = pg.Surface(SIZE_SCREEN)
        interface = Interface(surface)

        player = Player(player_im, SIZE_SCREEN[0] // 2, SIZE_SCREEN[1] // 2)
        mob_factory = Mob_Factory(player)

        mob_list = mob_factory.create_mobs()
        bullet_list = []

        game_status = player.is_alive()
        score = 0
        t = 0

        pause_butt = Button(surface, lambda: pause_menu(main_sf), (SIZE_SCREEN[0] / 2 - 50, 0, 60, 30), 'PAUSE', 18)
        start_tick = time.time()

        while game_status:
            pg.display.update()
            clock.tick(FPS)

            events = pg.event.get()

            for event in events:
                if event.type == pg.MOUSEBUTTONUP:
                    if event.button == 1:
                        pos = pg.mouse.get_pos()
                        bullet = player.event_shooting(pos[0], pos[1])
                        if bullet is not None:
                            bullet_list.append(bullet)

            surface.fill(COLOR)

            count_mob = len(mob_list)

            draw(surface, player, bullet_list, mob_list)
            check_collide(bullet_list, mob_list)

            end_tick = time.time()
            t = end_tick - start_tick
            game_time = time.gmtime(t)

            interface.show(player.get_hp(), score, time.strftime("%M:%S", game_time), player.get_count_amo())

            game_status = player.is_alive()

            if len(mob_list) < count_mob:
                score += (count_mob - len(mob_list)) * 10

            mob_factory.check_mob_count()

            pause_butt.work(events)
            main_sf.blit(surface, (0, 0))

            for event in events:
                if event.type == pg.QUIT:
                    Serialization.write(score, t)
                    sys.exit()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_p:
                        game_status = False

        mob_factory.clear_mob_list()
        Serialization.write(score, t)
