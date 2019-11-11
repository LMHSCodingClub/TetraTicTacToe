import pygame
from pygame.locals import *
pygame.init()

LEFT = 1 # left button
(width, height) = (600, 750)
backgroundColor = (255,255,255)
bg = pygame.image.load('gameboard.png')

screen = pygame.display.set_mode((width, height))

# screen modifications before flip()
pygame.display.flip()

running = True
while running:
 screen.blit(bg, (0, 0))
 pygame.display.flip()
 event = pygame.event.poll()
 if event.type == pygame.QUIT:
     running = False
     pygame.quit()

 elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
     print ("You pressed the left mouse button at (%d, %d)" % event.pos)
 elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
     print ("You released the left mouse button at (%d, %d)" % event.pos)
