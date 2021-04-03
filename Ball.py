import pygame
#def drawBall(window):
#    ball = pygame.image.load("ball2.png")
#    window.blit(ball,(int(ball_pos[x]-10),int(ball_pos[y]-10))) 
    

from INI import *
#import pygame
class Ball:
    def __init__(self, window):
        self.window = window
        #self.ball = pygame.image.load("ball2.png")
        self.X = int(ball_pos[x])
        self.Y = int(ball_pos[y])
        self.radius = 10
        self.speed = [0 , 0]
        self.goal = [0 , 0]
        #self.X = 300
        #self.Y = 200
        pygame.draw.circle(self.window, black, (self.X, self.Y), self.radius)
    def move (self,kicked):
        self.X = self.X + self.speed[0]
        self.Y = self.Y + self.speed[1]
        k = 0.9
        self.speed[0] = int(k * self.speed[0])
        self.speed[1] = int(k * self.speed[1])

        #print(self.speed)
        if (self.X > win_width or self.X < 0):
            if (self.Y > goal_loc[0] and self.Y  < goal_loc[1]):
                if (self.X < 0):
                    self.goal = [0 , 1]
                else:
                    self.goal = [1 , 0]
            else:
                if kicked:
                    self.speed[0] *= -1
                else:
                    if self.X > win_width:
                        self.X = win_width
                    if self.X < 0:
                        self.X = 0
        if (self.Y > win_height or self.Y < 0):
            if kicked:
                self.speed[1] *= -1
            else:
                if self.Y > win_height:
                    self.Y = win_height
                if self.Y < 0:
                    self.Y = 0
        pygame.draw.circle(self.window, black, (self.X, self.Y), self.radius)
