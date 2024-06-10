import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move Shapes with Keyboard")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Shapes and their positions
shapes = [
    {"type": "circle", "pos": [200, 300], "radius": 30, "color": RED},
    {"type": "square", "pos": [400, 300], "size": 60, "color": BLUE},
    {"type": "triangle", "pos": [600, 300], "size": 60, "color": GREEN}
]

selected_shape = None

# Game loop
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(60)  # 60 FPS

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for shape in shapes:
                if shape["type"] == "circle":
                    dx = mouse_x - shape["pos"][0]
                    dy = mouse_y - shape["pos"][1]
                    if dx * dx + dy * dy <= shape["radius"] * shape["radius"]:
                        selected_shape = shape
                        break
                elif shape["type"] == "square":
                    x, y = shape["pos"]
                    size = shape["size"]
                    if x - size // 2 <= mouse_x <= x + size // 2 and y - size // 2 <= mouse_y <= y + size // 2:
                        selected_shape = shape
                        break
                elif shape["type"] == "triangle":
                    x, y = shape["pos"]
                    size = shape["size"]
                    if x - size // 2 <= mouse_x <= x + size // 2 and y - size // 2 <= mouse_y <= y + size // 2:
                        selected_shape = shape
                        break

        elif event.type == pygame.KEYDOWN and selected_shape is not None:
            if event.key == pygame.K_LEFT:
                selected_shape["pos"][0] -= 5
            elif event.key == pygame.K_RIGHT:
                selected_shape["pos"][0] += 5
            elif event.key == pygame.K_UP:
                selected_shape["pos"][1] -= 5
            elif event.key == pygame.K_DOWN:
                selected_shape["pos"][1] += 5

    # Redraw display
    WIN.fill(WHITE)  # Fill window with white color

    for shape in shapes:
        if shape["type"] == "circle":
            pygame.draw.circle(WIN, shape["color"], shape["pos"], shape["radius"])
        elif shape["type"] == "square":
            x, y = shape["pos"]
            size = shape["size"]
            pygame.draw.rect(WIN, shape["color"], (x - size // 2, y - size // 2, size, size))
        elif shape["type"] == "triangle":
            x, y = shape["pos"]
            size = shape["size"]
            points = [
                (x, y - size // 2),
                (x - size // 2, y + size // 2),
                (x + size // 2, y + size // 2)
            ]
            pygame.draw.polygon(WIN, shape["color"], points)

    pygame.display.update()

pygame.quit()
sys.exit()
