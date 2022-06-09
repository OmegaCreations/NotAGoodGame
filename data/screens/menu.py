import pygame
from ..tools import Button


def menu(running) :

    # menu's initial vars
    bg_color = "#2b2d42"
    clock = pygame.time.Clock()

    # simmilar setup to game.py __init__ function
    screen = pygame.display.set_mode((720, 640))
    pygame.display.set_caption('NotAGoodGame')
    pygame.display.set_icon(pygame.image.load('./data/img/icon.jpg'))

    # elements
    button1 = Button("Play", 200, 40, (260, 300), 6, "./data/fonts/VT323/VT323-Regular.ttf")

    while running:
        pygame.event.get()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

        # background ----------------------
        screen.fill(bg_color)

        # buttons -------------------------
        button1.draw(screen)
        # check if button's animation ended
        if button1.animated():
            return False


        pygame.display.update()
        clock.tick(60)