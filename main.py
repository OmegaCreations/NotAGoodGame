import pygame
import random
from pygame.locals import *


screen = pygame.display.set_mode((240, 640))
score = 0
player_pos = 1
game_speed = 5
bg_color = (241, 250, 238)
walls_color = (29, 53, 87)
player_color = (230, 57, 70)
wall_arr = [
    0,
    40,
    80,
    120,
    160,
    200
]

# update player position
def updatePlayerPos(x):
    global player_pos
    if (x + player_pos) > 6:
        player_pos = ( x + player_pos ) % 6 
    else:
        player_pos += x
    
    print(player_pos)


# wall object class
class Wall :
    def __init__(self, start_pos):
        global wall_arr, wall_pos
        self.pos = start_pos
        self.walls = wall_arr.copy()
        self.action(True)

    def action(self, pop):
        if pop == True:
            try:
                self.walls = wall_arr.copy()
                x = random.randint(0, 5)
                self.walls.pop(x)
            except Exception as e: print(e)
        else:
            try:
                return self.walls
            except Exception as e: print(e)
    
    def move(self):
        global score, game_speed
        if self.pos >= 680:
            score += 1
            self.pos = -40
            self.action(True)
        # SPEED ADJUSTMENT ----------------------------------------------------------------------
        game_speed += 0.005
        self.pos += game_speed

wall_1 = Wall(-40)
wall_2 = Wall(-360)

# game run
running = True
game = True
frame = 0

pygame.font.init()
font = pygame.font.SysFont(None, 32)


while running:
    while game:
        frame += 1
        if frame == 60: 
            wall_1.move()
            wall_2.move()
        if frame > 80: frame = 0

        screen.fill(bg_color)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == KEYDOWN:
                if event.key == K_1:
                    updatePlayerPos(1)
                if event.key == K_2:
                    updatePlayerPos(2)
                if event.key == K_3:
                    updatePlayerPos(3)
                
        player = pygame.draw.rect(screen, player_color, (40*(player_pos-1), 600, 40, 40))
        score_text = font.render(f'SCORE: {str(score)}', True, (69, 123, 157))
        screen.blit(score_text, (100, 30))

        for n in range(len(wall_1.action(False))):
            pygame.draw.rect(screen, walls_color, (wall_1.action(False)[n], wall_1.pos, 40, 40))
            pygame.draw.rect(screen, walls_color, (wall_2.action(False)[n], wall_2.pos, 40, 40))
            if 40*(player_pos-1) == wall_1.action(False)[n] and (wall_1.pos > 560 and wall_1.pos < 640):
                game = False
            elif 40*(player_pos-1) == wall_2.action(False)[n] and (wall_2.pos > 560 and wall_2.pos < 640):
                game = False

        pygame.display.update()

    font = pygame.font.SysFont(None, 24)
    print(score)
    if score <=2:
        text = "ALE LAMUS XDDD"
    elif score > 2 and score <= 6:
        text = "4LATEK BY TO ZROBIL"
    elif score > 6 and score <= 10:
        text = "UJDZIE W TLUMIE"
    elif  score > 10:
        text = "DAMN BABY YOU KILLIN IT"
    score_text = font.render(f'{text}', True, player_color)
    screen.blit(score_text, (20, 300))
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.display.update()

pygame.quit()