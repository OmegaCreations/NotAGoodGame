import random


# wall object class
class Wall :
    def __init__(self, start_pos):
        # wall initial vars
        self.wall_arr = [0, 40, 80, 120, 160, 200] # 6 rect position of a wall
        self.pos = start_pos # wall starting y-pos
        self.walls = self.wall_arr.copy() 
        self.action(True)

    # pop one block from wall randomly --------------
    def action(self, pop):
        if pop == True:
            try:
                self.walls = self.wall_arr.copy()
                x = random.randint(0, 5)
                self.walls.pop(x)
            except Exception as e: print(e)
        else:
            try:
                return self.walls
            except Exception as e: print(e)
    
    # move wall function ----------------------------
    def move(self, incr, gamespeed):
        if self.pos >= 680:
            self.pos = -40
            self.action(True)
        # SPEED ADJUSTMENT --------------------------
        gamespeed += incr
        self.pos += gamespeed

        return incr, gamespeed