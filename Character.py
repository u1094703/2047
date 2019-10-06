class Character:
    def __init__  (self, name, maxHP = 20, HP = 20, attack = 0, defense = 0, critical = 0, positionX = 2, positionY = 4):
        self.maxHP = maxHP
        self.attack = attack
        self.defense = defense
        self.critical = critical
        self.positionX = positionX
        self.positionY = positionY

    def scoot_right (self):
        self.positionX += 1

    def scoot_left (self):
        self.positionX -= 1

    def scoot_up (self):
        self.positionY -= 1

    def scoot_down (self):
        self.positionY += 1


