
class Graph:
    #Comments suck dick read my shit nerds
    def __init__(self, x, y):
        self.xBoundary = int(x)
        self.yBoundary = int(y)
        self.graph = [[0] * self.xBoundary for i in range(self.yBoundary)]
        self.generateStartLevel()
    def generateStartLevel(self):
        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):
                if(i == 0 or i == self.xBoundary-1):
                    self.graph[i][j] = Node(2);
                elif(j == 0 or j == self.yBoundary-1):
                    self.graph[i][j] = Node(2);
                else:
                    self.graph[i][j] = Node(0)
    def generatRandomLevel(self):
        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):
                if(i == 0 or i == self.xBoundary-1):
                    self.graph[i][j] = Node(2);
                elif(j == 0 or j == self.yBoundary-1):
                    self.graph[i][j] = Node(2);
                else:
                    self.graph[i][j] = Node(0)
    def isAWall(self, xPosition, yPosition):
        return self.graph[xPosition][yPosition].typeOfGround == 2
    def typeOfGround(self, xPosition, yPosition):
        return self.graph[xPosition][yPosition].typeOfGround

# GROUND TYPES:
# 0: Ground
# 1: Grass
# 2: Wall
# 3: Exit
# 4: Store
class Node:
    def __init__(self, typeOfGround):
        self.typeOfGround = typeOfGround
    def typeOfGround(self):
        return self.typeOfGround


