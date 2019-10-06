
class Graph:
    #Comments suck dick read my shit nerds
    def __init__(self, x, y):
        self.xBoundary = int(x)
        self.yBoundary = int(y)
        self.graph = [[0] * self.xBoundary for i in range(self.yBoundary)]
        self.generateLevel(1)
    def generateLevel(self, levelNumber):
        if levelNumber == 1:
            file = open("StartLevel.txt", "r")
        if levelNumber == 2:
            file = open("SecondLevel.txt", "r")
        if levelNumber == 3:
            file = open("ThirdLevel.txt", "r")
        if levelNumber == 4:
            file = open("FourthLevel.txt", "r")
        j = 0
        for line in file:
            i = 0
            for element in line:
                if(element == '3'):
                    self.graph[i][j] = Node(3)
                if(element == '2'):
                    self.graph[i][j] = Node(2)
                if(element == "1"):
                    self.graph[i][j] = Node(1)
                if(element == "0"):
                    self.graph[i][j] = Node(0);
                i = i + 1
            j = j + 1

        # leftPosition = 10
        # rightPosition = 11
        # count = 0
        # for i in range(len(self.graph)):
        #     for j in range(len(self.graph[i])):
        #         if (i == leftPosition or i == rightPosition):
        #             self.graph[i][j] = Node(0)
        #             if (i == leftPosition and leftPosition != 2):
        #                 leftPosition = leftPosition - 1
        #             if(i == rightPosition and rightPosition != 3):
        #                 rightPosition = rightPosition-1
        #             elif (leftPosition == 2 and rightPosition == 3 and count != 4):
        #                 count = count + 1
        #             elif (count == 4):
        #                 if(i == leftPosition):
        #                     leftPosition = leftPosition + 1
        #                 if(i == rightPosition):
        #                     rightPosition = rightPosition + 1
        #         elif(i == 0 or i == self.xBoundary-1):
        #             self.graph[i][j] = Node(2);
        #         elif(j == 0 or j == self.yBoundary-1):
        #             self.graph[i][j] = Node(2);
        #
        #         else:
        #             self.graph[i][j] = Node(1)
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
class Node:
    def __init__(self, typeOfGround):
        self.typeOfGround = typeOfGround
    def typeOfGround(self):
        return self.typeOfGround


