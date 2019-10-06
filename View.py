import pygame
from pygame.locals import *
from Graph import Graph

pygame.init()
width = 700
height = 700
screen=pygame.display.set_mode((width,height))
isBlue=True
done = False
graph = Graph(width, height)
def starting():
    NewSurface = pygame.Surface((500, 300))
    NewSurface.fill((55, 155, 255))
    screen.blit(NewSurface, (0,0))
    screen.update()


while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done =True
    starting()