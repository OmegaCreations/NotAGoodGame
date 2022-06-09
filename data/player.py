import pygame

# TODO clean up code if possible
# add rect deform during move ?? 



# Player class
class Player :
    def __init__(self):
        # initial variables
        self.pos = 1 # position 1 to 6
        self.front = True # direction of player move

        # moving
        self.velocity = 1.0 # for speed animation
        self.starting_pos = 0 # position before
        self.actual_pos = 0 # actuall position (in px)
        self.end_pos = 0 # ending position to achieve


    # calculate nect position of player
    def updatePos(self, x):

        # if player will move backward
        if (x + self.pos) > 6:
            self.front = False
            self.pos = ( x + self.pos ) % 6 
            self.end_pos = 40*(self.pos-1)
        # if player will move forward
        else:
            self.front = True
            self.pos += x
            self.end_pos = 40*(self.pos-1)
    

    # moving player and animating movement
    def draw(self, screen, color, rect):
        # (40*(player.pos-1), 600, 40, 40)
        
        # check if player will move right or left (right --> self.front = True)
        if self.front:
            print(f"({self.starting_pos}, {self.actual_pos}, {self.end_pos})")
            if self.actual_pos < self.end_pos - 5:
                self.actual_pos += 4 + self.velocity
                
                # animation front ------------------------------------------------------------------
                # speed up until player hits most of the way
                if self.actual_pos < (self.end_pos // 2) + self.actual_pos and self.velocity <= 6: 
                    self.velocity += 1.5
                elif self.velocity >= 1.0: # to reduce too much slow
                    self.velocity -= 1.5
            

                pygame.draw.rect(screen, color, (self.actual_pos, 600, 40, 40))
            else:
                # setup variables for next move
                self.actual_pos = self.end_pos
                self.starting_pos = self.end_pos
                # draw on end posistion in case player isn't on end position after move
                pygame.draw.rect(screen, color, (self.actual_pos, 600, 40, 40))
                self.velocity = 1.0
        else:
            # print(f"({self.starting_pos}, {self.actual_pos}, {self.end_pos})")
            if self.actual_pos > self.end_pos + 5:
                self.actual_pos -= 2 + self.velocity
                
                # animation backwards --------------------------------------------------------------
                if self.actual_pos > (self.actual_pos //2) - (self.end_pos) and self.velocity <= 6:
                    self.velocity += 1.5
                elif self.velocity >= 1.0:
                    self.velocity -= 1.5
            
                pygame.draw.rect(screen, color, (self.actual_pos, 600, 40, 40))
            else:
                # setup variables for next move
                self.actual_pos = self.end_pos
                self.starting_pos = self.end_pos
                # draw on end posistion in case player isn't on end position after move
                pygame.draw.rect(screen, color, (self.actual_pos, 600, 40, 40)) 
                self.velocity = 1.0


        
        