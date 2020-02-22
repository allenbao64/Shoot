import player
import cards
import random

class BattleState:  # instantiated whenever a new battle begins, keeps track of HP and selections by both players
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
        self.storedPCard = -1
        self.storedOCard = -1

    def nextTurn(self):
        self.turn_counter = self.turn_counter + 1

    def setPlayerRPS(self, selection):
        self.playerRPS = selection

    def setOpponentRPS(self):  # gives the opponent a random selection between rock, paper, and scissors
        selection = random.randint(1, 3)
        if selection == 1:
            self.opponentRPS = "Rock"
        elif selection == 2:
            self.opponentRPS = "Paper"
        elif selection == 3:
            self.opponentRPS = "Scissors"

    def setPlayerCard(self, cardID):
        self.playerCard = cardID

    def setOpponentCard(self):  # 70% change of the opponent using their ability card, 30% to skip it
        selected = random.randint(1, 10)
        if selected > 3:
            self.opponentCard = self.opponent.cardOrder[0]
        else:
            self.opponentCard = -1

    def calculateDamage(self):  # uses all battle selections to calculate total damage done to both players
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

        # runs the cardEffect function twice, once from the perspective of each player
        pDam1, oDam1 = cards.cardEffect(self.playerCard, self.playerRPS, self.opponentRPS)
        oDam2, pDam2 = cards.cardEffect(self.opponentCard, self.opponentRPS, self.playerRPS)

        # combines the net damage effects of both players to calculate final damage scores
        self.playerDamage = self.playerDamage + pDam1 + pDam2
        self.opponentDamage = self.opponentDamage + oDam1 + oDam2

        # with the exception of the "rest" card, ensures that no player is healed by blocking damage while at 0 damage
        if self.playerDamage < 0:
            self.playerDamage = 0
        if self.opponentDamage < 0:
            self.opponentDamage = 0

        # if super shield is used, sets all damage to zero
        if self.playerCard > -1 and cards.getCardDict()[self.playerCard] == "Super Shield":
            self.playerDamage = 0
        if self.opponentCard > -1 and cards.getCardDict()[self.opponentCard] == "Super Shield":
            self.opponentDamage = 0

        # if rest is used while no damage has been inflicted, heals the player by 1 HP
        if self.playerCard > -1 and cards.getCardDict()[self.playerCard] == "Rest" and self.playerDamage == 0:
            self.playerDamage = -1
        if self.opponentCard > -1 and cards.getCardDict()[self.opponentCard] == "Rest" and self.opponentDamage == 0:
            self.opponentDamage = -1

        self.opponent.HP = self.opponent.HP - self.opponentDamage
        self.player.HP = self.player.HP - self.playerDamage
