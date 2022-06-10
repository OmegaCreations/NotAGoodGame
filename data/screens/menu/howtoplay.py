import pygame
from ...tools import Button, Animator, renderMultiLine


def howToPlay():
    # initial vars
    running = True
    bg_color = "#2b2d42"
    page = 0

    # simmilar setup to game.py __init__ function
    screen = pygame.display.set_mode((720, 640))
    pygame.display.set_caption('How to play')
    pygame.display.set_icon(pygame.image.load('./data/img/icon.jpg'))
    clock = pygame.time.Clock()

    # font
    pygame.font.init() # initiate fonts
    gui_font = pygame.font.Font("./data/fonts/VT323/VT323-Regular.ttf", 32)

    

    # elements -------------------------------------------------------------------------------------
    # texts
    text1 = gui_font.render(f'Click the "play" button in main menu.', True, "#ffffff")

    text2 = """Player is moving red square between 6 
possible positions.
Using buttons 1, 2 and 3 you are controlling 
an ammount of squares to move forward.
    """

    text3 = """For example: if you are on a 2nd position
and you press "2", you will end up 
on a 4th position. However, if you are 
on a 5th position and you press "3", 
you will go to 2nd position.
     """

    # back button
    button1 = Button("<", 40, 40, (20, 20), 6, "./data/fonts/VT323/VT323-Regular.ttf", 4)
    button3 = Button("<", 40, 40, (20, 20), 6, "./data/fonts/VT323/VT323-Regular.ttf", 4)
    # next page button
    button2 = Button(">", 40, 40, (660, 20), 6, "./data/fonts/VT323/VT323-Regular.ttf", 4)

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

    key01 = Animator(key_one_sprites, screen, 75, 220, 100)
    key02 = Animator(key_two_sprites, screen, 150, 220, 200)
    key03 = Animator(key_three_sprites, screen, 225, 220, 300)


    # main loop ------------------------------------------------------------------------------------
    while running:
        pygame.event.get()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
        
        # background ----------------------
        screen.fill(bg_color)
        

        # texts and buttons -----------------------------------------------------
        if page == 0:
            button1.draw(screen)
            button2.draw(screen)
            text_rect = text1.get_rect(center=(360, 100)) # center text
            screen.blit(text1, text_rect)
        elif page == 1:
            button3.draw(screen)
            renderMultiLine(text2, 70, 90, 32, screen, "#ffffff", gui_font)
            key01.animate()
            key02.animate()
            key03.animate()
            renderMultiLine(text3, 70, 320, 32, screen, "#ffffff", gui_font)

        # go back to menu
        if button1.animated():
            if page == 0:
                running = False 
        if button3.animated():
            page = 0
        if button2.animated():
            page = 1

        
        pygame.display.update()
        clock.tick(60)