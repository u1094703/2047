import pygame
from pygame.locals import *
from Setting import *
from Graph import Graph
class View:
    def __init__(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((width, height))
        self.graph = Graph(gridWidth, gridHeight)
    def runningGame(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.drawMainBackGround()
            pygame.display.update()

    def drawMainBackGround(self):
       for x in range(len(self.graph.graph)):
           for y in range (len(self.graph.graph[x])):
               wallSize = pygame.Surface((x * tileSize, y * tileSize))
               if self.graph.typeOfGround(x, y) == 0:
                   wallSize.fill(floorColor)
                   self.screen.blit(wallSize, (x * tileSize, y * tileSize))
               elif self.graph.typeOfGround(x,y) == 1:
                   wallSize.fill(grassColor)
                   self.screen.blit(wallSize, (x * tileSize, y * tileSize))
               else:
                   wallSize.fill(wallColor)
                   self.screen.blit(wallSize, (x * tileSize, y * tileSize))






if __name__=="__main__":
    view = View()
    view.runningGame()

