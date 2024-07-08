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

# Load NPC image
NPC_IMAGE = pygame.image.load(os.path.join('enemy.png'))

# Set up player variables
player_width, player_height = 50, 50
player_x, player_y = (WIDTH - player_width) // 2, (HEIGHT - player_height) // 2
player_vel = 5

# Set up NPC variables
npc_width, npc_height = 50, 50
npc_x, npc_y = (WIDTH - npc_width) // 2, 50
npc_vel = 3
npc_direction = 1  # 1 for moving right, -1 for moving left

# Game loop
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(30)  # FPS

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update player position based on pressed keys with move limits
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_vel
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_vel
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_vel
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_height:
        player_y += player_vel

    # Update NPC position
    npc_x += npc_vel * npc_direction

    # Reverse direction if NPC hits window bounds
    if npc_x <= 0:
        npc_direction = 1
    elif npc_x >= WIDTH - npc_width:
        npc_direction = -1

    # Redraw display
    WIN.fill((255, 255, 255))  # Fill window with white color
    WIN.blit(PLAYER_IMAGE, (player_x, player_y))  # Draw player
    WIN.blit(NPC_IMAGE, (npc_x, npc_y))  # Draw NPC
    pygame.display.update()

pygame.quit()
sys.exit()
