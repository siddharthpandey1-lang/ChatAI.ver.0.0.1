import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cricket Game")

font = pygame.font.SysFont(None, 40)
WHITE, BLACK = (255, 255, 255), (0, 0, 0)

score = 0
game_over = False
message = "Press 1-6 to bat"

def draw_text(text, x, y):
    img = font.render(text, True, BLACK)
    screen.blit(img, (x, y))

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over and event.type == pygame.KEYDOWN:
            if event.unicode in '123456':
                player = int(event.unicode)
                computer = random.randint(1, 6)
                if player == computer:
                    message = f"Out! You chose {player}, Computer {computer}"
                    game_over = True
                else:
                    score += player
                    message = f"You scored {player} runs"

        elif game_over and event.type == pygame.KEYDOWN:
            if event.unicode == 'r':
                score = 0
                game_over = False
                message = "Press 1-6 to bat"

    draw_text("Cricket Game", 200, 30)
    draw_text(f"Score: {score}", 250, 100)
    draw_text(message, 150, 160)
    if game_over:
        draw_text("Press 'R' to restart", 180, 220)

    pygame.display.update()