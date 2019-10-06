import pygame
import Character
import Enemy
import Graph
from random import randint, random
import shelve
from pygame.locals import *
from Setting import *
from Graph import Graph
from Character import *
class View:
    def __init__(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((width, height))
        self.graph = Graph(gridWidth, gridHeight)
        self.player = Character("placeholder name")
        pygame.display.set_caption("2047")
        self.savefile = shelve.open('savefile')
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

    def new_game(self):
        if not self.savefile:
            output = "Nothing to overwrite"
        else:
            self.wipe_saved_data()

    def wipe_saved_data(self):
        self.savefile.clear()
        player = Character("placeholder name")

    def save_game(self):
        self.savefile['maxHP'] = self.player.maxHP
        self.savefile['attack'] = self.player.attack
        self.savefile['defense'] = self.player.defense
        self.savefile['critical'] = self.player.critical
        self.savefile['positionX'] = self.player.positionX
        self.savefile['positionY'] = self.positionY

    def load_game(self):
        if not self.savefile:
            output = "No game saved"
        else:
            self.player.maxHP = self.savefile['maxHP']
            self.player.attack = self.savefile['attack']
            self.player.defense = self.savefile['defense']
            self.player.critical = self.savefile['critical']
            self.player.positionX = self.savefile['positionX']
            self.positionY = self.savefile['positionY']

    # in future versions, scale the difficulty of the enemies based on the map/level
    def battle(self):
        rand = random
        opponent = Enemy(randint(8, 15), randint(0, 1), randint(0, 1), 0)
        whose_turn = 'p'
        while True:
            if whose_turn == 'p':
                self.attack(self.player, opponent)
                if opponent.HP <= 0:
                    break
                whose_turn = 'o'
            else:
                self.attack(opponent, self.player)
                if self.player.currentHP <= 0:
                    break
                whose_turn = 'p'

    def attack(self,being_1, being_2):
        attack_roll = randint(1, 6)
        critical_roll = self.get_critical_roll(being_1)
        total_attack = attack_roll + critical_roll + being_1.attack - being_2.defense
        being_2.HP -= total_attack

    def get_critical_roll(self,being):
        if being.critical == 0:
            if randint(1, 6) == 1:
                critical = randint(1, 6)
            else:
                critical = 0
        elif being.critical == 1:
            if randint(1, 4) == 1:
                critical = randint(1, 6)
            else:
                critical = 0
        elif being.critical == 2:
            if randint(1, 2) == 1:
                critical = randint(1, 6)
            else:
                critical = 0
        else:
            critical = randint(1, 6)

        return critical

if __name__=="__main__":
    view = View()
    view.runningGame()