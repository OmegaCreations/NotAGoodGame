import pygame
import random

# Game class
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((720, 640))
        pygame.display.set_caption('NotAGoodGame')
        pygame.display.set_icon(pygame.image.load('./data/img/icon.jpg'))

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
        self.current_img = 7
        self.bg_image = pygame.image.load(f"./data/img/bg_{str(self.current_img)}.png").convert_alpha()
        self.bg_image = pygame.transform.scale(self.bg_image, self.backgrounds[self.current_img])
        self.bg_size = [self.bg_image.get_width(), self.bg_image.get_height()]

        self.music = [
            './data/music/1.mp3',
            './data/music/2.mp3'
        ]
        self.current_music = 1

        self.sound_gameover = [
            './data/music/gameover/araara.mp3'
        ]
        
        self.sound_score = [
            './data/music/score/gj.mp3',
            './data/music/score/nepu.mp3',
            './data/music/score/omg.mp3',
            './data/music/score/sugoi.mp3',
        ]

        self.score = 0
        self.ingame = True
        self.game_speed = 7
        self.bg_color = (241, 250, 238)
        self.walls_color = (29, 53, 87)
        self.player_color = (230, 57, 70)
        self.clock = pygame.time.Clock()

    def reloadImage(self):
        if self.score % 5 == 0 and self.score != 0:
                print("change!")
                if self.current_img != len(self.backgrounds):
                    self.current_img += 1
                else:
                    self.current_img = 1
                print(self.current_img)
                self.bg_image = pygame.image.load(f"./data/img/bg_{str(self.current_img)}.png").convert_alpha()
                self.bg_image = pygame.transform.scale(self.bg_image, self.backgrounds[self.current_img])
                self.bg_size = [self.bg_image.get_width(), self.bg_image.get_height()]
        
        if self.score % 10 == 0 and self.score != 0:
            self.playSound("score")


    def changeMusic(self):
        if self.current_music != len(self.music):
            self.current_music += 1
        else:
            self.current_music = 1

        pygame.mixer.music.load(self.music[self.current_music - 1])
        pygame.mixer.music.play()
    
    def playSound(self, par):

        if par == "gameover":
            gameover = pygame.mixer.Sound(self.sound_gameover[0])
            gameover.play()

        elif par == "score":
            sound = random.randint(0, len(self.sound_score) - 1)
            score = pygame.mixer.Sound(self.sound_score[sound])
            score.play()
       

