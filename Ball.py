import pygame
from pygame import *
from SoundEffects import *

#def drawBall(window):
#    ball = pygame.image.load("ball2.png")
#    window.blit(ball,(int(ball_pos[x]-10),int(ball_pos[y]-10))) 
    

from INI import *
#import pygame
class Ball:
    def __init__(self, window):
        self.window = window
        self.X = int(ball_pos[x]) - 10
        self.Y = int(ball_pos[y]) - 10
        self.radius = 18
        self.ball_radius = 35
        self.speed = [0 , 0]
        self.goal = [0 , 0]
        self.ball = transform.scale(pygame.image.load("images/ball.png"), (self.ball_radius, self.ball_radius))
        self.ball_rect = self.ball.get_rect()
        self.ball_rect.center = (self.X, self.Y)
        self.SoundEffect = SoundEffects()
        # pygame.draw.circle(self.window, black, (self.X, self.Y), self.radius)
        self.window.blit(self.ball,self.ball_rect)
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
                    self.SoundEffect.playGoal()
                else:
                    self.goal = [1 , 0]
                    self.SoundEffect.playGoal()
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
        self.ball_rect = self.ball.get_rect()
        self.ball_rect.center = (self.X, self.Y)
        self.window.blit(self.ball,self.ball_rect)
        # self.window.blit(self.ball,(self.X,self.Y))
