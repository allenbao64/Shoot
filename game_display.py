import pygame
from player import Player
from battle_state import BattleState
import cards
import random
import time

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))  # initializes game screen
pygame.display.set_caption("Shoot")
clock = pygame.time.Clock()

def text_objects(text, font):  # creates surface for displaying text
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()

def game_intro():  # runs loop to display the intro screen
    intro = True

    pygame.mixer.music.load("audio/music/intro_music_placeholder.wav")
    pygame.mixer.music.play(-1)

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # quits out of the game if the exit/X button is pressed
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # if space is pressed the game will exit the loop and progress to the story screen
                    intro = False
                if event.key == pygame.K_RETURN:  # if enter/return is pressed the game will skip directly to the battle setup
                    setup_loop()

        titleText = pygame.font.Font('SourceSansPro-Regular.ttf', 80)
        TextSurf, TextRect = text_objects("Shoot - Demo Version", titleText)  # Main title text
        TextRect.center = ((screen_width * 0.5), (screen_height * 0.35))
        screen.blit(TextSurf, TextRect)

        subtitleText = pygame.font.Font('SourceSansPro-Regular.ttf', 50)
        TextSurf2, TextRect2 = text_objects("Press SPACE to start", subtitleText)
        TextRect2.center = ((screen_width * 0.5), (screen_height * 0.55))
        screen.blit(TextSurf2, TextRect2)

        subtitleText = pygame.font.Font('SourceSansPro-Regular.ttf', 50)
        TextSurf3, TextRect3 = text_objects("Press ENTER to skip story", subtitleText)
        TextRect3.center = ((screen_width * 0.5), (screen_height * 0.7))
        screen.blit(TextSurf3, TextRect3)

        subtitleText = pygame.font.Font('SourceSansPro-Regular.ttf', 30)
        TextSurf4, TextRect4 = text_objects("A game by Allen Bao (250904206)", subtitleText)
        TextRect4.center = ((screen_width * 0.5), (screen_height * 0.85))
        screen.blit(TextSurf4, TextRect4)

        pygame.display.update()  # updates screen with changes every time the loop runs

    pygame.mixer.music.fadeout(1000)  # once loop exits the music will fade out, play a sound, and progress to the next screen
    time.sleep(0.5)
    select_sound = pygame.mixer.Sound("audio/sfx/game_start.wav")
    pygame.mixer.Sound.play(select_sound)
    time.sleep(1.5)
    screen.fill((0, 0, 0))
    pygame.event.clear()
    story_loop()

def story_loop():
    story = True
    showIm = False
    playSound = False

    file = open('script.txt', 'r')  # the story text comes from the script.txt file, where it is read in line-by-line
    line = file.readline()

    pygame.mixer.music.load("audio/music/story_music_placeholder.wav")
    pygame.mixer.music.play(-1)

    while story:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:  # progresses to the next line each time the left mouse button is clicked
                if event.button == 1:
                    line = file.readline()
                    if line[0:-1] == "!command: end":  # the script.txt file has special command lines that trigger functions
                        story = False
                        screen.fill((0, 0, 0))
                        continue
                    elif line[0:-2] == "!command: note":  # this command shows the note images
                        showIm = True
                        note = pygame.image.load('images/other/note' + line[-2] + '.png')
                        pageFlip = pygame.mixer.Sound("audio/sfx/page.wav")
                        pygame.mixer.Sound.play(pageFlip)
                    elif line[0:-1] == "!command: sound buzzer":  # this command plays the buzzer sound effect
                        playSound = True
                        buzzerSound = pygame.mixer.Sound("audio/sfx/buzzer.wav")
                        pygame.mixer.Sound.play(buzzerSound)
                        time.sleep(2)
                        pygame.event.clear()
                    else:  # this runs for regular script lines (no commands)
                        showIm = False
                        playSound = False

        screen.fill((0, 0, 0))

        bgImage = pygame.image.load('images/backgrounds/jail.jpg')
        screen.blit(bgImage, (0, 0))  # projects background image

        text = pygame.font.Font('SourceSansPro-Regular.ttf', 25)

        if not showIm and not playSound:  # draws text box for when dialogue needs to appear
            pygame.draw.rect(screen, (0, 0, 0), (screen_width*0.05, screen_height*0.7, screen_width*0.9, screen_height*0.25))

            if not story:
                continue  # exits the loop if the end of the script has been reached
            else:  # displays the line of text
                TextSurf, TextRect = text_objects(line[0:-1], text)
                TextRect.center = ((screen_width / 2), (screen_height*0.80))
                screen.blit(TextSurf, TextRect)

        if showIm:  # shows note
            screen.blit(note, (screen_width * 0.3, screen_height * 0.2))

        pygame.display.update()

    screen.fill((0, 0, 0))
    pygame.mixer.music.fadeout(1000)
    pygame.event.clear()
    setup_loop()

def cardButton(selected, cardNum, text, x, y, w, h, color, active_color):  # creates custom buttons to display cards on the setup screen
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    selection = selected

    if x + w > mouse[0] > x and y + h > mouse[1] > y:  # boxes change colour when the mouse hovers over them
        pygame.draw.rect(screen, active_color, (x, y, w, h))
        if click[0] == 1 and selection == 0:  # cards are selected when clicked, and cannot be selected more than once
            selection = cardNum + 1
            select_sound = pygame.mixer.Sound("audio/sfx/card_select.wav")
            pygame.mixer.Sound.play(select_sound)
    else:
        pygame.draw.rect(screen, color, (x, y, w, h))  # displays the typical card box colour while not being hovered over

    cardText = pygame.font.Font('SourceSansPro-Regular.ttf', 15)
    textSurf, textRect = text_objects(text, cardText)  # displays text over the boxes
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)
    return selection  # returns selection, telling the setup_loop function if this button has been selected

def miscButton(text, x, y, w, h, color, active_color, cardHover=False, cardID=None):  # for any other button with different functionalities
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    action = False  # tells the invoker function if the button has been pressed

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, w, h))
        if cardHover:  # if this is set as a battle loop card button, hovering over it will display the card's description
            desc = pygame.image.load('images/descriptions/' + str(cardID) + '.png')
            screen.blit(desc, (screen_width * 0.7, screen_height * 0.1))
        if click[0] == 1:
            action = True
    else:
        pygame.draw.rect(screen, color, (x, y, w, h))

    cardText = pygame.font.Font('SourceSansPro-Regular.ttf', 20)
    textSurf, textRect = text_objects(text, cardText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)
    return action

def setup_loop():
    setup = True

    pygame.mixer.music.load("audio/music/prep_music_placeholder.wav")
    pygame.mixer.music.play(-1)

    cardDict = cards.getCardDict()  # card dictionary to map card IDs onto card names

    playerCards = []  # list that contains the five cards displayed on the screen
    oppOrder = []  # list that contains the predetermined randomized order of the opponent's cards
    for i in range(0, 5):  # randomizes cards (without repetition)
        cardID = random.randint(1, 7)
        while cardID in playerCards:
            cardID = random.randint(1, 7)
        cardID2 = random.randint(1, 7)
        while cardID2 in oppOrder:
            cardID2 = random.randint(1, 7)
        playerCards.append(cardID)
        oppOrder.append(cardID2)

    playerOrder = []  # list that contains the player's selected cards in order

    selections = [0, 0, 0, 0, 0]  # each element will change from zero to display the order in which cards have been selected

    while setup:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill((0, 0, 0))

        reset = miscButton("RESET", screen_width * 0.02, screen_height * 0.85, screen_width * 0.13, screen_height * 0.1, (0, 0, 100), (0, 0, 200))
        if reset:  # removes all selections to allow the player to start over
            reset = False
            playerOrder = []
            selections = [0, 0, 0, 0, 0]

        confirm = miscButton("CONFIRM", screen_width * 0.85, screen_height * 0.85, screen_width * 0.13, screen_height * 0.1, (0, 100, 0), (0, 200, 0))
        if confirm and len(playerOrder) == 5:  # exits loop if the right number of selections has been made
            setup = False

        text = pygame.font.Font('SourceSansPro-Regular.ttf', 60)
        TextSurf, TextRect = text_objects("SHOOT PREPARATION", text)
        TextRect.center = ((screen_width / 2), (screen_height * 0.1))
        screen.blit(TextSurf, TextRect)

        text2 = pygame.font.Font('SourceSansPro-Regular.ttf', 35)
        TextSurf2, TextRect2 = text_objects("Select the order of your ability cards!", text2)
        TextRect2.center = ((screen_width / 2), (screen_height * 0.9))
        screen.blit(TextSurf2, TextRect2)

        current = 0.025  # value will increment to space cards out across the screen
        for i in range(0, 5):
            selections[i] = cardButton(selections[i], len(playerOrder), cardDict[playerCards[i]], screen_width * current,
                       screen_height * 0.25, screen_width * 0.15, screen_height * 0.1, (100, 0, 0), (255, 0, 0))
            if selections[i] > 0:  # card has been selected - add it to the player's card order
                if playerCards[i] not in playerOrder:
                    playerOrder.append(playerCards[i])
                buttonImage = pygame.image.load("images/buttons/" + str(selections[i]) + ".png")  # adds the button image to show selection
                screen.blit(buttonImage, (screen_width * current + 8, screen_height * 0.14))

            charImage = pygame.image.load('images/descriptions/' + str(playerCards[i]) + '.png')  # shows description underneath each card
            screen.blit(charImage, (screen_width * current, screen_height * 0.38))

            current = current + 0.2

        pygame.display.update()

    # creates new player objects with their starting attributes (HP and card order)
    player = Player("Player", 10, playerOrder)
    opponent = Player("Lord Mike", 10, oppOrder)
    battle = BattleState(player, opponent)  # starts new battle with the two players

    screen.fill((0, 0, 0))
    pygame.mixer.music.stop()
    select_sound = pygame.mixer.Sound("audio/sfx/card_confirm.wav")
    pygame.mixer.Sound.play(select_sound)
    time.sleep(1)
    pygame.event.clear()
    pygame.mixer.music.load("audio/music/battle_music_placeholder.wav")
    pygame.mixer.music.play(-1)
    rps_loop(battle, player, opponent)

def battle_permanent_display(battle, player, opponent):  # loads and displays images and text that are present for every stage of the battle
    enemyImg = pygame.image.load('images/characters/mike.jpg')
    heart = pygame.image.load("images/other/heart.png")

    screen.blit(enemyImg, (screen_width * 0.4, screen_height * 0.05))  # display enemy image

    HPText = pygame.font.Font('SourceSansPro-Regular.ttf', 40)
    TextSurf, TextRect = text_objects(opponent.name + " HP: " + str(opponent.HP), HPText)  # display opponent HP
    TextRect.center = ((screen_width * 0.2), (screen_height * 0.15))
    screen.blit(TextSurf, TextRect)

    oppHeartPos = 0.02
    for i in range(0, opponent.HP):  # display opponent's HP in heart images
        screen.blit(heart, (screen_width * oppHeartPos, screen_height * 0.2))
        oppHeartPos = oppHeartPos + 0.035

    TextSurf2, TextRect2 = text_objects(player.name + " HP: " + str(player.HP), HPText)
    TextRect2.center = ((screen_width * 0.5), (screen_height * 0.6))
    screen.blit(TextSurf2, TextRect2)

    playerHeartPos = 0.32
    for i in range(0, player.HP):
        screen.blit(heart, (screen_width * playerHeartPos, screen_height * 0.65))
        playerHeartPos = playerHeartPos + 0.035

    TextSurf3, TextRect3 = text_objects("Turn " + str(battle.turn_counter), HPText)  # display turn counter
    TextRect3.center = ((screen_width * 0.1), (screen_height * 0.05))
    screen.blit(TextSurf3, TextRect3)

    pygame.draw.rect(screen, (255, 255, 255),  # display text box
                     (screen_width * 0.02, screen_height * 0.7, screen_width * 0.96, screen_height * 0.28), 1)

def rps_loop(battle, player, opponent):  # loop that plays while player is making their rock/paper/scissors selection
    time.sleep(0.25)

    rps = True
    while rps:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if close button is pressed, quit game
                pygame.quit()
                quit()

        battle_permanent_display(battle, player, opponent)

        # detects and saves which button has been selected
        rock = miscButton("ROCK", screen_width * 0.10, screen_height * 0.74, screen_width * 0.2,
                             screen_height * 0.2, (100, 0, 0), (200, 0, 0))
        paper = miscButton("PAPER", screen_width * 0.4, screen_height * 0.74, screen_width * 0.2,
                          screen_height * 0.2, (0, 0, 100), (0, 0, 200))
        scissors = miscButton("SCISSORS", screen_width * 0.7, screen_height * 0.74, screen_width * 0.2,
                          screen_height * 0.2, (0, 100, 0), (0, 200, 0))

        if rock:
            battle.setPlayerRPS("Rock")
        if paper:
            battle.setPlayerRPS("Paper")
        if scissors:
            battle.setPlayerRPS("Scissors")

        if battle.playerRPS != "":  # plays a sound after a selection, then quits the loop to progress to the next screen
            ping = pygame.mixer.Sound("audio/sfx/ping.wav")
            pygame.mixer.Sound.play(ping)
            rps = False

        pygame.display.update()

    screen.fill((0, 0, 0))
    pygame.event.clear()
    card_loop(battle, player, opponent)

def card_loop(battle, player, opponent):  # loop that plays while the player is making their card selection
    time.sleep(0.25)

    card = True
    while card:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if close button is pressed, quit game
                pygame.quit()
                quit()

        battle_permanent_display(battle, player, opponent)

        skip = miscButton("SKIP", screen_width * 0.05, screen_height * 0.74, screen_width * 0.2,  # button to not choose a card this turn
                              screen_height * 0.2, (50, 100, 50), (50, 200, 50))
        activeCard = miscButton(cards.getCardDict()[player.cardOrder[0]], screen_width * 0.35, screen_height * 0.74, screen_width * 0.25,
                              screen_height * 0.2, (100, 20, 0), (200, 20, 0), cardHover=True, cardID=player.cardOrder[0])  # current active card

        # four buttons that display the next available cards (cannot be clicked, but can be viewed as descriptions if hovered over)
        miscButton(cards.getCardDict()[player.cardOrder[1]], screen_width * 0.7, screen_height * 0.72, screen_width * 0.25,
                              screen_height * 0.05, (0, 100, 0), (0, 200, 0), cardHover=True, cardID=player.cardOrder[1])
        miscButton(cards.getCardDict()[player.cardOrder[2]], screen_width * 0.7, screen_height * 0.78, screen_width * 0.25,
                              screen_height * 0.05, (0, 100, 0), (0, 200, 0), cardHover=True, cardID=player.cardOrder[2])
        miscButton(cards.getCardDict()[player.cardOrder[3]], screen_width * 0.7, screen_height * 0.84, screen_width * 0.25,
                              screen_height * 0.05, (0, 100, 0), (0, 200, 0), cardHover=True, cardID=player.cardOrder[3])
        miscButton(cards.getCardDict()[player.cardOrder[4]], screen_width * 0.7, screen_height * 0.90, screen_width * 0.25,
                              screen_height * 0.05, (0, 100, 0), (0, 200, 0), cardHover=True, cardID=player.cardOrder[4])

        if skip:
            card = False
        if activeCard:
            battle.playerCard = player.cardOrder[0]
            card = False

        pygame.display.update()

    ping = pygame.mixer.Sound("audio/sfx/ping.wav")
    pygame.mixer.Sound.play(ping)
    screen.fill((0, 0, 0))
    pygame.event.clear()
    shoot_loop(battle, player, opponent)

def shoot_loop(battle, player, opponent):  # loop that plays while player is on the lock-in/shoot screen
    time.sleep(0.25)

    shoot = True
    while shoot:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if close button is pressed, quit game
                pygame.quit()
                quit()

        battle_permanent_display(battle, player, opponent)

        shootButton = miscButton("SHOOT!", screen_width * 0.6, screen_height * 0.74, screen_width * 0.2,
                          screen_height * 0.2, (0, 100, 0), (0, 200, 0))  # lock in selection

        reset = miscButton("RESET", screen_width * 0.2, screen_height * 0.74, screen_width * 0.2,
                          screen_height * 0.2, (0, 0, 100), (0, 0, 200))  # restart selection

        if reset:  # restart selection, resets the battle state
            battle.setPlayerRPS("")
            battle.setPlayerCard(-1)
            shoot = False
            screen.fill((0, 0, 0))
            pygame.event.clear()
            rps_loop(battle, player, opponent)

        if shootButton:  # progresses to the action screen
            shoot = False
            ping = pygame.mixer.Sound("audio/sfx/ping.wav")
            pygame.mixer.Sound.play(ping)
            screen.fill((0, 0, 0))
            action_loop(battle, player, opponent)

        pygame.display.update()

def action_loop(battle, player, opponent):  # loop that plays to calculate all results of the battle turn and display them
    time.sleep(0.25)

    battle.setOpponentRPS()  # opponent's selections are made once the player's selections have finished
    battle.setOpponentCard()

    topText = player.name + " used " + battle.playerRPS + "!"  # topText displays the player's selections and actions
    if battle.playerCard > -1:
        topText = player.name + " used " + battle.playerRPS + " and " + cards.getCardDict()[battle.playerCard] + "!"
    botText = opponent.name + " used " + battle.opponentRPS + "!"  # botText displays the opponent's selections and actions
    if battle.opponentCard > -1:
        botText = opponent.name + " used " + battle.opponentRPS + " and " + cards.getCardDict()[battle.opponentCard] + "!"

    reset = False
    victory = False
    gameover = False
    action = True
    clairvoyant = False
    clairCard = -1
    while action:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if close button is pressed, quit game
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # click to progress to the following text
                    if reset:  # battle has not ended, progress to the next turn
                        battle.setPlayerRPS("")
                        battle.setPlayerCard(-1)
                        screen.fill((0, 0, 0))
                        pygame.event.clear()
                        rps_loop(battle, player, opponent)
                    elif victory:  # battle has ended, progress to victory screen
                        screen.fill((0, 0, 0))
                        pygame.mixer.music.fadeout(1000)
                        victory_loop()
                    elif gameover:  # battle has ended, progress to game over screen
                        screen.fill((0, 0, 0))
                        pygame.mixer.music.fadeout(1000)
                        gameover_loop()
                    else:  # calculates the damage taken by both players, then decides the state of the battle
                        battle.calculateDamage()
                        if battle.playerDamage > 0 or battle.opponentDamage > 0:  # plays sound if damage was taken
                            dmgSound = pygame.mixer.Sound("audio/sfx/damage.wav")
                            pygame.mixer.Sound.play(dmgSound)
                        if battle.playerDamage == -1 or battle.opponentDamage == -1:  # plays sound for HP recovery
                            recoverSound = pygame.mixer.Sound("audio/sfx/recover.wav")
                            pygame.mixer.Sound.play(recoverSound)

                        # function of Give Dummy - replaces opponent's next card with the Dummy card
                        if battle.playerCard > -1 and cards.getCardDict()[battle.playerCard] == "Give Dummy":
                            battle.storedOCard = opponent.cardOrder[1]  # keeps track of the card that was replaced so it can be returned later
                            opponent.cardOrder[1] = 0
                        if battle.opponentCard > -1 and cards.getCardDict()[battle.opponentCard] == "Give Dummy":
                            battle.storedPCard = player.cardOrder[1]
                            player.cardOrder[1] = 0
                        # if either player plays their Dummy card, it will go back to the previous card
                        # note: Dummy is not a selectable card - it can only appear through the Give Dummy card's action
                        if battle.playerCard > -1 and cards.getCardDict()[battle.playerCard] == "Dummy":
                            player.cardOrder[0] = battle.storedPCard
                            battle.storedPCard = -1
                        if battle.opponentCard > -1 and cards.getCardDict()[battle.opponentCard] == "Dummy":
                            opponent.cardOrder[0] = battle.storedOCard
                            battle.storedOCard = -1
                        # displays the opponent's next card and description on the screen
                        if battle.playerCard > -1 and cards.getCardDict()[battle.playerCard] == "Clairvoyant":
                            clairvoyant = True
                            clairCard = opponent.cardOrder[1]
                            if battle.opponentCard == -1:
                                clairCard = opponent.cardOrder[0]
                            desc = pygame.image.load('images/descriptions/' + str(clairCard) + '.png')

                        # sets next text to be displayed after left click
                        topText = player.name + " took " + str(battle.playerDamage) + " HP of damage!"
                        if battle.playerDamage < 0:
                            topText = player.name + " recovered " + str(battle.playerDamage * -1) + " HP!"
                        botText = opponent.name + " took " + str(battle.opponentDamage) + " HP of damage!"
                        if battle.opponentDamage < 0:
                            botText = opponent.name + " recovered " + str(battle.opponentDamage * -1) + " HP!"

                        # resets battle state for the next turn, increments turn counter
                        if player.HP > 0 and opponent.HP > 0:
                            battle.playerDamage = 0
                            battle.opponentDamage = 0
                            battle.turn_counter = battle.turn_counter + 1
                            if battle.playerCard > -1:  # rotates cards if they have been used
                                player.nextCard()
                            if battle.opponentCard > -1:
                                opponent.nextCard()
                            reset = True
                        elif opponent.HP <= 0:
                            victory = True
                        elif player.HP <= 0:
                            gameover = True

        screen.fill((0, 0, 0))

        battle_permanent_display(battle, player, opponent)

        # shows rock/paper/scissors graphics
        screen.blit(pygame.image.load("images/other/" + battle.opponentRPS + "O.png"), (screen_width * 0.12, screen_height * 0.23))
        screen.blit(pygame.image.load("images/other/" + battle.playerRPS + ".png"), (screen_width * 0.11, screen_height * 0.45))

        text = pygame.font.Font('SourceSansPro-Regular.ttf', 25)
        TextSurf, TextRect = text_objects(topText, text)
        TextRect.center = ((screen_width * 0.5), (screen_height * 0.75))
        screen.blit(TextSurf, TextRect)
        TextSurf2, TextRect2 = text_objects(botText, text)
        TextRect2.center = ((screen_width * 0.5), (screen_height * 0.9))
        screen.blit(TextSurf2, TextRect2)

        if clairvoyant:
            TextSurfC, TextRectC = text_objects("Opponent's next card: " + cards.getCardDict()[clairCard], text)
            TextRectC.center = ((screen_width * 0.7), screen_height * 0.02)
            screen.blit(TextSurfC, TextRectC)
            screen.blit(desc, (screen_width * 0.7, screen_height * 0.1))

        pygame.display.update()

def victory_loop():
    victory = True

    while victory:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    victory = False

        titleText = pygame.font.Font('SourceSansPro-Regular.ttf', 80)
        TextSurf, TextRect = text_objects("VICTORY!", titleText)
        TextRect.center = ((screen_width * 0.5), (screen_height * 0.4))
        screen.blit(TextSurf, TextRect)

        subtitleText = pygame.font.Font('SourceSansPro-Regular.ttf', 50)
        TextSurf2, TextRect2 = text_objects("End of Demo - Press SPACE to quit", subtitleText)
        TextRect2.center = ((screen_width * 0.5), (screen_height * 0.6))
        screen.blit(TextSurf2, TextRect2)
        pygame.display.update()

    pygame.quit()
    quit()

def gameover_loop():
    gameover = True

    while gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameover = False

        titleText = pygame.font.Font('SourceSansPro-Regular.ttf', 80)
        TextSurf, TextRect = text_objects("GAME OVER", titleText)
        TextRect.center = ((screen_width * 0.5), (screen_height * 0.4))
        screen.blit(TextSurf, TextRect)

        subtitleText = pygame.font.Font('SourceSansPro-Regular.ttf', 50)
        TextSurf2, TextRect2 = text_objects("End of Demo - Press SPACE to quit", subtitleText)
        TextRect2.center = ((screen_width * 0.5), (screen_height * 0.6))
        screen.blit(TextSurf2, TextRect2)

        pygame.display.update()

    pygame.quit()
    quit()
