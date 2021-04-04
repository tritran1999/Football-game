import pygame
from pygame import *
from INI import *
from Field import *
from Ball import *
from Player import *
#print(y)
        
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 50)


window = pygame.display.set_mode((win_width, win_height))
BackGround = Background('Field1.jpg', [0,0])
points = [0 , 0]
player1 = player(window,0)
player2 = player(window,1)
ball1 = Ball(window)
kicked = False

def collision (x1, y1, r1, x2, y2, r2):
    if ((x1-x2)**2 + (y1-y2)**2) <= (r1 + r2)**2:
        return True
    else:
        return False

while True:

    event = pygame.event.poll()
    if event.type == pygame.QUIT:        
        pygame.quit()
        sys.exit() 

    #playerDir = [0 , 0]
    p1dirX = 0
    p1dirY = 0
    p2dirX = 0
    p2dirY = 0
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w] :
        p1dirY += -1
    if pressed[pygame.K_s]                      :
        p1dirY += 1
    if pressed[pygame.K_a]                      :
        p1dirX += -1
    if pressed[pygame.K_d]                     :
        p1dirX += 1
    if pressed[pygame.K_UP]:
        p2dirY += -1
    if pressed[pygame.K_DOWN]:
        p2dirY += 1
    if pressed[pygame.K_LEFT]:
        p2dirX += -1
    if pressed[pygame.K_RIGHT]:
        p2dirX += 1

    player1Dir = [p1dirX, p1dirY]
    player2Dir = [p2dirX, p2dirY]

  #  drawSoccer(window)

#    pygame.draw.circle(window, black, (int(ball_pos[x]), int(ball_pos[y])), radius)
#    drawBall(window)
    

#    Background.blit()
    window.fill([255, 255, 255])
    window.blit(BackGround.image, BackGround.rect)

    player1.move(player1Dir)
    player2.move(player2Dir)



    if collision(player1.X,player1.Y,player1.radius,ball1.X,ball1.Y,ball1.radius):
        ball1.speed = [4 * p1dirX, 4 * p1dirY]
        if pressed[pygame.K_SPACE]                     :
            kicked = True
            dirX = int((ball1.X - player1.X)/5)
            dirY = int((ball1.Y - player1.Y)/5)
            ball1.speed = [8*ball1.speed[0], 8*ball1.speed[1]]
    

    #else:
     #   ball1.speed = [0,0]

    if collision(player2.X, player2.Y, player2.radius, ball1.X, ball1.Y, ball1.radius):
        ball1.speed = [4 * p2dirX, 4 * p2dirY]
        if pressed[pygame.K_p]:
            kicked = True
            dirX = int((ball1.X - player2.X) / 5)
            dirY = int((ball1.Y - player2.Y) / 5)
            ball1.speed = [8 * ball1.speed[0], 8 * ball1.speed[1]]


    # else:
    #   ball1.speed = [0,0]
    if kicked:
        if ball1.speed != [0,0]:
            kicked = True
        else:
            kicked = False
    ball1.move(kicked)
    if (ball1.goal != [0 , 0]):
        points[0] += ball1.goal[0]
        points[1] += ball1.goal[1]
        
        player1 = player(window,0)
        player2 = player(window,1)
        ball1 = Ball(window)
        kicked = False
#    print(pygame.mouse.get_pos())
    
    player1PointsText = myfont.render(str(points[0]), False, (0, 0, 0))
    player2PointsText = myfont.render(str(points[1]), False, (0, 0, 0))
    
    window.blit(player1PointsText,(win_width/2 - win_width/10,0))
    window.blit(player2PointsText,(win_width/2 + win_width/10 - 25,0))

    pygame.display.update()
    
    clock = pygame.time.Clock().tick(60)
