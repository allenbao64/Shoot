class Player:
    def __init__(self, name, HP, cardOrder):
        self.name = name
        self.HP = HP
        self.cardOrder = cardOrder  # list of 5 card ids

    def setHP(self, HP):
        self.HP = HP

    def nextCard(self):
        self.cardOrder = self.cardOrder[1:] + self.cardOrder[:1]
