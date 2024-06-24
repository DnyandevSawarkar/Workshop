import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Nokia Snake Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GREEN = (144, 238, 144)
DARK_GREEN = (0, 100, 0)
RED = (255, 0, 0)

# Game variables
snake_block = 20
snake_speed = 6

# Font
font_style = pygame.font.SysFont(None, 35)

def draw_snake(snake_block, snake_list):
    for i, x in enumerate(snake_list):
        if i == 0:  # Head
            pygame.draw.circle(screen, DARK_GREEN, (x[0] + snake_block // 2, x[1] + snake_block // 2), snake_block // 2)
        elif i == len(snake_list) - 1:  # Tail
            tail_center = (x[0] + snake_block // 2, x[1] + snake_block // 2)
            pygame.draw.circle(screen, DARK_GREEN, tail_center, snake_block // 2)
            points = [
                (x[0], x[1] + snake_block // 2),
                (x[0] + snake_block // 2, x[1] + snake_block),
                (x[0] + snake_block, x[1] + snake_block // 2)
            ]
            pygame.draw.polygon(screen, DARK_GREEN, points)
        else:  # Body
            pygame.draw.rect(screen, LIGHT_GREEN, [x[0], x[1], snake_block, snake_block], border_radius=3)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])

def show_score(score):
    value = font_style.render("Score: " + str(score), True, WHITE)
    screen.blit(value, [10, 10])

def gameLoop():
    game_over = False
    game_close = False

    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    score = 0

    foodx = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 20.0) * 20.0

    clock = pygame.time.Clock()

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        x1 += x1_change
        y1 += y1_change

        # Wrap around the boundaries
        if x1 >= SCREEN_WIDTH:
            x1 = 0
        elif x1 < 0:
            x1 = SCREEN_WIDTH - snake_block
        if y1 >= SCREEN_HEIGHT:
            y1 = 0
        elif y1 < 0:
            y1 = SCREEN_HEIGHT - snake_block

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [foodx, foody, snake_block, snake_block], border_radius=3)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(snake_block, snake_List)
        show_score(score)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 20.0) * 20.0
            Length_of_snake += 1
            score += 10

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
