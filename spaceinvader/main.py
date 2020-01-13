import pygame
import random
import math

#inititalizing pygame
pygame.init()
#Screen display
screen = pygame.display.set_mode(size=(800,600))
running = True
#Screen title and icon
pygame.display.set_caption("Space Invader")
pygame.display.set_icon(pygame.image.load("project.png"))

#Screen background
background=pygame.image.load("background.png")

#loading spaceship image on to the screen
playerimage = pygame.image.load("spaceship.png")
playerX=370
playerY=480
playerX_change=0

score =0

enemyimage = pygame.image.load("enemy.png")
enemyX=random.randint(0,800)
enemyY=random.randint(50,150)
enemyX_change=4
enemyY_change=40

bulletimage = pygame.image.load("bullet.png")
bulletX=0
bulletY=480
bulletX_change=4
bulletY_change=10
bullet_state="ready"


def player(x,y):
    screen.blit(playerimage,(x,y))


def enemy(x,y):
    screen.blit(enemyimage,(x,y))


def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletimage,(x+16,y+10))


def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow((enemyX-bulletX),2))+(math.pow((enemyY-bulletY),2)))
    if distance <= 27:
        return True
    else:
        return False

while running:
    # screen filled with black color
    screen.fill(color=(0, 0, 0))
    # set background
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                playerX_change=15
            if event.key==pygame.K_LEFT:
                playerX_change=-15
            if event.key==pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)
        if event.type==pygame.KEYUP:
            if (event.key==pygame.K_RIGHT) or (event.key==pygame.K_LEFT):
                playerX_change=0
    playerX += playerX_change
    #space ship boundaries checking if it goes beyond
    enemyX += enemyX_change

    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736
    # enemy movement
    if enemyX<=0:
        enemyX_change=10
        enemyY += enemyY_change
    elif enemyX>=736:
        enemyX_change=-10
        enemyY += enemyY_change

    # bullet movement
    if bulletY<=0:
        bulletY=480
        bullet_state="ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    collision=iscollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY=480
        bullet_state="ready"
        score+=1
        enemyX = random.randint(0, 800)
        enemyY = random.randint(50, 150)



    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()