def getCardDict():  # returns a dictionary matching each card ID to the card's name
    cardDict = {
        0: "Dummy",  # no code
        1: "Give Dummy",  # in game_display
        2: "Enhancement",  # below
        3: "Shield",    # below
        4: "Super Shield",  # in battle_state
        5: "Clairvoyant",  # in game_display
        6: "Beam",  # below
        7: "Rest"  # in battle_state
    }
    return cardDict

def cardEffect(id, playerRPS, oppRPS):  # determines what the card's function will be, based on the ID given
    playerDamage = 0
    oppDamage = 0
    if id == 2:
        if playerRPS == "Rock":
            playerDamage, oppDamage = eRock(oppRPS)
        elif playerRPS == "Paper":
            playerDamage, oppDamage = ePaper(oppRPS)
        elif playerRPS == "Scissors":
            playerDamage, oppDamage = eScissors(oppRPS)
    elif id == 3:
        playerDamage, oppDamage = shield()
    elif id == 6:
        playerDamage, oppDamage = beam()
    return playerDamage, oppDamage

# enhanced cards: extra strength vs ties and strengths, and reduces player damage by 1 vs weaknesses
def eRock(oppRPS):
    playerDamage = 0
    oppDamage = 0
    if oppRPS == "Rock":
        oppDamage = 1
    elif oppRPS == "Paper":
        playerDamage = -1
    elif oppRPS == "Scissors":
        oppDamage = 1
    return playerDamage, oppDamage

def ePaper(oppRPS):
    playerDamage = 0
    oppDamage = 0
    if oppRPS == "Paper":
        oppDamage = 1
    elif oppRPS == "Scissors":
        playerDamage = -1
    elif oppRPS == "Rock":
        oppDamage = 1
    return playerDamage, oppDamage

def eScissors(oppRPS):
    playerDamage = 0
    oppDamage = 0
    if oppRPS == "Scissors":
        oppDamage = 1
    elif oppRPS == "Rock":
        playerDamage = -1
    elif oppRPS == "Paper":
        oppDamage = 1
    return playerDamage, oppDamage

def shield():  # reduces the player's damage by 1
    return -1, 0

def beam():  # inflicts 1 HP damage on the opponent
    return 0, 1
