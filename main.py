import pygame
from pygame.locals import *
import sys, time, math
from utils_and_classes import *
from menu_and_buttons import Menu


level1_path = [(430, 280), (480,190), (530, 190), (600, 290), (620, 440), (660, 580), (710, 610), (800, 650), 
               (820, 700), (930, 710), (960, 655), (960, 190), (970, 120), (1054, 160), (990, 230), (1130, 380),
               (1080, 500), (1050, 590), (1200, 800), (1200, 880), (1010, 810), (860, 770), (660, 830), (530, 880),
               (480, 805), (600, 660), (570, 510), (480, 300)]

level2_path = [(650, 350), (720, 440), (700, 610), (750, 660), (790, 580), (740, 130), (800, 80), (895, 150), (960, 300), (975, 440), (1110, 670), (1200, 780), (1120, 820),
               (1025, 700), (860, 800), (950, 910), (850, 930), (660, 700), (590, 420), (660, 350), (710, 480),
               (720, 650), (800, 650), (740, 130)]

level3_path = [(350, 100), (450, 200), (550, 140), (850, 420), (1000, 380), (1200, 310), (1450, 430), (1280, 600),
               (1050, 530), (1060, 630), (420, 610), (390, 510), (280, 500), (220, 200)]

level4_path = [(530, 460), (330, 410), (335, 310), (450, 190), (570, 300), (650, 360), (670, 280), (650, 150), (730, 210),
               (830, 430), (1000, 540), (1225, 500), (1330, 600), (1500, 580), (1400, 700), (580, 680), (550, 500)]

# Cars
RED_CAR = scale_image(pygame.image.load("Imagery/red-car.png"), 0.6)
GREEN_CAR = scale_image(pygame.image.load("Imagery/green-car.png"), 0.6)
WHITE_CAR = scale_image(pygame.image.load("Imagery/White_car.png"), 0.6)

# (CAR) OBJECTS
game_info = GameInfo()


#   #   #   #   #       MENU FUNCTIONS      #   #   #   #   #

def main_menu(screen, BACKGROUND):  # Main Menu Screen
    pygame.display.set_caption("Menu")
    program_running = True

    while program_running:

        pygame.display.update()
        screen.blit(BACKGROUND, (0, 0))  # Background color

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TXT.get_rect(center=(640, 260))
        
        screen.blit(MENU_TXT, MENU_RECT)

        for button in [
            obj_menu.QUIT_BUTTON, obj_menu.OPTIONS_BUTTON, obj_menu.PLAY_BUTTON
            ]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # If a said button is clicked
                if obj_menu.PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play_screen()
                if obj_menu.OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pass
                if obj_menu.QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

#

def play_screen():  # Play Screen

    while True:

        pygame.display.update()
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        screen.fill("BLACK")

        PLAY_TXT = get_font(45).render("This is the PLAY screen.", True, "WHITE")
        PLAY_RECT = PLAY_TXT.get_rect(center=(640, 260))
        screen.blit(PLAY_TXT, PLAY_RECT)

        for button in [
            obj_menu.BACK_BUTTON, obj_menu.ONE_PLAYER_OPTION_BUTTON, obj_menu.TWO_PLAYER_OPTION_BUTTON
            ]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if obj_menu.BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    main_menu(screen, GRASS)
                if obj_menu.ONE_PLAYER_OPTION_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    level_select(1)
                if obj_menu.TWO_PLAYER_OPTION_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    level_select(2)

#

def level_select(players_amount):

    while True:

        pygame.display.update()
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        screen.fill("GRAY")  # The grass is always greener on the other side :)

        PLAY_TXT = get_font(45).render("Choose your map/circuit/level", True, "WHITE")
        PLAY_RECT = PLAY_TXT.get_rect(center=(640, 260))
        screen.blit(PLAY_TXT, PLAY_RECT)

        for button in [
            obj_menu.BACK_BUTTON, obj_menu.LEVEL1, obj_menu.LEVEL2, obj_menu.LEVEL3, obj_menu.LEVEL4
                       ]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if obj_menu.BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    play_screen()
                if obj_menu.LEVEL1.checkForInput(PLAY_MOUSE_POS):
                    width, height = obj_menu.level1.get_width(), obj_menu.level1.get_height()
                    pygame.display.set_mode((width, height))
                    play_game(players_amount, obj_menu.level1, obj_menu.level1_borders, width, height)
                if obj_menu.LEVEL2.checkForInput(PLAY_MOUSE_POS):
                    width, height = obj_menu.level2.get_width(), obj_menu.level2.get_height()
                    pygame.display.set_mode((width, height))
                    play_game(players_amount, obj_menu.level2, obj_menu.level2_borders, width, height)
                if obj_menu.LEVEL3.checkForInput(PLAY_MOUSE_POS):
                    width, height = obj_menu.level3.get_width(), obj_menu.level3.get_height()
                    pygame.display.set_mode((width, height))
                    play_game(players_amount, obj_menu.level3, obj_menu.level3_borders, width, height)
                if obj_menu.LEVEL4.checkForInput(PLAY_MOUSE_POS):
                    width, height = obj_menu.level4.get_width(), obj_menu.level4.get_height()
                    pygame.display.set_mode((width, height))
                    play_game(players_amount, obj_menu.level4, obj_menu.level4_borders, width, height)

#   #   #   #  #    ACTUAL PLAY_GAME FUNCTION      #   #   #   #   #

def play_game(players_option, circuit, circuit_borders, c_width, c_height):
    run = True
    clock = pygame.time.Clock()

    if circuit == obj_menu.level1:
        player_car = PlayerCar(4, 4, RED_CAR, (470, 420))
        player2_car = PlayerCar(4, 4, WHITE_CAR, (500, 420))
        computer_car = ComputerCar(2, 4, level1_path, GREEN_CAR, (500, 420))

        FINISH = scale_image(pygame.image.load("Imagery/finish.png"), 1.8)
        FINISH_MASK = pygame.mask.from_surface(FINISH)
        FINISH_POSITION = (400, 490)
    elif circuit == obj_menu.level2:
        player_car = PlayerCar(4, 4, RED_CAR, (630, 380))
        player2_car = PlayerCar(4, 4, WHITE_CAR, (600, 380))
        computer_car = ComputerCar(2, 4, level2_path, GREEN_CAR, (600, 380))

        FINISH = scale_image(pygame.image.load("Imagery/finish.png"), 0.9)
        FINISH_MASK = pygame.mask.from_surface(FINISH)
        FINISH_POSITION = (570, 440)  # Adjust later
    elif circuit == obj_menu.level3:
        player_car = PlayerCar(4, 4, RED_CAR, (220, 150))
        player2_car = PlayerCar(4, 4, WHITE_CAR, (190, 150))
        computer_car = ComputerCar(2, 4, level3_path, GREEN_CAR, (190, 150))

        FINISH = scale_image(pygame.image.load("Imagery/finish.png"), 1)
        FINISH_MASK = pygame.mask.from_surface(FINISH)
        FINISH_POSITION = (180, 200)  # Adjust later
    elif circuit == obj_menu.level4:
        player_car = PlayerCar(4, 4, RED_CAR, (560, 575))
        player2_car = PlayerCar(4, 4, WHITE_CAR, (585, 575))
        computer_car = ComputerCar(2, 4, level4_path, GREEN_CAR, (585, 575))

        FINISH = scale_image(pygame.image.load("Imagery/finish.png"), 1.5)
        FINISH_MASK = pygame.mask.from_surface(FINISH)
        FINISH_POSITION = (470, 630)  # Adjust later

    images = [(GRASS, (0, 0)), (circuit, (0, 0)),
        (FINISH, FINISH_POSITION), (circuit_borders, (0, 0))]
    camera = Camera(player_car, c_width, c_height)

    if players_option == 1:
        player2_or_bot_car = computer_car
    elif players_option == 2:
        player2_or_bot_car = player2_car

    while run:
        pygame.init()
        clock.tick(FPS)

        draw(screen, images, player_car, player2_or_bot_car, game_info, c_height)

        while not game_info.started:
            blit_text_center(
                screen, MAIN_FONT, f"Press any key to start level {game_info.level}!")
            pygame.display.update()

            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            for button in [
                obj_menu.PAUSE_BUTTON
                        ]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if obj_menu.PAUSE_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        pause_screen(players_option, circuit, circuit_borders, c_width, c_height)

                if event.type == pygame.KEYDOWN:
                    game_info.start_level()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if obj_menu.PAUSE_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    pause_screen(players_option, circuit, circuit_borders, c_width, c_height)

        if run:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            for button in [
                obj_menu.PAUSE_BUTTON
                        ]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if obj_menu.PAUSE_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        pause_screen(players_option, circuit, circuit_borders, c_width, c_height)

            move_player(player_car)
            if players_option == 1:
                player2_or_bot_car.move()
            elif players_option == 2:
                move_player2(player2_or_bot_car)

            circuit_mask = pygame.mask.from_surface(circuit_borders)
            handle_collision(player_car, player2_or_bot_car, game_info, circuit_mask, FINISH_POSITION, FINISH_MASK, screen)

            if game_info.game_finished():
                blit_text_center(screen, MAIN_FONT, "You won the game!")
                pygame.time.wait(5000)
                game_info.reset()
                player_car.reset()
                player2_or_bot_car.reset()

    pygame.quit()


def pause_screen(players_option, circuit, circuit_borders, c_width, c_height):  # NOT WORKING YET, WOULD RELOAD THE GAME INSTEAD OF RESUMING

    while True:

        pygame.display.update()
        PAUSE_MOUSE_POS = pygame.mouse.get_pos()
        screen.fill("BLACK")

        for button in [
            obj_menu.BACK_BUTTON, obj_menu.RESUME_BUTTON
        ]:
            button.changeColor(PAUSE_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if obj_menu.BACK_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                    main_menu(screen, GRASS)
                if obj_menu.RESUME_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                    play_game(players_option, circuit, circuit_borders, c_width, c_height)


if __name__ == '__main__':
    pygame.font.init()

    # Colors
    colors = {
    "WHITE":(255,255,255),
    "RED"  :(255,0,0),
    "GREEN":(0,255,0),
    "BLUE" :(0,0,255),
    "BLACK":(0,0,0),
    "GREY":(127, 127, 127)
    }

    MAIN_FONT = pygame.font.SysFont("comicsans", 44)

    # Screen and background
    window = width, height = (1700, 960)
    screen = pygame.display.set_mode(window)
    GRASS = scale_image(pygame.image.load("Imagery/Grass1.png"), 1.5)
    pygame.display.set_caption("Racing gimma")

    FPS = 60

    pygame.display.set_caption("Racing Game!")

    obj_menu = Menu(window)
    main_menu(screen, GRASS)
