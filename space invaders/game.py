import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1800, 1000

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Title and Icon
pygame.display.set_caption("Space Invaders")

# Load images
background = pygame.image.load('sky.jpg')
player_img = pygame.image.load('player.png')
player_bullet_img = pygame.image.load('player_bullet.png')
enemy_img = pygame.image.load('enemy.png')
enemy_bullet_img = pygame.image.load('enemy_bullet.png')

# Load fonts
font = pygame.font.Font(None, 36)

class Player:
    def __init__(self):
        self.image = player_img
        self.x = WIDTH // 2
        self.y = HEIGHT - 100
        self.x_change = 0
        self.lives = 3

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x += self.x_change

        # Boundary checking
        if self.x <= 0:
            self.x = 0
        elif self.x >= WIDTH - self.image.get_width():
            self.x = WIDTH - self.image.get_width()

class Bullet:
    def __init__(self, x, y, image, speed):
        self.image = image
        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.y += self.speed

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class Enemy:
    def __init__(self, x, y):
        self.image = enemy_img
        self.x = x
        self.y = y
        self.x_change = 2  # Reduced speed
        self.y_change = 40

    def move(self):
        self.x += self.x_change
        if self.x <= 0 or self.x >= WIDTH - self.image.get_width():
            self.x_change *= -1
            self.y += self.y_change

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

def is_collision(entity1, entity2):
    distance = math.sqrt((entity1.x - entity2.x)**2 + (entity1.y - entity2.y)**2)
    return distance < 27

def show_score(x, y):
    score_display = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_display, (x, y))

def show_level(x, y):
    level_display = font.render(f"Level: {level}", True, (255, 255, 255))
    screen.blit(level_display, (x, y))

def show_lives(x, y):
    lives_display = font.render(f"Lives: {player.lives}", True, (255, 255, 255))
    screen.blit(lives_display, (x, y))

# Game variables
player = Player()
player_bullets = []
enemies = []
enemy_bullets = []
enemy_count = 10
level = 1
score = 0
game_over = False

# Create enemies
for _ in range(enemy_count):
    x = random.randint(0, WIDTH - enemy_img.get_width())
    y = random.randint(50, 150)
    enemies.append(Enemy(x, y))

# Main game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x_change = -5
            if event.key == pygame.K_RIGHT:
                player.x_change = 5
            if event.key == pygame.K_SPACE:
                player_bullets.append(Bullet(player.x + player.image.get_width() // 2, player.y, player_bullet_img, -10))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.x_change = 0

    player.move()
    player.draw()

    for bullet in player_bullets:
        bullet.move()
        bullet.draw()
        if bullet.y < 0:
            player_bullets.remove(bullet)

    for enemy in enemies:
        enemy.move()
        enemy.draw()
        
        # Enemy shooting bullets
        if random.randint(0, 100) < 2 and len(enemy_bullets) < 2:
            enemy_bullets.append(Bullet(enemy.x + enemy.image.get_width() // 2, enemy.y, enemy_bullet_img, 5))
        
        if is_collision(player, enemy):
            player.lives -= 1
            enemies.remove(enemy)
            if player.lives == 0:
                game_over = True

        for bullet in player_bullets:
            if is_collision(bullet, enemy):
                try:
                    player_bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1
                except ValueError:
                    pass

    for bullet in enemy_bullets:
        bullet.move()
        bullet.draw()
        if bullet.y > HEIGHT:
            enemy_bullets.remove(bullet)
        if is_collision(player, bullet):
            player.lives -= 1
            enemy_bullets.remove(bullet)
            if player.lives == 0:
                game_over = True

    if not enemies:
        level += 1
        enemy_count += 5
        for _ in range(enemy_count):
            x = random.randint(0, WIDTH - enemy_img.get_width())
            y = random.randint(50, 150)
            enemies.append(Enemy(x, y))

    show_score(10, 10)
    show_level(10, 40)
    show_lives(10, 70)

    pygame.display.update()

    if game_over:
        print(f"Game Over! Final Score: {score}")
        running = False
