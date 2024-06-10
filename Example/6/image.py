import pygame
import os

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the window
pygame.display.set_caption("Image Display")

# Load the image
image_path = os.path.join("image.jpg")  # Replace "example_image.png" with the name of your image file
image = pygame.image.load(image_path)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a white background
    screen.fill((255, 255, 255))

    # Blit the image onto the screen
    screen.blit(image, (0, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
