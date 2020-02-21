import game_display
import battle_state
import player

def getCardDict():
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

def cardEffect(id, playerRPS, oppRPS):
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

def shield():
    return -1, 0

def beam():
    return 0, 1
