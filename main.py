# imports
import pygame
from pygame.locals import *
from data.game import Game
from data.walls import Wall
from data.player import Player
from data.screens.menu.menu import menu
from data.tools import draw_rect_alpha, rect_surf, Animator
from data.screens.gameover import gameover

# TODO clean up code and ??move inGame function to another file?



# basic setup
game = Game()
player = Player()
wall_1 = Wall(-40)
wall_2 = Wall(-360)

running = True # main loop run
pygame.font.init() # initiate fonts
font = pygame.font.SysFont("./data/fonts/VT323/VT323-Regular.tff", 24)
pygame.mixer.init() # initiate pygame mixer for music playing

# game restart function -----------------
def restart():
    global game, player, wall_1, wall_2
    game = Game()
    player = Player()
    wall_1 = Wall(-40)
    wall_2 = Wall(-360)

# in game function ------------------------------------------------------------------------------------------
# screen is being initialized in Game() class (game.py)
def inGame():

    # main vars
    global running
    school_img = pygame.image.load(f"./data/img/school.jpg").convert() # bg image for characters

    # key sprites
    key01_state_1 = pygame.image.load(f"./data/img/keys/01-state-1.png").convert_alpha()
    key01_state_1 = pygame.transform.scale(key01_state_1, (120, 120))
    key01_state_2 = pygame.image.load(f"./data/img/keys/01-state-2.png").convert_alpha()
    key01_state_2 = pygame.transform.scale(key01_state_2, (120, 120))
    key_one_sprites = [key01_state_1, 
                       key01_state_2
    ]

    key02_state_1 = pygame.image.load(f"./data/img/keys/02-state-1.png").convert_alpha()
    key02_state_1 = pygame.transform.scale(key02_state_1, (120, 120))
    key02_state_2 = pygame.image.load(f"./data/img/keys/02-state-2.png").convert_alpha()
    key02_state_2 = pygame.transform.scale(key02_state_2, (120, 120))
    key_two_sprites = [key02_state_1, 
                       key02_state_2
    ]

    key03_state_1 = pygame.image.load(f"./data/img/keys/03-state-1.png").convert_alpha()
    key03_state_1 = pygame.transform.scale(key03_state_1, (120, 120))
    key03_state_2 = pygame.image.load(f"./data/img/keys/03-state-2.png").convert_alpha()
    key03_state_2 = pygame.transform.scale(key03_state_2, (120, 120))
    key_three_sprites = [key03_state_1, 
                         key03_state_2
    ]

    key01 = Animator(key_one_sprites, game.screen, 280, 520, 5)
    key02 = Animator(key_two_sprites, game.screen, 150, 220, 5)
    key03 = Animator(key_three_sprites, game.screen, 225, 220, 5)


    # in game loop
    while game.ingame:

        # check if music is already playing
        if not pygame.mixer.music.get_busy():
            game.changeMusic() # change music (game.py)

        # walls movement (walls.py)
        wall_2.move(game.speed_incr, game.game_speed) 
        game.speed_incr, game.game_speed = wall_1.move(game.speed_incr, game.game_speed) # update vars 
    
                
        # background setup
        game.screen.fill(game.bg_color) # game background
        draw_rect_alpha(game.screen, (34, 36, 53, 127), (0, 595, 240, 5)) # player movement background

        # center character on bg img
        if wall_1.pos >= 680 or wall_2.pos >= 680:
            game.score += 1 # adding score after every wall
            game.reloadImage() # change character image

        # right side images
        game.screen.blit(school_img, (240, 0)) # character background
         # center character image
        game.screen.blit(game.bg_image, (480 - (game.bg_size[0] // 2), 320 - (game.bg_size[1] // 2)))

        if key01.pressed:
            key01.animate()


        # events
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                game.ingame = False
                running = False
            
            # player movement keys
            if event.type == KEYDOWN:
                if event.key == K_1:
                    player.updatePos(1)
                    key01.pressed = True
                if event.key == K_2:
                    player.updatePos(2)
                if event.key == K_3:
                    player.updatePos(3)
        
        # player draw
        player.draw(game.screen, game.player_color, (40*(player.pos-1), 600, 40, 40))
        
        # current score text
        score_text = font.render(f'SCORE: {str(game.score)}', True, "#e9eaec")
        text_rect = score_text.get_rect(center=(120, 50))
        game.screen.blit(score_text, text_rect)


        # walls draw
        for n in range(len(wall_1.action(False))):
            pygame.draw.rect(game.screen, game.walls_color, (wall_1.action(False)[n], wall_1.pos, 40, 40))
            pygame.draw.rect(game.screen, game.walls_color, (wall_2.action(False)[n], wall_2.pos, 40, 40))

            # walls blends
            game.screen.blit(rect_surf(size = 48, color = (15,27,44)), (wall_2.action(False)[n], wall_2.pos), special_flags =BLEND_RGB_ADD)
            game.screen.blit(rect_surf(size = 48, color = (15,27,44)), (wall_1.action(False)[n], wall_1.pos), special_flags =BLEND_RGB_ADD)

            # collide check
            if 40*(player.pos-1) == wall_1.action(False)[n] and (wall_1.pos > 560 and wall_1.pos < 640):
                game.ingame = False
                game.playSound("gameover")

            elif 40*(player.pos-1) == wall_2.action(False)[n] and (wall_2.pos > 560 and wall_2.pos < 640):
                game.ingame = False
                game.playSound("gameover")
                


        pygame.display.update()
        game.clock.tick(60) # 60 fps

menu_running = True # player is in menu
while running:

    # menu
    if menu_running == True:
        menu_running = menu(menu_running) # update menu status
    
    # in game
    if game.ingame:
        inGame()

    # change screen after game over
    menu_action = gameover(game.screen, game.score, font)
    if menu_action == "restart":
        restart()
    elif menu_action == "menu":
        menu()
    
    pygame.display.update()

pygame.quit()