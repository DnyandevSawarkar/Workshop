import pygame
import os

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 1080, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Bird Animation")

# Load background image
BACKGROUND_IMAGE = pygame.image.load(os.path.join("sky.jpg")).convert()
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))


# Load bird images
BIRD_IMAGES = [pygame.image.load(os.path.join(f'{i}.jpg')) for i in range(1, 9)]
bird_index = 0

# Set bird position and velocity
bird_rect = BIRD_IMAGES[0].get_rect(center=(WIDTH // 2, HEIGHT // 2))
bird_vel = 5

# Game loop
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(30)  # FPS

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    # Update bird position
    bird_rect.x -= bird_vel
    # Check if bird is out of the screen on the right side
    if bird_rect.right > WIDTH:
        bird_rect.left = 0  # Move bird to the left side
    # Check if bird is out of the screen on the left side
    elif bird_rect.left < 0:
        bird_rect.right = WIDTH  # Move bird to the right side
    # Bird animation
    bird_index = (bird_index + 1) % len(BIRD_IMAGES)

    # Redraw display
    WIN.blit(BACKGROUND_IMAGE, (0, 0))  # Draw background

    WIN.blit(BIRD_IMAGES[bird_index], bird_rect)  # Draw bird
    pygame.display.update()

pygame.quit()
