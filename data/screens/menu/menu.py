import pygame

from data.screens.menu.howtoplay import howToPlay
from ...tools import Button


def menu(running) :

    # menu's initial vars
    bg_color = "#2b2d42"
    clock = pygame.time.Clock()

    # simmilar setup to game.py __init__ function
    screen = pygame.display.set_mode((720, 640))
    pygame.display.set_caption('NotAGoodGame')
    pygame.display.set_icon(pygame.image.load('./data/img/icon.jpg'))
    pygame.font.init() # initiate fonts
    gui_font = pygame.font.Font("./data/fonts/VT323/VT323-Regular.ttf", 64)
    title = gui_font.render(f'NotAGoodGame', True, "#e9eaec")

    # elements -------------------------------------------------------------------------------------
    # play button
    button1 = Button("Play", 200, 40, (260, 210), 6, "./data/fonts/VT323/VT323-Regular.ttf")

    # how to play button
    button2 = Button("How to play? (do not)", 280, 40, (220, 300), 6, "./data/fonts/VT323/VT323-Regular.ttf")

    # about button
    button3 = Button("About NotAGoodGame", 280, 40, (220, 390), 6, "./data/fonts/VT323/VT323-Regular.ttf")

    while running:
        pygame.event.get()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

        # background ----------------------
        screen.fill(bg_color)

        # texts
        text_rect = title.get_rect(center=(360, 100)) # center text
        screen.blit(title, text_rect)

        # buttons -------------------------
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)

        # check if button's animation ended -----------
        # go into game
        if button1.animated():
            return False 
        
        # go to - how to play loop
        if button2.animated():
            howToPlay()


        pygame.display.update()
        clock.tick(60)