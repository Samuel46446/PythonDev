from random import randint
import pygame
import sys
import random

# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600

# Créer la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mon jeu Pygame")

# Couleur de fond
BACKGROUND_COLOR = (0, 0, 0)  # Noir

bX=400
bY=500
bonusSize=10
bonus=pygame.draw.rect(screen, (255,0,255), (bX, bY, bonusSize, bonusSize))

mX=700
mY=300
monsterSize=50
MoveDown=True

score=0
pv=5
police=pygame.font.Font(None, 22)

square_x, square_y = 150, 150
square_size = 25
speed=0.2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Fermer la fenêtre
            running = False
            print("quit")

    if pv == 0:
        running=False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and square_x > 0:
        square_x -= speed
    if keys[pygame.K_RIGHT] and square_x + square_size < WIDTH:
        square_x += speed
    if keys[pygame.K_UP] and square_y > 0:
        square_y -= speed
    if keys[pygame.K_DOWN] and square_y + square_size < HEIGHT:
        square_y += speed

    screen.fill(BACKGROUND_COLOR)

    player = pygame.draw.rect(screen, (255,255,0), (square_x, square_y, square_size, square_size))  # Dessiner le carré
    bonus = pygame.draw.rect(screen, (255, 0, 255), (bX, bY, bonusSize, bonusSize))
    monster = pygame.draw.rect(screen, (255, 0, 0), (mX, mY, monsterSize, monsterSize))


    if MoveDown and mY > 0:
        mY = mY - speed
    else:
        MoveDown=False

    if not MoveDown and mY + monsterSize < HEIGHT:
        mY = mY + speed
    else:
        MoveDown=True

    if player.colliderect(bonus):
        score=score+1
        bX=randint(0+bonusSize, WIDTH-bonusSize)
        bY=randint(0+bonusSize, HEIGHT-bonusSize)

    if player.colliderect(monster):
        pv=pv-1
        square_x, square_y = 150, 150
        mX = 700
        mY = 300

    score_text = police.render(f"Score: {score}", True, "white")
    pv_text = police.render(f"Pv: {pv}", True, "white")
    screen.blit(score_text, (10, 10))  # Position (x=10, y=10)
    screen.blit(pv_text, (10, 25))
    pygame.display.flip()

# Quitter Pygame
print("Vous n'avez plus de pv, votre score est de ", score, " points")
pygame.quit()
sys.exit()
