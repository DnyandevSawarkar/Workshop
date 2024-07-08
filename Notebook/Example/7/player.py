import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 1800, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move Player with Keyboard")

# Load player image
PLAYER_IMAGE = pygame.image.load(os.path.join('player.png'))

# Load background image
BACKGROUND_IMAGE = pygame.image.load(os.path.join("sky.jpg")).convert()
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))

# Set up player variables
player_width, player_height = 50, 50
player_x, player_y = (WIDTH - player_width) // 2, (HEIGHT - player_height) // 2
player_vel = 5

# Game loop
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(30)  # FPS

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Update player position based on pressed keys with move limits
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_vel
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_vel
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_vel
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_height:
        player_y += player_vel

    # Redraw display
    # WIN.fill((255, 255, 255))  # Fill window with white color
    WIN.blit(BACKGROUND_IMAGE, (0, 0))  # Draw background
    WIN.blit(PLAYER_IMAGE, (player_x, player_y))  # Draw player
    pygame.display.update()

pygame.quit()
sys.exit()
