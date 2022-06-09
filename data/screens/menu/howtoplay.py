import pygame
from ...tools import Button

def howToPlay():
    # initial vars
    running = True
    bg_color = "#2b2d42"
    clock = pygame.time.Clock()

    # simmilar setup to game.py __init__ function
    screen = pygame.display.set_mode((720, 640))
    pygame.display.set_caption('How to play')
    pygame.display.set_icon(pygame.image.load('./data/img/icon.jpg'))

    # font
    pygame.font.init() # initiate fonts
    gui_font = pygame.font.Font("./data/fonts/VT323/VT323-Regular.ttf", 32)
    text1 = gui_font.render(f'Click, the "play" button in main menu.', True, "#ffffff")

    # elements -------------------------------------------------------------------------------------
    # back button
    button1 = Button("<", 40, 40, (20, 20), 6, "./data/fonts/VT323/VT323-Regular.ttf", 4)

    while running:
        pygame.event.get()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
        
        # background ----------------------
        screen.fill(bg_color)
        
        # buttons -------------------------
        button1.draw(screen)

        # texts
        text_rect = text1.get_rect(center=(360, 100)) # center text
        screen.blit(text1, text_rect)

        # go back to menu
        if button1.animated():
            running = False 


        
        pygame.display.update()
        clock.tick(60)