import pygame


# Player class
class Player :
    def __init__(self):
        self.pos = 1
    
    def updatePos(self, x):
        if (x + self.pos) > 6:
            self.pos = ( x + self.pos ) % 6 
        else:
            self.pos += x
    
    def draw(self, screen, color, rect):
        pygame.draw.rect(screen, color, rect)