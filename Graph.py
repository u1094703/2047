
class Graph:
    #Comments suck dick read my shit nerds
    def __init__(self, x, y):
        self.xBoundary = x
        self.yBoundary = y
        self.graph = [[0] * x]*y
        self.make_walls()
    def make_walls(self):
        for i in range(len(self.graph)):
            for j in range(len(self.graph)):
                if(i == 0 or i == self.xBoundary-1):
                    self.graph[i][j] = Node(2);
                elif(j == 0 or j == self.yBoundary-1):
                    self.graph[i][j] = Node(2);
                else:
                    self.graph[i][j] = Node(0)
    def isAWall(self, xPosition, yPosition):
        return self.graph[xPosition][yPosition].typeOfGround == 2
class Node:
    def __init__(self, typeOfGround):
        self.typeOfGround = typeOfGround
    def typeOfGround(self):
        return self.typeOfGround


