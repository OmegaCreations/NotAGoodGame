import pygame
from pygame.locals import *
from data.game import Game
from data.walls import Wall
from data.player import Player
from data.tools import draw_rect_alpha
from pygame import mixer
import os



# setup
game = Game()
player = Player()
wall_1 = Wall(-40)
wall_2 = Wall(-360)

def restart():
    global game, player, wall_1, wall_2
    game = Game()
    player = Player()
    wall_1 = Wall(-40)
    wall_2 = Wall(-360)


running = True
pygame.font.init()
font = pygame.font.SysFont("inkfree", 18)

pygame.mixer.init()


def inGame():
    global running
    school_img = pygame.image.load(f"./data/img/school.jpg").convert()

    while game.ingame:
        if not pygame.mixer.music.get_busy():
            game.changeMusic()

        # walls move
        wall_1.move()
        wall_2.move()
                
        # background setup
        game.screen.fill(game.bg_color)
        draw_rect_alpha(game.screen, (168, 218, 220, 127), (0, 600, 240, 40))

        # center character on bg img
        if wall_1.pos == 670 or wall_2.pos == 670:
            game.score += 1 # adding score after every wall
            game.reloadImage()

        # right side images
        game.screen.blit(school_img, (240, 0))
        game.screen.blit(game.bg_image, (480 - (game.bg_size[0] // 2), 320 - (game.bg_size[1] // 2)))

        
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.ingame = False
                running = False
            
            if event.type == KEYDOWN:
                if event.key == K_1:
                    player.updatePos(1)
                if event.key == K_2:
                    player.updatePos(2)
                if event.key == K_3:
                    player.updatePos(3)
        
        # player draw
        player.draw(game.screen, game.player_color, (40*(player.pos-1), 600, 40, 40))
        
        # score
        score_text = font.render(f'SCORE: {str(game.score)}', True, (69, 123, 157))
        game.screen.blit(score_text, (100, 30))


        # walls draw
        for n in range(len(wall_1.action(False))):
            pygame.draw.rect(game.screen, game.walls_color, (wall_1.action(False)[n], wall_1.pos, 40, 40))
            pygame.draw.rect(game.screen, game.walls_color, (wall_2.action(False)[n], wall_2.pos, 40, 40))

            # collide check
            if 40*(player.pos-1) == wall_1.action(False)[n] and (wall_1.pos > 560 and wall_1.pos < 640):
                game.ingame = False
                game.playSound("gameover")

            elif 40*(player.pos-1) == wall_2.action(False)[n] and (wall_2.pos > 560 and wall_2.pos < 640):
                game.ingame = False
                game.playSound("gameover")
                


        pygame.display.update()
        game.clock.tick(60) # 60 fps


while running:
    
    if game.ingame:
        inGame()

    draw_rect_alpha(game.screen, (45, 52, 54, 127), (0, 0, 240, 640))
    
    score_text = font.render(f'Press "0" to restart game', True, game.player_color)
    game.screen.blit(score_text, (20, 150))
    

    end_img = pygame.image.load(f"./data/img/gameover.png").convert_alpha()
    end_img = pygame.transform.scale(end_img, (208, 202))
    game.screen.blit(end_img, (20, 200))

    score_text = font.render(f'SCORE: {str(game.score)}', True, (255, 255, 255))
    game.screen.blit(score_text, (100, 30))

    end_text = font.render(f'You got distracted, didn\'t you?', True, (255, 255, 255))
    game.screen.blit(end_text, (5, 425))

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_0:
                    restart()
    pygame.display.update()

pygame.quit()