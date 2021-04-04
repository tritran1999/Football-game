from INI import *
import pygame
class player:
    def __init__(self, window, player):
        self.window = window
        self.radius = 15
        self. color = ""
        if player == 0:
            self.color = red
            self.X = win_width/2 - 100
            self.Y = win_height/2
        else:
            self.color = blue
            self.X = win_width/2 + 100
            self.Y = win_height/2
        pygame.draw.circle(window, self.color, (self.X, self.Y), self.radius)

    def move (self,dir):
        newX = self.X + dir[0]*4
        newY = self.Y + dir[1]*4
        if (newX  < wall_loc[3] and newX > wall_loc[2]):
            self.X = newX
        if (newY  < wall_loc[0] and newY > wall_loc[1]):
            self.Y = newY
        pygame.draw.circle(self.window, self.color, (self.X, self.Y), self.radius)
        
    
        
