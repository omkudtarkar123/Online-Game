import pygame
from pygame import color

class Ball():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.circ = (x, y, radius)
        self.vel = 3
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x -= self.vel

win = pygame.display.set_mode((500, 500))
b = Ball(200, 200, 50, (0,255,255))
b.draw(win)
clock = pygame.time.Clock()


x_pos = 200
y_pos = 200
run = True
while run:
    win.fill((255,255,255))
    #pygame.draw.circle(win, (255,0,0), (x_pos,y_pos), 50)
    b.draw(win)
    b.move()
    #x_pos += 3
    pygame.display.update()
    clock.tick(30)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()