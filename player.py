import pygame

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 5
        self.moving_right = False
        self.moving_left = False
        self.moving = False
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        #self.x += self.vel
        self.moving_left = False
        self.moving = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
            #self.vel = -3
            #self.moving = True
            selfmoving_right = False
            self.moving_left = True
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
            #self.vel = 3
            #self.moving = True
            self.moving_right = True
            self.moving_left = False
        #if keys[pygame.K_UP]:
            #self.y -= self.vel
        #if keys[pygame.K_DOWN]:
            #self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
