from random import randint
import pygame
import sys
import random

# Définir les dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600

def onCollisionWithMonster(mob, playable, pvPlayer, xPlayer, yPlayer, xMob, yMob, valueX, valueY):
    if playable.colliderect(mob):
        pvPlayer=pvPlayer-1
        xPlayer, yPlayer = 150, 150
        xMob = valueX
        yMob = valueY
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
bonusSize=20
bonus=pygame.draw.rect(screen, (255,0,255), (bX, bY, bonusSize, bonusSize))

#Default Coord Monsters
MonsterBaseX=700
MonsterBaseY=300
BigBaseX=200
BigBaseY=500
CrazyBaseX=200
CrazyBaseY=550
SpeedyBaseX=400
SpeedyBaseY=50

mX=MonsterBaseX
mY=MonsterBaseY
bmX=BigBaseX
bmY=BigBaseY
cmX=CrazyBaseX
cmY=CrazyBaseY
smX=SpeedyBaseX
smY=SpeedyBaseY

monsterSize=50

monsterTxt=pygame.image.load("textures/monster.png")
BigmonsterTxt=pygame.image.load("textures/monsterBig.png")
CrazymonsterTxt=pygame.image.load("textures/monsterCrazy.png")
SpeedymonsterTxt=pygame.image.load("textures/monsterSpeedy.png")

#Boolean Monsters
    #For Crazy Monster
CrazyDown=True
CrazyRight=True
    #For Speedy Monster
SpeedyDown=True
SpeedyRight=True

    #For Monsters and Big Monster
MoveDown=True
MoveRight=True

score=0
pv=5
police=pygame.font.Font(None, 22)

square_x, square_y = 150, 150
square_size = 25
speed=0.2

#Heart System
heartSpawn=20 # Quand le score est égal à 20 un coeur spawn
heartTxt=pygame.image.load("textures/heart.png")
playerTxt=pygame.image.load("textures/player.png")
bonusTxt=pygame.image.load("textures/bonus.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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

    player = pygame.Rect(square_x, square_y, square_size, square_size) #pygame.draw.rect(screen, (255,255,0), (square_x, square_y, square_size, square_size))
    bonus = pygame.Rect(bX, bY, bonusSize, bonusSize)#pygame.draw.rect(screen, (255, 0, 255), (bX, bY, bonusSize, bonusSize))
    texture_player = pygame.transform.scale(playerTxt, (player.width, player.height))
    screen.blit(texture_player, player.topleft)
    texture_bonus = pygame.transform.scale(bonusTxt, (bonus.width, bonus.height))
    screen.blit(texture_bonus, bonus.topleft)

    heart=None


    if score >= heartSpawn:
        heart=pygame.Rect(250, 250, 25, 25)
        texture_heart = pygame.transform.scale(heartTxt, (heart.width, heart.height))
        screen.blit(texture_heart, heart.topleft)
        if player.colliderect(heart):
            pv=pv+1
            heartSpawn=heartSpawn+10

    monster=None
    monsterBig=None
    monsterCrazy=None
    monsterSpeedy=None

    if score >= 3:
        monster = pygame.Rect(mX, mY, monsterSize, monsterSize)
        MoveDown, mY = ia_monster(MoveDown, mY, speed, HEIGHT)
        pv, square_x, square_y, mX, mY = onCollisionWithMonster(monster, player, pv, square_x, square_y, mX, mY, MonsterBaseX, MonsterBaseY)
        texture_monster = pygame.transform.scale(monsterTxt, (monster.width, monster.height))
        screen.blit(texture_monster, monster.topleft)
    if score >= 6:
        monsterBig = pygame.Rect(bmX, bmY, monsterSize+10, monsterSize+10)
        MoveRight, bmX = ia_monster(MoveRight, bmX, speed, WIDTH)
        pv, square_x, square_y, bmX, bmY = onCollisionWithMonster(monsterBig, player, pv, square_x, square_y, bmX, bmY, BigBaseX, BigBaseY)
        texture_bigmonster = pygame.transform.scale(BigmonsterTxt, (monsterBig.width, monsterBig.height))
        screen.blit(texture_bigmonster, monsterBig.topleft)
    if score >= 12:
        monsterCrazy = pygame.Rect(cmX, cmY, monsterSize, monsterSize)
        CrazyDown, cmY = ia_monster(CrazyDown, cmY, speed, HEIGHT)
        CrazyRight, cmX = ia_monster(CrazyRight, cmX, speed, WIDTH)
        pv, square_x, square_y, cmX, cmY = onCollisionWithMonster(monsterCrazy, player, pv, square_x, square_y, cmX, cmY, CrazyBaseX, CrazyBaseY)
        texture_crazymonster = pygame.transform.scale(CrazymonsterTxt, (monsterCrazy.width, monsterCrazy.height))
        screen.blit(texture_crazymonster, monsterCrazy.topleft)
    if score >= 25:
        monsterSpeedy = pygame.Rect(smX, smY, 30, 30)
        SpeedyDown, smY = ia_monster(SpeedyDown, smY, speed+0.001, HEIGHT)
        SpeedyRight, smX = ia_monster(SpeedyRight, smX, speed+0.001, WIDTH)
        pv, square_x, square_y, smX, smY = onCollisionWithMonster(monsterSpeedy, player, pv, square_x, square_y, smX, smY, SpeedyBaseX, SpeedyBaseY)
        texture_speedymonster = pygame.transform.scale(SpeedymonsterTxt, (monsterSpeedy.width, monsterSpeedy.height))
        screen.blit(texture_speedymonster, monsterSpeedy.topleft)

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