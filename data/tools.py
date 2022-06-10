import pygame

# drawing transparent rect ------------------------------------------------------------------------
def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)

# small lightning blend on rects ------------------------------------------------------------------
def rect_surf(size, color):
    surf = pygame.Surface((size * 2, size * 2))
    pygame.draw.rect(surf, color, (-6, -4, size, size))
    surf.set_colorkey((255, 255, 255))
    return surf


# button creator -----------------------------------------------------------------------------------
class Button():
    def __init__(self, text, width, height, pos, elevation, font, borderradius = 12):
        # core
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]
        self.clicked = False

        # sound
        self.hover_played = False

        # for animation
        self.last = pygame.time.get_ticks()
        self.cooldown = 600 

        # upper rect
        self.upper_rect = pygame.Rect(pos, (width, height))
        self.upper_color = '#475F77'
        self.borderradius = borderradius

        # bottom rect
        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_color = '#354B5E'

        # text
        pygame.font.init()
        gui_font = pygame.font.Font(font, 30)
        self.text_surf = gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.upper_rect.center)

    def draw(self, screen):
        # elevation
        self.upper_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.upper_rect.center

        self.bottom_rect.midtop = self.upper_rect.midtop
        self.bottom_rect.height = self.upper_rect.height + self.dynamic_elevation

        # rect draw
        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius= self.borderradius)
        pygame.draw.rect(screen, self.upper_color, self.upper_rect, border_radius= self.borderradius)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click() # check if btn clicked

    # button click checker ---------------------------------------
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        

        # if mouse hover
        if self.upper_rect.collidepoint(mouse_pos):
            # hover move and sound
            if not self.hover_played:
                hover = pygame.mixer.Sound('./data/music/other/button-hover.wav')
                hover.set_volume(0.1)
                hover.play()
                self.hover_played = True

                self.dynamic_elevation -= 1 # hover move

            # cursor change to pointer
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND) 

            # hover color
            self.upper_color = '#D74B4B'

            # check if button is clicked
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                # play animation once
                if self.pressed == True:
                    self.dynamic_elevation = self.elevation - 1
                    self.pressed = False
                    self.clicked = True
                    click = pygame.mixer.Sound('./data/music/other/button-click.wav')
                    click.set_volume(0.1)
                    click.play()
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            self.upper_color = '#475F77'
            self.clicked = False
            self.hover_played = False
            self.dynamic_elevation = self.elevation

    # button animation screen change delay -(possibilites for better screen animations)
    def animated(self):
        if self.clicked:
            now = pygame.time.get_ticks()
            if now - self.last >= self.cooldown:
                self.last = now
                return True # animation ended



# multilines text rendering ----------------------------------------------------------------------------
def renderMultiLine(text, x, y, fsize, screen, color, font):
        lines = text.splitlines()
        for i, l in enumerate(lines):
            screen.blit(font.render(l, 0, color), (x, y + fsize*i))


# animator ---------------------------------------------------------------------------------------------
# sprites is an array with images
# delay is a value in ticks between changing image
class Animator():
    def __init__(self, sprites, screen, x, y, delay = 0):
        # initial vars
        self.rect = (x, y)
        self.delay = delay
        self.screen = screen
        self.sprites = sprites
        self.last = pygame.time.get_ticks()
        self.current_sprite = 1
        self.sprites_num = len(sprites)

        self.pressed = False

    def animate(self):
        # draw sprite  
        self.screen.blit(self.sprites[self.current_sprite - 1], self.rect)

        # for delay
        now = pygame.time.get_ticks()

        # change current sprite
        if now - self.last >= self.delay:
            self.last = now

            if self.current_sprite == self.sprites_num:
                self.current_sprite = 0
            else:
                self.current_sprite += 1


        
    

