import pygame
pygame.init()

class Player:
    def __init__(self):
        self.image = pygame.Surface((16, 16))  # Create Player Image
        self.image.fill(colors["RED"])  # Fill Player Red
        self.rect = pygame.Rect((50, 50), (16, 16))  # Create Player Rect
        self.speed = 8  # Initial speed
        self.rotation_speed = 3
        self.direction = 0
        self.slow_timer = 5  # Timer to track how long the player should be slowed down

    def move(self, camera_pos, oil_rect):
        pos_x, pos_y = camera_pos  # Split camera_pos

        key = pygame.key.get_pressed()  # Get Keyboard Input

        if self.slow_timer > 0:
            self.slow_timer -= 1
            self.speed *= 0.8  # Reduce speed when in the oil
        else:
            self.speed = 8  # Reset speed if the slow timer is over

        if key[pygame.K_w]:
            self.rect.y -= self.speed  # Move Player Rect Coord
            pos_y += self.speed  # Move Camera Coord Against Player Rect
        if key[pygame.K_a]:
            self.rect.x -= self.speed
            pos_x += self.speed
        if key[pygame.K_s]:
            self.rect.y += self.speed
            pos_y -= self.speed
        if key[pygame.K_d]:
            self.rect.x += self.speed
            pos_x -= self.speed

        self.direction %= 360  # Keep direction in the range [0, 360)

        # Check if the player is in the oil puddle
        if self.rect.colliderect(oil_rect):
            self.slow_timer = 30  # Set the slow timer to 30 frames (adjust as needed)

        # ... Rest of your collision and boundary checking code ...

        return (pos_x, pos_y)  # Return New Camera Pos

    def render(self, display):
        rotated_image = pygame.transform.rotate(self.image, self.direction)
        display.blit(rotated_image, (self.rect.x, self.rect.y))


def Main(display, clock):
    world = pygame.Surface((1000, 1000))  # Create Map Surface
    world.fill(colors["BLACK"])  # Fill Map Surface Black
    for x in range(10):
        pygame.draw.rect(world, colors["BLUE"], ((x * 100, x * 100), (20, 20)))  # Put Blue Rectangles On Map Surface

    player = Player()  # Initialize Player Class
    camera_pos = (192, 192)  # Create Camera Starting Position

    oil_rect = pygame.Rect(300, 200, 15, 15)  # Oil puddle rect

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        camera_pos = player.move(camera_pos, oil_rect)  # Run Player Move Function And Return New Camera Pos

        display.fill(colors["WHITE"])  # Fill The Background White To Avoid Smearing
        world.fill(colors["BLACK"])  # Refresh The World So The Player Doesn't Smear
        for x in range(10):
            pygame.draw.rect(world, colors["BLUE"], ((x * 100, x * 100), (20, 20)))

        pygame.draw.rect(world, colors["GREEN"], ((120, 120), (20, 20)))  # Put Blue Rectangles On Map Surface
        pygame.draw.rect(world, colors["BROWN"], oil_rect)  # Draw oil puddle

        player.render(world)  # Render The Player
        display.blit(world, camera_pos)  # Render Map To The Display

        pygame.display.flip()


if __name__ in "__main__":
    display = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Scrolling Camera")
    clock = pygame.time.Clock()

    colors = {
        "WHITE": (255, 255, 255),
        "RED": (255, 0, 0),
        "GREEN": (0, 255, 0),
        "BLUE": (0, 0, 255),
        "BLACK": (0, 0, 0),
        "BROWN": (139, 69, 19),  # Brown color for oil puddle
    }

    Main(display, clock)  # Run Main Loop
