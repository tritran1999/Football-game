from INI import *
import pygame
from pygame import *
class player:
    def __init__(self, window, player):
        self.window = window
        self.radius = 20
        self.player_radius = 50
        self. color = ""
        if player == 0:
            self.color = red
            self.X = win_width/2 - 100
            self.Y = win_height/2
            self.player_img = transform.scale(pygame.image.load("images/Character1.png"), (self.player_radius, self.player_radius))
        else:
            self.color = blue
            self.X = win_width/2 + 100
            self.Y = win_height/2
            self.player_img = transform.scale(pygame.image.load("images/Character2.png"), (self.player_radius, self.player_radius))
        # pygame.draw.circle(window, self.color, (self.X, self.Y), self.radius)
        self.window.blit(self.player_img,(self.X, self.Y))

    def move (self,dir):
        newX = self.X + dir[0]*4
        newY = self.Y + dir[1]*4
        if (newX  < wall_loc[3] and newX > wall_loc[2]):
            self.X = newX
        if (newY  < wall_loc[0] and newY > wall_loc[1]):
            self.Y = newY
        self.window.blit(self.player_img,(self.X, self.Y))
        
    
        
