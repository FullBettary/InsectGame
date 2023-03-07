from src.game.gameProcess.Creature import Creature
from random import uniform


class Mob(Creature):

    def __init__(self, filename, x, y, player, dmg=10):
        super().__init__(filename, x, y, dmg=dmg)
        self.player = player
        self.speed = uniform(0.7, 1)

    def handler_event_to_move(self):
        coord = self.player.get_coord()
        p_x, p_y = coord[0], coord[1]
        dx, dy = p_x - self._x, p_y - self._y
        r = (dx**2 + dy**2)**0.5

        if 10 <= r <= 20:
            self.move(0, 0)
            return
        if r <= 30:
            self.give_damage()

        t = self.speed * max(abs(dx), abs(dy)) // 1.25
        if t == 0:
            t = 1

        if r < 10:
            self.move(-dx/t, -dy/t)
            return

        vx, vy = dx/t, dy/t
        self.move(vx, vy)

    def handler_event_to_rotation(self):
        coord = self.player.get_coord()
        x, y = coord[0], coord[1]
        return self.rotation(x, y)

    def action(self):
        if self._hp <= 0:
            return None
        else:
            self.handler_event_to_move()
            return self.handler_event_to_rotation()

    def get_damage(self):
        self.get_dmg(self.player.hit())
        if self._hp < 0:
            del self

    def give_damage(self):
        self.player.get_dmg(self._dmg)
