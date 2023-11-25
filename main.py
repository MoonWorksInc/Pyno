import pygame
import random
import sys
import os

pygame.init()

sourceFileDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(sourceFileDir)


WIDTH, HEIGHT = 1200, 600
GROUND_HEIGHT = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pyno Game")

dinosaur_img = pygame.image.load('assets/dino.png')
cactus_img = pygame.image.load('assets/cactus.png')

dinosaur_img = pygame.transform.scale(dinosaur_img, (50, 50))
cactus_img = pygame.transform.scale(cactus_img, (30, 50))

font = pygame.font.Font(None, 36)

dinosaur_x = 50
dinosaur_y = HEIGHT - GROUND_HEIGHT - dinosaur_img.get_height()
dinosaur_vel_y = 0
gravity = 1
jump_height = -15
ground_y = HEIGHT - GROUND_HEIGHT
cacti = []
score = 0

def reset_game():
    global dinosaur_x, dinosaur_y, dinosaur_vel_y, score, cacti, gravity
    dinosaur_x = 50
    dinosaur_y = HEIGHT - GROUND_HEIGHT - dinosaur_img.get_height()
    dinosaur_vel_y = 0
    gravity = 1
    jump_height = -15
    ground_y = HEIGHT - GROUND_HEIGHT
    cacti = []
    score = 0

reset_game()

def draw_ground():
    pygame.draw.rect(screen, BLACK, (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))

def draw_dinosaur():
    screen.blit(dinosaur_img, (dinosaur_x, dinosaur_y))

def draw_cacti():
    for cactus in cacti:
        screen.blit(cactus_img, (cactus[0], ground_y - cactus_img.get_height()))

def draw_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def game_over():
    game_over_text = font.render("Game Over - Click to Restart", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - 180, HEIGHT // 2 - 30))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    reset_game()
                    waiting = False

def main():
    global dinosaur_y, dinosaur_vel_y, score

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.MOUSEBUTTONDOWN and dinosaur_y == ground_y - dinosaur_img.get_height():
                    dinosaur_vel_y = jump_height

        dinosaur_vel_y += gravity
        dinosaur_y += dinosaur_vel_y

        if dinosaur_y >= ground_y - dinosaur_img.get_height():
            dinosaur_y = ground_y - dinosaur_img.get_height()
            dinosaur_vel_y = 0

        if len(cacti) == 0 or cacti[-1][0] < WIDTH - 300:
            cacti.append([WIDTH, random.randint(10, 50)])

        for cactus in cacti:
            cactus[0] -= 5

        if cacti and cacti[0][0] < -cactus_img.get_width():
            cacti.pop(0)

        for cactus in cacti:
            cactus_rect = pygame.Rect(cactus[0], ground_y - cactus_img.get_height(), cactus_img.get_width(), cactus_img.get_height())
            dinosaur_rect = pygame.Rect(dinosaur_x, dinosaur_y, dinosaur_img.get_width(), dinosaur_img.get_height())
            if dinosaur_rect.colliderect(cactus_rect):
                game_over()

        score += 1

        screen.fill((150, 150, 255))
        draw_ground()
        draw_dinosaur()
        draw_cacti()
        draw_score()

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
