import pygame
from pygame.locals import *
import time, math

pygame.font.init()
MAIN_FONT = pygame.font.SysFont("comicsans", 44)


def scale_image(img, factor=None):  # Used to scale an image
    if factor is None:
        factor = 1
    if isinstance(img, int):  # Check if img is an integer
        size = round(img * factor), round(img)  # Assuming scaling factor applies only to width
        return size
    else:
        size = round(img.get_width() * factor), round(img.get_height() * factor)
        return pygame.transform.scale(img, size)


GREEN_CAR = scale_image(pygame.image.load("Imagery/green-car.png"), 0.55)


def rotate_image(win, image, top_left, angle):  # Fyi literally the same fucking function as `blit_rotate_center`
    rotate_image = pygame.transform.rotate(image, angle)
    new_rect = rotate_image.get_rect(center=image.get_rect(topleft = top_left).center)
    win.blit(rotate_image, new_rect.topleft)


def blit_text_center(win, font, text):  # Used to display texts on the screen independent of the Button Class
    render = font.render(text, 1, (200, 200, 200))
    win.blit(render, (win.get_width()/2 - render.get_width() /
                      2, win.get_height()/2 - render.get_height()/2))


def get_font(size):  # Only used by the main menu
    return pygame.font.Font("imagery/font.ttf", size)


def draw(win, images, player_car, player2_or_computer_car, game_info, map_height):  # Animate the screen
    for img, pos in images:
        win.blit(img, pos)

    level_text = MAIN_FONT.render(
        f"Level {game_info.level}", 1, (255, 255, 255))
    win.blit(level_text, (10, map_height - level_text.get_height() - 70))

    time_text = MAIN_FONT.render(
        f"Time: {game_info.get_level_time()}s", 1, (255, 255, 255))
    win.blit(time_text, (10, map_height - time_text.get_height() - 40))

    vel_text = MAIN_FONT.render(
        f"Vel: {round(player_car.vel, 1)}px/s", 1, (255, 255, 255))
    win.blit(vel_text, (10, map_height - vel_text.get_height() - 10))

    player_car.draw(win)
    player2_or_computer_car.draw(win)
    pygame.display.update()


# These two are for movement animations
def move_player(player_car):
    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()
    if keys[pygame.K_s]:
        moved = True
        player_car.move_backward()

    if not moved:
        player_car.reduce_speed()

def move_player2(player2_car):
    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_LEFT]:
        player2_car.rotate(left=True)
    if keys[pygame.K_RIGHT]:
        player2_car.rotate(right=True)
    if keys[pygame.K_UP]:
        moved = True
        player2_car.move_forward()
    if keys[pygame.K_DOWN]:
        moved = True
        player2_car.move_backward()

    if not moved:
        player2_car.reduce_speed()


def handle_collision(player_car, player2_or_bot_car, game_info, level_mask, FINISH_POSITION, FINISH_MASK, screen, players_option):
    if player_car.collide(level_mask) != None:
        player_car.bounce()
    if players_option == 2:
        if player2_or_bot_car.collide(level_mask) != None:
            player2_or_bot_car.bounce()

    computer_finish_poi_collide = player2_or_bot_car.collide(
        FINISH_MASK, *FINISH_POSITION)
    if computer_finish_poi_collide != None:
        if players_option == 1:
            blit_text_center(screen, MAIN_FONT, "You lost!")
            pygame.display.update()
            pygame.time.wait(5000)
            game_info.reset()
            player_car.reset()
            player2_or_bot_car.reset()
        elif players_option == 2:
            if computer_finish_poi_collide[1] == 0:
                player2_or_bot_car.bounce()
            else:
                game_info.next_level()
                player2_or_bot_car.reset()
                player_car.reset()
                blit_text_center(screen, MAIN_FONT, "Player 2 won!")

    player_finish_poi_collide = player_car.collide(
        FINISH_MASK, *FINISH_POSITION)
    if player_finish_poi_collide != None:
        if player_finish_poi_collide[1] == 0:
            player_car.bounce()
        else:
            game_info.next_level()
            player2_or_bot_car.reset()
            player_car.reset()
            if players_option == 1:
                player2_or_bot_car.next_level(game_info.level)


#   #   #   #   #   CLASSES     #   #   #   #   #


class Button():  # Used to create both displayable and text-replaced images that can be pressed with the left mouse button
    def __init__(self, image, pos, text_input, font, base_color, hovering_color) -> None:
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        if self.font is not None:
            self.base_color, self.hovering_color = base_color, hovering_color
            self.text_input = text_input
            self.text = self.font.render(self.text_input, True, self.base_color)
            if self.image is None:
                self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        if self.font is not None:
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):  # Puts an image and its text on the screen
        if self.font is not None:
            if self.image is None:
                screen.blit(self.image, self.rect)
            screen.blit(self.text, self.text_rect)
        else:
            screen.blit(self.image, self.rect)

    def checkForInput(self, position):  # Checks if we're clicking on it
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):  # If we hover over the button, its color changes as an indicator
        if self.font is not None:
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                self.text = self.font.render(self.text_input, True, self.hovering_color)
            else:
                self.text = self.font.render(self.text_input, True, self.base_color)


class GameInfo:  # Determine time-based facts in the game (next level, reset, game finished, start level, level time)
    LEVELS = 10

    def __init__(self, level=1):
        self.level = level
        self.started = False
        self.level_start_time = 0

    def next_level(self):
        self.level += 1
        self.started = False

    def reset(self):
        self.level = 1
        self.started = False
        self.level_start_time = 0

    def game_finished(self):
        return self.level > self.LEVELS

    def start_level(self):
        self.started = True
        self.level_start_time = time.time()

    def get_level_time(self):
        if not self.started:
            return 0
        return round(time.time() - self.level_start_time)


class AbstractCar:
    def __init__(self, max_vel, rotation_vel, img, start_pos):
        self.img = img
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.start_pos = start_pos
        self.x, self.y = self.start_pos
        self.acceleration = 0.5

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        rotate_image(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi

    def reset(self):
        self.x, self.y = self.start_pos
        self.angle = 0
        self.vel = 0


class PlayerCar(AbstractCar):
    def __init__(self, max_vel, rotation_vel, img=None, start_pos=(250, 150)):
        super().__init__(max_vel, rotation_vel, img, start_pos)

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def bounce(self):
        self.vel = -self.vel
        self.move()


class ComputerCar(AbstractCar):
    def __init__(self, max_vel, rotation_vel, path=[], img=GREEN_CAR, start_pos=(270, 150)):
        super().__init__(max_vel, rotation_vel, img, start_pos)
        self.path = path
        self.current_point = 0
        self.vel = max_vel

    def draw_points(self, win):
        for point in self.path:
            pygame.draw.circle(win, (255, 0, 0), point, 5)

    def draw(self, win):
        super().draw(win)
        # self.draw_points(win)

    def calculate_angle(self):
        target_x, target_y = self.path[self.current_point]
        x_diff = target_x - self.x
        y_diff = target_y - self.y

        if y_diff == 0:
            desired_radian_angle = math.pi / 2
        else:
            desired_radian_angle = math.atan(x_diff / y_diff)

        if target_y > self.y:
            desired_radian_angle += math.pi

        difference_in_angle = self.angle - math.degrees(desired_radian_angle)
        if difference_in_angle >= 180:
            difference_in_angle -= 360

        if difference_in_angle > 0:
            self.angle -= min(self.rotation_vel, abs(difference_in_angle))
        else:
            self.angle += min(self.rotation_vel, abs(difference_in_angle))

    def update_path_point(self):
        target = self.path[self.current_point]
        rect = pygame.Rect(
            self.x, self.y, self.img.get_width(), self.img.get_height())
        if rect.collidepoint(*target):
            self.current_point += 1

    def move(self):
        if self.current_point >= len(self.path):
            return

        self.calculate_angle()
        self.update_path_point()
        super().move()

    def next_level(self, level):
        self.reset()
        self.vel = self.max_vel + (level - 1) * 0.5
        self.current_point = 0


class Camera:
    def __init__(self, target, WIDTH, HEIGHT):
        self.target = target
        self.width = WIDTH
        self.height = HEIGHT

    def apply(self, target_rect):
        return target_rect.move(-self.target.x + self.width // 2, -self.target.y + self.height // 2)
