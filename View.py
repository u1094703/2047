import pygame
import Character
import Enemy
import Graph
from random import randint
import shelve

player = Character("placeholder name")
game_map = Graph()

savefile = shelve.open('savefile')

def new_game():
    if not savefile:
        output = "Nothing to overwrite"
    else:
        wipe_saved_data()

def wipe_saved_data():
    savefile.clear()
    player = Character("placeholder name")

def save_game():
    savefile['maxHP'] = player.maxHP
    savefile['attack'] = player.attack
    savefile['defense'] = player.defense
    savefile['critical'] = player.critical
    savefile['positionX'] = player.positionX
    savefile['positionY'] = self.positionY

def load_game():
    if not savefile:
        output = "No game saved"
    else:
        player.maxHP = savefile['maxHP']
        player.attack = savefile['attack']
        player.defense = savefile['defense']
        player.critical = savefile['critical']
        player.positionX = savefile['positionX']
        self.positionY = savefile['positionY']

# NOTE: INITIALZE THESE VALUES TO SAVED VALUES IF THERE'S A SAVE FILE
pygame.init()
screen=pygame.display.set_mode((400,400))
isBlue=True
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done =True

# in future versions, scale the difficulty of the enemies based on the map/level
def battle():
    rand = random
    opponent = Enemy(randint(8, 15), randint(0, 1), randint(0, 1), 0)
    whose_turn = 'p'
    while True:
        if whose_turn == 'p':
            attack(player, opponent)
            if opponent.HP <= 0:
                break
            whose_turn = 'o'
        else:
            attack(opponent, player)
            if player.currentHP <= 0:
                break
            whose_turn = 'p'

def attack(being_1, being_2):
    attack_roll = randint(1, 6)
    critical_roll = get_critical_roll(being_1)
    total_attack = attack_roll + critical_roll + being_1.attack - being_2.defense
    being_2.HP -= total_attack

def get_critical_roll(being):
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
        critical = rand(1, 6)

    return critical