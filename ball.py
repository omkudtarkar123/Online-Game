import pygame
from pygame import color
from player import Player


class Ball():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.circ = (x, y, radius)
        self.y_vel = 3
        self.x_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.y -= self.y_vel
        self.x += self.x_vel
        if self.y <= 25 or self.y >= 475:
            self.y_vel = -(self.y_vel)
        if self.x <= 25 or self.x >= 475:
            self.x_vel = -(self.x_vel)
        