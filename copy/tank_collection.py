from tank import Tank
from random import randint
import world

_tank = []
_canvas = None


def initialize(canv):
    global _canvas
    _canvas = canv
    # player = Tank(canvas=canv, x = world.BLOCK_SIZE*2, y = world.BLOCK_SIZE*4, ammo=100, speed=1, bot=False)
    # enemy = Tank(canvas=canv, x = world.BLOCK_SIZE*4, y = world.BLOCK_SIZE*6, ammo=100, speed=1, bot=True)
    # enemy.set_target(player)
    #
    # _tank.append(player)
    # _tank.append(enemy)
    spawn(False)
    for i in range(5):
        spawn(True).set_target(get_player())

def get_player():
    return _tank[0]

def update():
    for tank in _tank:
        tank.update()
        check_collision(tank)

def check_collision(tank):
    for other_tank in _tank:
        if tank == other_tank:
            continue
        if tank.intersects(other_tank):
            return True
    return False







 def spawn(is_bot=True):
     cols = world.get_cols()
     rows = world.get_rows()
     while True:
         col = randint(1, cols-1)
         row = randint(1, rows-1)

         if world.get_block(col, row) != world.GROUND:
             continue

         t = Tank(_canvas,x=col*world.BLOCK_SIZE, y=row*world.BLOCK_SIZE, speed=2, bot=is_bot)
         if not check_collision(t):
             _tank.append(t)
             return t



