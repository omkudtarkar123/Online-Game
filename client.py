import pygame
from network import Network
from player import Player
from ball import Ball

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Client')
#b = Ball(250,250,25, (0,0,0))

def redrawWindow(win, player, player2, b1, b2):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    b1.draw(win)
    b2.draw(win)
    if (b1.y <= 50 and b1.x > player.x and b1.x < player.x + 100) or (b2.y <= 50 and b2.x > player2.x and b2.x < player2.x + 100):
        b1.y_vel = -(b1.y_vel)
        b2.y_vel = -(b2.y_vel)
        if player.moving_right == True:
            b1.x_vel += player.vel
            b2.x_vel += player2.vel
        if player.moving_left == True:
            b1.x_vel -= player.vel
            b2.x_vel += player2.vel
    b1.move()
    pygame.display.update()

def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        p2 = n.send(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p[0].move()
        p[1].move()
        redrawWindow(win, p[0], p2[0], p[1], p2[1])

main()