import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Animation")

# Set up ball variables
ball_radius = 20
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_vel_x, ball_vel_y = 5, 5

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Game loop
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(60)  # 60 FPS

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update ball position
    ball_x += ball_vel_x
    ball_y += ball_vel_y

    # Bounce ball off the walls
    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
        ball_vel_x = -ball_vel_x
    if ball_y - ball_radius < 0 or ball_y + ball_radius > HEIGHT:
        ball_vel_y = -ball_vel_y

    # Redraw display
    WIN.fill(WHITE)  # Fill window with white color
    pygame.draw.circle(WIN, RED, (ball_x, ball_y), ball_radius)  # Draw ball
    pygame.display.update()

pygame.quit()
sys.exit()
