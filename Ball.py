import pygame

#def drawBall(window):
#    ball = pygame.image.load("ball2.png")
#    window.blit(ball,(int(ball_pos[x]-10),int(ball_pos[y]-10))) 
    

from INI import *
#import pygame
class Ball:
    def __init__(self, window):
        self.window = window
        self.ball = pygame.image.load("images/ball2.png")
        self.X = int(ball_pos[x])
        self.Y = int(ball_pos[y])
        self.radius = 15
        self.speed = [0 , 0]
        self.goal = [0 , 0]
        # self.X = 300
        # self.Y = 200
        # pygame.draw.circle(self.window, black, (self.X, self.Y), self.radius)
        self.window.blit(self.ball,(self.X - self.radius,self.Y - self.radius))
    def move (self,kicked):
        self.X = self.X + self.speed[0]
        self.Y = self.Y + self.speed[1]
        k = 0.9
        self.speed[0] = int(k * self.speed[0])
        self.speed[1] = int(k * self.speed[1])

        #print(self.speed)
        if (self.X > wall_loc[3] or self.X < wall_loc[2]):
            if (self.Y > goal_loc[0] and self.Y  < goal_loc[1]):
                if (self.X < wall_loc[2]):
                    self.goal = [0 , 1]
                else:
                    self.goal = [1 , 0]
            else:
                if kicked:
                    self.speed[0] *= -1
                else:
                    if self.X > wall_loc[3]:
                        self.X = wall_loc[3]
                    if self.X < wall_loc[2]:
                        self.X = wall_loc[2]
        if (self.Y > wall_loc[0] or self.Y < wall_loc[1]):
            if kicked:
                self.speed[1] *= -1
            else:
                if self.Y > win_height:
                    self.Y = win_height
                if self.Y < 0:
                    self.Y = 0
        self.window.blit(self.ball,(self.X - self.radius,self.Y - self.radius))
