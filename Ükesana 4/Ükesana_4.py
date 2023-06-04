import pygame
import sys
import random

pygame.init()

X = 640
Y = 480

Valge = (255, 255, 255)
Must = (0, 0, 0)
Kollane = (255, 255, 0)

les=pygame.image.load("cxz.png")

seen_suurus = 20
Mario_laius = 30
Mario_kõrgus = 30

seen_X = random.randint(0, X - seen_suurus)
seen_Y = 0

Mario_X = X // 2 - Mario_laius // 2
Mario_Y = Y // 1.25

seen_kiirus = 3 #Скорость грибов.
enemies=[]

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("seen")

seen_pilt = pygame.image.load("zxc.png")  # для грибов
Mario_pilt = pygame.image.load("всякое.png")  # для корзины

player = pygame.Rect(X, Y, 120, 120)
playerImage = pygame.image.load("всякое.png")
playerImage = pygame.transform.scale(playerImage, [player.width, player.height])

for i in range(5):
    enemies.append(pygame.Rect(random.randint(0, X - 100), random.randint(0,Y - 100), 60, 73))
enemyImage = pygame.image.load("zxc.png")
enemyImage = pygame.transform.scale(enemyImage, [enemies[0].width, enemies[0].height])

clock = pygame.time.Clock()
score = 0
gameover=False
while not gameover:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover=True
        elif pygame.key.get_pressed()[pygame.K_a]:
            Mario_X-=10
        elif pygame.key.get_pressed()[pygame.K_d]:
            Mario_X+=10
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                Mario_X-=30
            elif event.key==pygame.K_RIGHT:
                Mario_X+=30

    seen_Y += seen_kiirus

    for enemy in enemies[:]:
        if player.colliderect(enemy):
            enemies.remove(enemy)
            score += 1
            seen_X = random.randint(0, X - seen_suurus)
            seen_Y = 0

    if seen_Y >= Y:
        score -= 1
        seen_X = random.randint(0, X - seen_suurus)
        seen_Y = 0

    if seen_Y + seen_suurus >= Mario_Y and seen_X + seen_suurus >= Mario_X and seen_X <= Mario_X + Mario_laius:
        score += 1
        seen_X = random.randint(0, X - seen_suurus)
        seen_Y = 0


    screen.fill(Valge)

    for enemy in enemies[:]:
        if player.colliderect(enemy):
            enemies.remove(enemy)
            score += 1
            seen_X = random.randint(0, X - seen_suurus)
            seen_Y = 0


    screen.blit(les, (0,0))
    screen.blit(seen_pilt, (seen_X, seen_Y)) # Отображение изображения яблока на экране
    screen.blit(Mario_pilt, (Mario_X, Mario_Y)) # Отображение изображения корзины на экране

    font = pygame.font.Font(None, 36)
    score_text = font.render("Счет: {}".format(score), True, Must)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
