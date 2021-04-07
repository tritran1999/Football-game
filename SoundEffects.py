import pygame
from pygame import *

class SoundEffects:
    def __init__(self):
        self.mainTrack = ""
        self.goalKick = pygame.mixer.Sound("sounds/goal_kick.wav")
        self.background = pygame.mixer.music.load("sounds/background.ogg")
        self.goalCelebration = pygame.mixer.Sound("sounds/goal.mp3")
        self.hitWall = pygame.mixer.Sound("sounds/ball_hit.wav")

        self.goalCelebration.set_volume(10.0)
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(-1)

    def playKick(self):
        self.goalKick.play()
    
    def playGoal(self):
        self.goalCelebration.play()

    def playHitWall(self):
        self.hitWall.play()
