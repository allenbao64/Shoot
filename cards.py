def getCardDict():
    cardDict = {
        0: "Dummy",
        1: "Give Dummy",
        2: "Enhanced Rock",
        3: "Enhanced Paper",
        4: "Enhanced Scissors",
        5: "Shield",
        6: "Clairvoyant",
        7: "Shoot",
        8: "Mini-Shoot",
        9: "Disable"
    }
    return cardDict

def getCardDescriptions():
    cardDict = {
        0: "Has no effect.",
        1: "Changes the opponent's next card into a Dummy card. Effect reverses once the new Dummy is played.",
        2: "Does 2HP to scissors, 1HP to rock, and ties with paper. Treats other enhanced cards as regular ones. After use, player must use regular rock in the following turn with no ability card.",
        3: "Does 2HP to rock, 1HP to paper, and ties with scissors. Treats other enhanced cards as regular ones. After use, player must use regular paper in the following turn with no ability card.",
        4: "Does 2HP to paper, 1HP to scissors, and ties with rock. Treats other enhanced cards as regular ones. After use, player must use regular scissors in the following turn with no ability card.",
        5: "Reduces all incoming damage by 1 HP. Active for 2 turns.",
        6: "Reveals opponent's next card and its effects.",
        7: "Charge for one turn, then launch an energy shot that deals 2 HP, or 1 HP if opponent uses an enhanced card. While charging, player is vulnerable to all attacks (1 HP for regular, 2 HP for enhanced)",
        8: "Launches a small energy shot that deals 1 HP. Has no effect if opponent uses an enhanced card.",
        9: "The opponent cannot use their current rock/paper/scissors selection for 2 turns following this one."
    }
    return cardDict
