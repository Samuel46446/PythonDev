from random import randint
import pygame
import sys
import random

# Définir les dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600

def onCollisionWithMonster(mob, playable, pvPlayer, xPlayer, yPlayer, xMob, yMob):
    if playable.colliderect(mob):
        pvPlayer=pvPlayer-1
        xPlayer, yPlayer = 150, 150
        xMob = 700
        yMob = 300
    return pvPlayer, xPlayer, yPlayer, xMob, yMob

def ia_monster(b : bool, moveValue, sprint, param):
    if b and moveValue > 0:
        moveValue = moveValue - sprint
    else:
        b=False

    if not b and moveValue + monsterSize < param:
        moveValue = moveValue + sprint
    else:
        b=True
    return b, moveValue

# Initialiser Pygame
pygame.init()

# Créer la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mon jeu Pygame")

# Couleur de fond
BACKGROUND_COLOR = (0, 0, 0)  # Noir

bX=400
bY=500
bonusSize=10
bonus=pygame.draw.rect(screen, (255,0,255), (bX, bY, bonusSize, bonusSize))

cmX=200
cmY=100
CrazyDown=True
CrazyRight=True

bmX=200
bmY=500

mX=700
mY=300
monsterSize=50
MoveDown=True
MoveRight=True

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

    monster=None
    monsterBig=None
    monsterCrazy=None

    if score >= 3:
        monster = pygame.draw.rect(screen, (255, 0, 0), (mX, mY, monsterSize, monsterSize))
        MoveDown, mY = ia_monster(MoveDown, mY, speed, HEIGHT)
        pv, square_x, square_y, mX, mY = onCollisionWithMonster(monster, player, pv, square_x, square_y, mX, mY)
    if score >= 10:
        monsterBig = pygame.draw.rect(screen, (56, 255, 89), (bmX, bmY, monsterSize, monsterSize))
        MoveRight, bmX = ia_monster(MoveRight, bmX, speed, WIDTH)
        pv, square_x, square_y, bmX, bmY = onCollisionWithMonster(monsterBig, player, pv, square_x, square_y, bmX, bmY)
    if score >= 16:
        monsterCrazy = pygame.draw.rect(screen, (255, 192, 203), (cmX, cmY, monsterSize, monsterSize))
        CrazyDown, cmY = ia_monster(CrazyDown, cmY, speed, HEIGHT)
        CrazyRight, cmX = ia_monster(CrazyRight, cmX, speed, WIDTH)
        pv, square_x, square_y, cmX, cmY = onCollisionWithMonster(monsterCrazy, player, pv, square_x, square_y, cmX, cmY)

    if player.colliderect(bonus):
        score=score+1
        bX=randint(0+bonusSize, WIDTH-bonusSize)
        bY=randint(0+bonusSize, HEIGHT-bonusSize)

    score_text = police.render(f"Score: {score}", True, "white")
    pv_text = police.render(f"Pv: {pv}", True, "white")
    screen.blit(score_text, (10, 10))  # Position (x=10, y=10)
    screen.blit(pv_text, (10, 25))
    pygame.display.flip()

# Quitter Pygame
print("Vous n'avez plus de pv, votre score est de", score, "points")
pygame.quit()
sys.exit()
