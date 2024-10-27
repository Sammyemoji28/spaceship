
import time
import pygame

from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Spaceship!!!!!!!")

width = 1000
height = 800

bg = pygame.image.load("background.jpg")
player = pygame.image.load("spaceship.png")
bg = pygame.transform.scale(bg, (width, height))
playerX = 500
playerY = 400

keys = [False, False, False, False]

while playerY < 800:
    screen.blit(bg, (0,0))
    screen.blit(player, (playerX, playerY))
    
    pygame.display.flip()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # - property QUIT
            pygame.quit() # - function quit
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                keys[0] = True
            elif event.key == K_LEFT:
                keys[1] = True
            elif event.key == K_DOWN:
                keys[2] = True
            elif event.key == K_RIGHT:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0] == False
            elif event.key == pygame.K_LEFT:
                keys[1] == False
            elif event.key == pygame.K_DOWN:
                keys[2] == False
            elif event.key == pygame.K_RIGHT:
                keys[3] == False
    if keys[0]:
        if playerY > 0:
            playerY -= 5
    if keys[2]:
        if playerY < 700:
            playerY += 5
    if keys[1]:
        if playerX > 0:
            playerX -= 5
    if keys[3]:
        if playerX < 900:
            playerX += 5
    #playerY += 5
    time.sleep(.5)