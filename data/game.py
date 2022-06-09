import pygame
import random

# Game class
class Game:
    def __init__(self):
        # initials
        self.screen = pygame.display.set_mode((720, 640)) # resolution
        pygame.display.set_caption('NotAGoodGame') # window title
        pygame.display.set_icon(pygame.image.load('./data/img/icon.jpg')) # window icon

        # character scaling data
        self.backgrounds = {
            1 : (326, 432),
            2 : (291, 512),
            3 : (386, 534),
            4 : (378, 494),
            5 : (201, 369),
            6 : (298, 581),
            7 : (346, 617),
            8 : (471, 512),
            9 : (385, 387)
        }
        self.current_img = 1 # current character image
        # import character image
        self.bg_image = pygame.image.load(f"./data/img/bg_{str(self.current_img)}.png").convert_alpha()
        # scale image with self.backgrounds data
        self.bg_image = pygame.transform.scale(self.bg_image, self.backgrounds[self.current_img])
        # background image size (for centering images in main.py)
        self.bg_size = [self.bg_image.get_width(), self.bg_image.get_height()]


        # sounds and music -------------------
        # background musics data
        self.music = [
            './data/music/1.mp3',
            './data/music/2.mp3'
        ]
        # current music
        self.current_music = 0

        # gameover sounds
        self.sound_gameover = [
            './data/music/gameover/araara.mp3'
        ]
        
        # score sounds
        self.sound_score = [
            './data/music/score/gj.mp3',
            './data/music/score/nepu.mp3',
            './data/music/score/omg.mp3',
            './data/music/score/sugoi.mp3',
        ]

        # game initials ----------------------
        # game score
        self.score = 0
        
        # if in game
        self.ingame = True

        # game speed vars --------------------
        self.game_speed = 2
        self.speed_incr = 0.002

        # coloring ---------------------------
        self.bg_color = (239, 239, 239)
        self.walls_color = (29, 53, 87)
        self.player_color = (230, 57, 70)

        # clock setup
        self.clock = pygame.time.Clock()

    # change character image and play score sound
    def reloadImage(self):
        # change image after every 5 points
        if self.score % 5 == 0 and self.score != 0:
                if self.current_img != len(self.backgrounds):
                    self.current_img += 1
                else:
                    self.current_img = 1
                # update current image values
                self.bg_image = pygame.image.load(f"./data/img/bg_{str(self.current_img)}.png").convert_alpha()
                self.bg_image = pygame.transform.scale(self.bg_image, self.backgrounds[self.current_img])
                self.bg_size = [self.bg_image.get_width(), self.bg_image.get_height()]
        
        # play score sound every 10 points
        if self.score % 10 == 0 and self.score != 0:
            self.playSound("score")

    # change music
    def changeMusic(self):
        if self.current_music != len(self.music):
            self.current_music += 1
        else:
            self.current_music = 1

        pygame.mixer.music.load(self.music[self.current_music - 1])
        pygame.mixer.music.set_volume(0.08) # change music volume
        pygame.mixer.music.play()
    
    # play sounds
    def playSound(self, par):
        
        # game over sounds
        if par == "gameover":
            gameover = pygame.mixer.Sound(self.sound_gameover[0])
            gameover.set_volume(0.1)
            gameover.play()

        # score sounds
        elif par == "score":
            sound = random.randint(0, len(self.sound_score) - 1)
            score = pygame.mixer.Sound(self.sound_score[sound])
            score.set_volume(0.1)
            score.play()
       

