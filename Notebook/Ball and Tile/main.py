import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ball and Tile Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
paddle_image = pygame.image.load('paddle.png')
ball_image = pygame.image.load('ball.png')
brick_image = pygame.image.load('brick.png')
cracked_brick_image = pygame.image.load('cracked_brick.png')
solid_brick_image = pygame.image.load('solid_brick.png')
powerup_life_image = pygame.image.load('powerup_life.png')
powerup_multiplier_image = pygame.image.load('powerup_multiplier.png')
powerup_bigball_image = pygame.image.load('powerup_bigball.png')

# Classes for game objects
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = paddle_image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT - 50
        self.speed = 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < SCREEN_WIDTH - self.rect.width:
            self.rect.x += self.speed

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ball_image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.speed_x = 5 * random.choice((1, -1))
        self.speed_y = -5
        self.big = False

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off the walls
        if self.rect.x <= 0 or self.rect.x >= SCREEN_WIDTH - self.rect.width:
            self.speed_x = -self.speed_x
        if self.rect.y <= 0:
            self.speed_y = -self.speed_y

        # If the ball hits the bottom, it is lost
        if self.rect.y >= SCREEN_HEIGHT:
            self.kill()

class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, hit_points=1):
        super().__init__()
        self.hit_points = hit_points
        self.images = [brick_image, cracked_brick_image, solid_brick_image]
        self.image = self.images[min(hit_points - 1, len(self.images) - 1)]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def hit(self):
        self.hit_points -= 1
        if self.hit_points > 0:
            self.image = self.images[min(self.hit_points - 1, len(self.images) - 1)]
        else:
            self.kill()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.type = type
        if type == 'life':
            self.image = powerup_life_image
        elif type == 'multiplier':
            self.image = powerup_multiplier_image
        elif type == 'bigball':
            self.image = powerup_bigball_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()

# Initialize sprites
all_sprites = pygame.sprite.Group()
balls = pygame.sprite.Group()
bricks = pygame.sprite.Group()
powerups = pygame.sprite.Group()

paddle = Paddle()
all_sprites.add(paddle)

# Create initial ball
ball = Ball()
all_sprites.add(ball)
balls.add(ball)

# Function to create bricks for a level
def create_level(level):
    for row in range(5):
        for col in range(10):
            if level == 1:
                brick = Brick(col * (brick_image.get_width() + 10) + 35, row * (brick_image.get_height() + 10) + 35)
            elif level == 2:
                hit_points = 1 if random.random() < 0.5 else 2
                brick = Brick(col * (brick_image.get_width() + 10) + 35, row * (brick_image.get_height() + 10) + 35, hit_points)
            elif level == 3:
                hit_points = random.choice([1, 2, 3])
                brick = Brick(col * (brick_image.get_width() + 10) + 35, row * (brick_image.get_height() + 10) + 35, hit_points)
            all_sprites.add(brick)
            bricks.add(brick)

create_level(1)

# Game variables
lives = 3
score = 0
level = 1
max_lives = 5

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game objects
    all_sprites.update()

    # Ball and paddle collision
    for ball in balls:
        if pygame.sprite.collide_rect(ball, paddle):
            ball.speed_y = -ball.speed_y

    # Ball and brick collision
    hits = pygame.sprite.groupcollide(balls, bricks, False, False)
    for ball, hit_bricks in hits.items():
        for brick in hit_bricks:
            score += 10
            brick.hit()
            ball.speed_y = -ball.speed_y
            # Chance to drop a power-up
            if random.random() < 0.1:
                powerup_type = random.choice(['life', 'multiplier', 'bigball'])
                powerup = PowerUp(brick.rect.x, brick.rect.y, powerup_type)
                all_sprites.add(powerup)
                powerups.add(powerup)

    # Power-up and paddle collision
    powerup_hits = pygame.sprite.spritecollide(paddle, powerups, True)
    for powerup in powerup_hits:
        if powerup.type == 'life' and lives < max_lives:
            lives += 1
        elif powerup.type == 'multiplier':
            # Create additional ball
            new_ball = Ball()
            new_ball.rect.x, new_ball.rect.y = paddle.rect.center
            all_sprites.add(new_ball)
            balls.add(new_ball)
        elif powerup.type == 'bigball':
            for ball in balls:
                ball.image = pygame.transform.scale(ball_image, (ball.rect.width * 2, ball.rect.height * 2))
                ball.rect = ball.image.get_rect(center=ball.rect.center)

    # Check if any balls are left
    if len(balls) == 0:
        lives -= 1
        if lives > 0:
            # Create new ball
            new_ball = Ball()
            all_sprites.add(new_ball)
            balls.add(new_ball)
        else:
            # Game over
            running = False

    # Check if all bricks are destroyed
    if len(bricks) == 0:
        level += 1
        if level > 3:
            # Game completed
            running = False
        else:
            create_level(level)

    # Draw everything
    screen.fill(BLACK)
    all_sprites.draw(screen)
    
    # Display score and lives
    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(text, (10, 10))
    text = font.render(f'Lives: {lives}', True, WHITE)
    screen.blit(text, (10, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
