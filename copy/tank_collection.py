from tank import randint
from tank import Tank
import world

_tanks = []
_canvas = None


def initialize(canv):
    global _canvas
    _canvas = canv
    player = Tank(canvas=canv, x=100, y=50, ammo=100, speed=1, bot=False)
    enemy = Tank(canvas=canv, x=300, y=300, ammo=100, speed=1, bot=True)
    neutral = Tank(canvas=canv, x=300, y=300, ammo=100, speed=1, bot=False)
    neutral.stop()
    enemy.set_target(player)

    _tanks.append(player)
    _tanks.append(enemy)
    print(_tanks)


def get_player():
    return _tanks[0]


def update():
    for tank in _tanks:
        tank.update()
        check_collisions(tank)

def check_collisions(tank):
    for other_tank in _tanks:
        if tank == other_tank:
            continue
        if tank.intersects(other_tank):
            return True
        return False


def spawn_enemy():
    while True:
       pos_x = randint(200, 800)
       pos_y  = randint(200, 800)


    t = Tank(_canvas, x=pos_x, y=pos_y, speed=1)
    if not check_collisions(t):
        t.set_target(get_player())
        _tanks.append(t)
        return True


