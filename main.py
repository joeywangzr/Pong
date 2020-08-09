import pygame
from paddle import Paddle
from ball import Ball
import time

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
font = pygame.font.Font(None, 74)

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

playing = True

clock = pygame.time.Clock()

scoreA = 0
scoreB = 0

screen.blit(font.render("READY?", 1, WHITE), (245,70))
pygame.display.flip()
time.sleep(1)

for count in [3, 2, 1]:
    screen.fill(BLACK)
    screen.blit(font.render("READY?", 1, WHITE), (245,70))
    screen.blit(font.render(str(count), 1, WHITE), (330,150))
    pygame.display.flip()
    time.sleep(1)

for i in range(5):
    screen.fill(BLACK)
    pygame.display.flip()
    time.sleep(0.1)
    screen.blit(font.render("GAME ON!", 1, WHITE), (225,150))
    pygame.display.flip()
    time.sleep(0.1)
    
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              playing = False

    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    all_sprites_list.draw(screen) 

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(8)
    if keys[pygame.K_s]:
        paddleA.moveDown(8)
    if keys[pygame.K_UP]:
        paddleB.moveUp(8)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(8)    

    all_sprites_list.update()

    if ball.rect.x >= 690:
        scoreA += 1
        ball.aPoint()
    if ball.rect.x <= 0:
        scoreB += 1
        ball.bPoint()
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]     

    # print(ball.velocity)
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    screen.blit(font.render(str(scoreA), 1, WHITE), (180,20))
    screen.blit(font.render(str(scoreB), 1, WHITE), (490,20))

    if scoreA == 10:
        for i in range(5):
            screen.fill(BLACK)
            pygame.display.flip()
            time.sleep(0.1)
            pygame.draw.rect(screen, BLACK, [0, 0, 800, 800])
            screen.blit(font.render('Player A wins!!!', 1, WHITE), (160,70))
            pygame.display.flip()
            time.sleep(0.1)
        break

    elif scoreB == 10:
        for i in range(5):
            screen.fill(BLACK)
            pygame.display.flip()
            time.sleep(0.1)
            pygame.draw.rect(screen, BLACK, [0, 0, 800, 800])
            screen.blit(font.render('Player B wins!!!', 1, WHITE), (160,70))
            pygame.display.flip()
            time.sleep(0.1)
        break

    pygame.display.flip()
    clock.tick(60)

time.sleep(1)
pygame.quit()
