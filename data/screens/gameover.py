import pygame
from data.tools import draw_rect_alpha, Button
from pygame.locals import *

# game over screen
def gameover(screen, score, font):
    # TODO make fullscreen gameover 
    draw_rect_alpha(screen, (45, 52, 54, 127), (0, 0, 240, 640))
    
    # restart text TODO make animated button for better graphic presentation
    restart_text = font.render(f'Press "0" to restart game', True, (255, 255, 255))
    screen.blit(restart_text, (20, 150))

    # gameover image
    end_img = pygame.image.load(f"./data/img/gameover.png").convert_alpha()
    end_img = pygame.transform.scale(end_img, (208, 202))
    screen.blit(end_img, (20, 200))

    # score TODO save score to database
    score_text = font.render(f'SCORE: {str(score)}', True, (255, 255, 255))
    screen.blit(score_text, (100, 30))

    # gameover texts
    end_text = font.render(f'You got distracted, didn\'t you?', True, (255, 255, 255))
    screen.blit(end_text, (5, 425))

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == KEYDOWN:
                # restart if pressed 0
                if event.key == K_0:
                    return "restart"