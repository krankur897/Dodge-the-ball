import pygame
import random
import tkinter as tk
from tkinter import simpledialog


root = tk.Tk()

root.withdraw()

player_name = simpledialog.askstring("Player Name", "Enter your name:")


if not player_name:
    player_name = "Unknown Player"

root.destroy()
pygame.init()

SCREEN_WIDTH = 800

SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dodge Game - Pandit ji Edition")

# Colors of ball
light_orange = (247, 197, 142)

light_brown = (217, 160, 104)

BLACK = (0, 0, 0)

# Fonts design
font = pygame.font.Font(None, 36)

title_font = pygame.font.Font(None, 72)

player_img = pygame.image.load("Pandit.jpg").convert_alpha()

player_img = pygame.transform.scale(player_img, (50, 50))
bell_img = pygame.image.load("Bell.jpg").convert_alpha()

bell_img = pygame.transform.scale(bell_img, (40, 40))

player_rect = player_img.get_rect()

player_rect.centerx = SCREEN_WIDTH // 2

player_rect.bottom = SCREEN_HEIGHT - 10

player_speed = 7

balls = []

ball_speed = 5

ball_frequency = 20 
score = 0
def create_ball():

    x = random.randrange(0, SCREEN_WIDTH - 40)

    rect = pygame.Rect(x, -40, 40, 40)

    balls.append(rect)

def draw_player():

    screen.blit(player_img, player_rect)

def draw_balls():

    for ball in balls:
        screen.blit(bell_img, (ball.x, ball.y))

def move_balls():

    global score, ball_speed
    if score > 50:
        ball_speed = 7

    if score > 100:
        ball_speed = 9

    if score > 150:
        ball_speed = 12
    for i in reversed(range(len(balls))):
        balls[i].y += ball_speed

        if balls[i].y > SCREEN_HEIGHT:
            balls.pop(i)

            score += 1

def check_collision():

    for ball in balls:#loop for ball

        if player_rect.colliderect(ball):

            return True
        
    return False #give return

def display_score():

    text = font.render(f"Score: {score}", True, BLACK)

    screen.blit(text, (10, 10))

screen.fill(light_orange)

start_text = title_font.render("LET'S BEGIN!", True, BLACK)

start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

screen.blit(start_text, start_rect)

pygame.display.flip()

pygame.time.delay(2000)

running = True
clock = pygame.time.Clock()

ball_timer = 0

game_over = False

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.left > 0:

            player_rect.x -= player_speed


        if keys[pygame.K_RIGHT] and player_rect.right < SCREEN_WIDTH:

            player_rect.x += player_speed


        ball_timer += 1 #increase
        if ball_timer % ball_frequency == 0:

            create_ball()

        move_balls()
        if check_collision():

            game_over = True
    screen.fill(light_orange)
    pygame.draw.rect(screen, light_brown, (0, SCREEN_HEIGHT // 1.4, SCREEN_WIDTH, SCREEN_HEIGHT))

    if not game_over:

        draw_player()
        draw_balls()
        display_score()
    else:
        ohshit = title_font.render("OH SHIT!", True, BLACK)
        score_final = font.render(f"Final Score: {score}", True, BLACK)
        name_tag = font.render(f"Player: {player_name}", True, BLACK)

        screen.blit(ohshit, (SCREEN_WIDTH//2 - 120, SCREEN_HEIGHT//2 - 60))
        screen.blit(score_final, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 10))
        screen.blit(name_tag, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

with open("scores.txt", "a") as f:
    f.write(f"{player_name} : {score}\n")

print("Score saved successfully!")