import random
# wall object class
class Wall :
    def __init__(self, start_pos):
        self.wall_arr = [0, 40, 80, 120, 160, 200]
        self.pos = start_pos
        self.walls = self.wall_arr.copy()
        self.action(True)

    # pop one block from wall randomly
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
    
    # move wall
    def move(self):
        if self.pos >= 680:
            self.pos = -40
            self.action(True)
        # SPEED ADJUSTMENT ----------------------------------------------------------------------
        self.pos += 5