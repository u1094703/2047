import pygame

class Graph:
    def __init__(self, x, y, characterX, characterY):
        self.xBoundary = x
        self.yBoundary = y
        self.characterX = characterX
        self.characterY = characterY
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
    # def update_position(self):


class Node:
    def __init__(self, typeOfGround):
        self.typeOfGround = typeOfGround
    def typeOfGround(self):
        return self.typeOfGround

if __name__ == "__main__":
    g = Graph(5, 5)


