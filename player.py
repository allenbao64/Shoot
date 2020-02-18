class Player:
    def __init__(self, name, HP, cardOrder):
        self.name = name
        self.HP = HP
        self.cardOrder = cardOrder  # list of 5 card ids
        self.currentCard = self.cardOrder[0]
        print("This is the player " + self.name + ".")
        print(self.name + " has " + str(self.HP) + " HP.")
        print(self.name + "'s cards are: " + ','.join(map(str, self.cardOrder)))

    def getName(self):
        return self.name

    def getHP(self):
        return self.HP

    def getCurrentCard(self):
        return self.currentCard

    def setHP(self, HP):
        self.HP = HP
        print(self.name + "'s new HP is: " + str(self.HP))

    def nextCard(self):
        print("Card order before rotation: " + ','.join(map(str, self.cardOrder)))
        self.cardOrder = self.cardOrder[1:] + self.cardOrder[:1]
        print("Card order after rotation: " + ','.join(map(str, self.cardOrder)))