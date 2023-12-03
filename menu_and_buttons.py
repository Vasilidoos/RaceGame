import pygame, time, math, sys
from pygame.locals import *
from utils_and_classes import *
#

# https://www.youtube.com/watch?v=GMBqjxcKogA
# https://www.youtube.com/watch?v=L3ktUWfAMPg

pygame.font.init()

# Colors
global colors
colors = {
"WHITE":(255,255,255),
"RED"  :(255,0,0),
"GREEN":(0,255,0),
"BLUE" :(0,0,255),
"BLACK":(0,0,0),
"GREY":(127, 127, 127)
}


class Menu:
    def __init__(self, window):
        # Buttons
        self.window = window
        self.BACK_BUTTON = Button(image=scale_image(pygame.image.load("Imagery/Back_button1.png"), 0.3), pos=(200, 600),
                        text_input="BACK", font=get_font(75), base_color="GREY", hovering_color="WHITE")
        self.QUIT_BUTTON = Button(image=scale_image(pygame.image.load("Imagery/Quit_button1.png"), 0.3), pos=(360, 600),
                        text_input="QUIT", font=get_font(75), base_color="GREY", hovering_color="WHITE")
        self.OPTIONS_BUTTON = Button(image=scale_image(pygame.image.load("Imagery/Options_button1.png"), 0.3), pos=(360, 400),
                        text_input="OPTIONS", font=get_font(75), base_color="GREY", hovering_color="WHITE")
        self.PLAY_BUTTON = Button(image=scale_image(pygame.image.load("Imagery/Play_button1.png"), 0.3), pos=(360, 200),
                        text_input="PLAY", font=get_font(75), base_color="GREY", hovering_color="WHITE")
        self.PAUSE_BUTTON = Button(image=scale_image(pygame.image.load("Imagery/Pause_button1.png"), 0.5), pos=(30, 30),
                        text_input="PLAY", font=None, base_color="GREY", hovering_color="WHITE")
        self.RESUME_BUTTON = Button(image=scale_image(pygame.image.load("Imagery/Resume_button1.png"), 0.3), pos=(1000, 600),
                        text_input="RESUME", font=get_font(75), base_color="GREY", hovering_color="WHITE")
        self.ONE_PLAYER_OPTION_BUTTON = Button(image=scale_image(pygame.image.load("Imagery/One_player_button1.png"), 0.4), pos=(800, 400),
                                    text_input="One player", font=get_font(75), base_color="GREY", hovering_color="WHITE")
        self.TWO_PLAYER_OPTION_BUTTON = Button(image=scale_image(pygame.image.load("Imagery/Two_player_button1.png"), 0.4), pos=(800, 600),
                                    text_input="Two player", font=get_font(75), base_color="GREY", hovering_color="WHITE")
        # Level buttons
        self.LEVEL1 = Button(image=scale_image(pygame.image.load("Imagery/Circuit2_level.png"), 0.1), pos=(500, 400),
                                text_input="Level1", font=None, base_color="GREY", hovering_color="WHITE")
        self.LEVEL2 = Button(image=scale_image(pygame.image.load("Imagery/Circuit3_level.png"), 0.1), pos=(640, 400),
                                text_input="Level2", font=None, base_color="GREY", hovering_color="WHITE")
        self.LEVEL3 = Button(image=scale_image(pygame.image.load("Imagery/Circuit4_level.png"), 0.075), pos=(790, 400),
                                text_input="Level3", font=None, base_color="GREY", hovering_color="WHITE")
        self.LEVEL4 = Button(image=scale_image(pygame.image.load("Imagery/Circuit5_level.png"), 0.05), pos=(930, 400),
                                text_input="Level4", font=None, base_color="GREY", hovering_color="WHITE")

        # Level maps
        self.level1 = scale_image(pygame.image.load("Imagery/Circuit2.png"), 0.9)
        self.level2 = scale_image(pygame.image.load("Imagery/Circuit3.png"), 0.9)
        self.level3 = scale_image(pygame.image.load("Imagery/Circuit4.png"), 0.9)
        self.level4 = scale_image(pygame.image.load("Imagery/Circuit5.png"), 0.9)

        # Map borders
        self.level1_borders = scale_image(pygame.image.load("Imagery/Circuit2_borders.png"), 0.9)
        self.level2_borders = scale_image(pygame.image.load("Imagery/Circuit3_borders.png"), 0.9)
        self.level3_borders = scale_image(pygame.image.load("Imagery/Circuit4_borders.png"), 0.9)
        self.level4_borders = scale_image(pygame.image.load("Imagery/Circuit5_borders.png"), 0.9)
