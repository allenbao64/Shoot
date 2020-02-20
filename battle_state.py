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
        selection = random.randint(1, 3)
        if selection == 1:
            self.opponentRPS = "Rock"
        elif selection == 2:
            self.opponentRPS = "Paper"
        elif selection == 3:
            self.opponentRPS = "Scissors"

    def setPlayerCard(self, cardID):
        self.playerCard = cardID

    def setOpponentCard(self):
        selected = random.randint(1, 10)
        if selected > 3:
            self.opponentCard = self.opponent.cardOrder[0]

    def calculateDamage(self):
        if self.playerRPS == "Rock":
            if self.opponentRPS == "Paper":
                self.playerDamage = 1
            elif self.opponentRPS == "Scissors":
                self.opponentDamage = 1
        elif self.playerRPS == "Paper":
            if self.opponentRPS == "Rock":
                self.opponentDamage = 1
            elif self.opponentRPS == "Scissors":
                self.playerDamage = 1
        elif self.playerRPS == "Scissors":
            if self.opponentRPS == "Rock":
                self.playerDamage = 1
            elif self.opponentRPS == "Paper":
                self.opponentDamage = 1

        pCard = self.playerCard
        oCard = self.opponentCard

        self.opponent.HP = self.opponent.HP - self.opponentDamage
        self.player.HP = self.player.HP - self.playerDamage
