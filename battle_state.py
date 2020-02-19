import player
import cards
import random

class BattleState:
    def __init__(self, player, opponent):
        self.turn_counter = 1
        self.player = player
        self.opponent = opponent
        self.playerRPS = ""
        self.opponentRPS = ""
        self.playerCard = -1
        self.opponentCard = -1
        self.playerDamage = 0
        self.opponentDamage = 0

    def nextTurn(self):
        self.turn_counter = self.turn_counter + 1

    def setPlayerRPS(self, selection):
        self.playerRPS = selection

    def setOpponentRPS(self):
        selection = random.randint(1,3)
        if selection == 1:
            self.opponentRPS = "Rock"
        elif selection == 2:
            self.opponentRPS = "Paper"
        elif selection == 3:
            self.opponentRPS = "Scissors"

    def setPlayerCard(self, selected):
        if selected:
            self.playerCard = self.player.currentCard

    def setOpponentCard(self):
        selected = random.randint(1, 10)
        if selected > 3:
            self.opponentCard = self.opponent.currentCard

    def calculateDamage(self):
        print('placeholder, calculateDamage')
        # something something
        # playerDamage = ___
        # opponentDamage = ___
        # self.playerDamage = playerDamage
        # self.opponentDamage = opponentDamage
        # self.opponent.HP = self.opponent.HP - self.opponentDamage
        # self.player.HP = self.player.HP - self.playerDamage
