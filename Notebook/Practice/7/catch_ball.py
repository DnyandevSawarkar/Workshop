import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Balls")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Basket properties
BASKET_WIDTH, BASKET_HEIGHT = 100, 20
basket_x = WIDTH // 2 - BASKET_WIDTH // 2
basket_y = HEIGHT - BASKET_HEIGHT - 10
basket_speed = 10

# Ball properties
BALL_RADIUS = 10
ball_speed = 5
balls = []

# Game loop control
clock = pygame.time.Clock()
run = True

def create_ball():
    x = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS)
    y = -BALL_RADIUS
    return [x, y]

def draw_window():
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLUE, (basket_x, basket_y, BASKET_WIDTH, BASKET_HEIGHT))
    for ball in balls:
        pygame.draw.circle(WIN, RED, (ball[0], ball[1]), BALL_RADIUS)
    pygame.display.update()

while run:
    clock.tick(30)  # 30 FPS

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Control basket movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x - basket_speed > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x + basket_speed + BASKET_WIDTH < WIDTH:
        basket_x += basket_speed

    # Create a new ball periodically
    if random.randint(1, 20) == 1:
        balls.append(create_ball())

    # Update ball positions and check for collisions
    for ball in balls[:]:
        ball[1] += ball_speed
        if ball[1] > HEIGHT:
            balls.remove(ball)
        # Check if ball collides with the basket
        if (basket_x < ball[0] < basket_x + BASKET_WIDTH) and (basket_y < ball[1] + BALL_RADIUS < basket_y + BASKET_HEIGHT):
            balls.remove(ball)

    draw_window()

pygame.quit()
sys.exit()
