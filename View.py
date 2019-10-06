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
        self.drawMainBackGround()
        pygame.display.update()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                if self.graph.isAWall(self.player.positionX - 1, self.player.positionY):
                    output = "do nothing"
                else:
                    self.player.scoot_left()
            if keys[pygame.K_RIGHT]:
                if self.graph.isAWall(self.player.positionX + 1, self.player.positionY):
                    output = "do nothing"
                else:
                    self.player.scoot_right()
            if keys[pygame.K_UP]:
                if self.graph.isAWall(self.player.positionX, self.player.positionY - 1):
                    output = "do nothing"
                else:
                    self.player.scoot_up()
            if keys[pygame.K_DOWN]:
                if self.graph.isAWall(self.player.positionX, self.player.positionY + 1):
                    output = "do nothing"
                else:
                    self.player.scoot_down()

    def check_tile_actions(self):
        if self.graph.typeOfGround(self.player.positionX, self.player.positionY) == 1:
            if randint(1, 6) == 1:
                self.battle()

    def drawMainBackGround(self):
        y = 0
        for i in range(0, 20):
            x = 0
            for j in range(0, 20):
                wallSize = pygame.Surface((tileSize, tileSize))
                if self.graph.typeOfGround(x, y) == 0:
                    wallSize.fill(floorColor)
                    self.screen.blit(wallSize, (x * tileSize, y * tileSize))
                elif self.graph.typeOfGround(x, y) == 1:
                    wallSize.fill(grassColor)
                    self.screen.blit(wallSize, (x * tileSize, y * tileSize))
                elif self.graph.typeOfGround(x, y) == 3:
                    wallSize.fill(itemStore)
                    self.screen.blit(wallSize, (x * tileSize, y * tileSize))
                else:
                    wallSize.fill(wallColor)
                    self.screen.blit(wallSize, (x * tileSize, y * tileSize))
                x = x + 1
            y = y + 1



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
                    self.player.credits += randint(15, 30)
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