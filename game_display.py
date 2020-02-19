import pygame
from player import Player
import cards
import random
import time

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shoot")
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()

def game_intro():
    intro = True

    pygame.mixer.music.load("audio/music/intro_music_placeholder.wav")
    pygame.mixer.music.play(-1)

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False

        titleText = pygame.font.SysFont('Arial', 80)
        TextSurf, TextRect = text_objects("Shoot - Demo Version", titleText)
        TextRect.center = ((screen_width * 0.5), (screen_height * 0.4))
        screen.blit(TextSurf, TextRect)

        subtitleText = pygame.font.SysFont('Arial', 50)
        TextSurf2, TextRect2 = text_objects("Press SPACE to start", subtitleText)
        TextRect2.center = ((screen_width * 0.5), (screen_height * 0.6))
        screen.blit(TextSurf2, TextRect2)

        subtitleText = pygame.font.SysFont('Arial', 30)
        TextSurf2, TextRect2 = text_objects("A game by Allen Bao (250904206)", subtitleText)
        TextRect2.center = ((screen_width * 0.5), (screen_height * 0.85))
        screen.blit(TextSurf2, TextRect2)

        pygame.display.update()

    pygame.mixer.music.stop()
    select_sound = pygame.mixer.Sound("audio/sfx/game_start.wav")
    pygame.mixer.Sound.play(select_sound)
    time.sleep(2)
    screen.fill((0, 0, 0))
    pygame.event.clear()
    story_loop()

def story_loop():
    story = True

    file = open('script.txt', 'r')
    line = file.readline()

    pygame.mixer.music.load("audio/music/story_music_placeholder.wav")
    pygame.mixer.music.play(-1)

    while story:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    line = file.readline()
                    if line[0:-1] == "!command: end":
                        story = False
                        screen.fill((0, 0, 0))
                        continue

        screen.fill((0, 0, 0))

        bgImage = pygame.image.load('images/backgrounds/jail.jpg')
        screen.blit(bgImage, (0, 0))
        charImage = pygame.image.load('images/characters/placeholder.png')
        screen.blit(charImage, (screen_width*0.35, screen_height*0.3))

        text = pygame.font.SysFont('Arial', 30)

        pygame.draw.rect(screen, (0, 0, 0), (screen_width*0.05, screen_height*0.7, screen_width*0.9, screen_height*0.25))

        if not story:
            continue
        else:
            TextSurf, TextRect = text_objects(line[0:-1], text)
            TextRect.center = ((screen_width / 2), (screen_height*0.75))
            screen.blit(TextSurf, TextRect)

        pygame.display.update()

    screen.fill((0, 0, 0))
    pygame.mixer.music.stop()
    pygame.event.clear()
    setup_loop()

def cardButton(selected, cardNum, text, x, y, w, h, color, active_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    selection = selected

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, w, h))
        if click[0] == 1:
            selection = cardNum
            select_sound = pygame.mixer.Sound("audio/sfx/card_select.wav")
            pygame.mixer.Sound.play(select_sound)
    else:
        pygame.draw.rect(screen, color, (x, y, w, h))

    cardText = pygame.font.SysFont("Arial", 15)
    textSurf, textRect = text_objects(text, cardText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)
    return selection

def miscButton(text, x, y, w, h, color, active_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    action = False

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, w, h))
        if click[0] == 1:
            action = True
    else:
        pygame.draw.rect(screen, color, (x, y, w, h))

    cardText = pygame.font.SysFont("Arial", 20)
    textSurf, textRect = text_objects(text, cardText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)
    return action

def setup_loop():
    setup = True

    pygame.mixer.music.load("audio/music/prep_music_placeholder.wav")
    pygame.mixer.music.play(-1)

    cardDict = cards.getCardDict()

    playerCards = []
    oppOrder = []
    for i in range(0, 5):
        cardID = random.randint(0, 9)
        while cardID in playerCards:
            cardID = random.randint(0, 9)
        cardID2 = random.randint(0, 9)
        while cardID2 in oppOrder:
            cardID2 = random.randint(0, 9)
        playerCards.append(cardID)
        oppOrder.append(cardID2)

    playerOrder = [-1]

    selections = [0, 0, 0, 0, 0]

    while setup:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill((0, 0, 0))

        reset = miscButton("RESET", screen_width * 0.02, screen_height * 0.85, screen_width * 0.13, screen_height * 0.1, (0, 0, 100), (0, 0, 200))
        if reset:
            reset = False
            playerOrder = [-1]
            selections = [0, 0, 0, 0, 0]

        confirm = miscButton("CONFIRM", screen_width * 0.85, screen_height * 0.85, screen_width * 0.13, screen_height * 0.1, (0, 100, 0), (0, 200, 0))
        if confirm and len(playerOrder) == 5:
            setup = False

        text = pygame.font.SysFont('Arial', 60)
        TextSurf, TextRect = text_objects("SHOOT PREPARATION", text)
        TextRect.center = ((screen_width / 2), (screen_height * 0.1))
        screen.blit(TextSurf, TextRect)

        text2 = pygame.font.SysFont('Arial', 40)
        TextSurf2, TextRect2 = text_objects("Select the order of your ability cards!", text2)
        TextRect2.center = ((screen_width / 2), (screen_height * 0.9))
        screen.blit(TextSurf2, TextRect2)

        current = 0.025
        for i in range(0, 5):
            selections[i] = cardButton(selections[i], len(playerOrder), cardDict[playerCards[i]], screen_width * current,
                       screen_height * 0.25, screen_width * 0.15, screen_height * 0.1, (100, 0, 0), (255, 0, 0))
            if selections[i] > 0:
                if playerCards[i] not in playerOrder:
                    if -1 in playerOrder:
                        playerOrder.pop()
                    playerOrder.append(playerCards[i])
                buttonImage = pygame.image.load("images/buttons/" + str(selections[i]) + ".png")
                screen.blit(buttonImage, (screen_width * current + 8, screen_height * 0.14))

            charImage = pygame.image.load('images/descriptions/' + str(playerCards[i]) + '.png')
            screen.blit(charImage, (screen_width * current, screen_height * 0.38))

            current = current + 0.2

        pygame.display.update()

    player = Player("Player", 10, playerOrder)
    opponent = Player("Opponent", 10, oppOrder)

    screen.fill((0, 0, 0))
    pygame.mixer.music.stop()
    select_sound = pygame.mixer.Sound("audio/sfx/card_confirm.wav")
    pygame.mixer.Sound.play(select_sound)
    time.sleep(2)
    pygame.event.clear()
    battle_loop(player, opponent)

def battle_loop(player, opponent):
    enemyImg = pygame.image.load('images/characters/placeholder.png')

    battle = True
    win = False

    pygame.mixer.music.load("audio/music/battle_music_placeholder.wav")
    pygame.mixer.music.play(-1)

    while battle:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if close button is pressed, quit game
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    player.setHP(0)
                elif event.button == 3:
                    opponent.setHP(0)
        if opponent.HP == 0:
            battle = False
            win = True
            screen.fill((0, 0, 0))
            continue
        elif player.HP == 0:
            battle = False
            screen.fill((0, 0, 0))
            continue

        screen.blit(enemyImg, (screen_width*0.6, screen_height*0.05))

        pygame.draw.rect(screen, (255, 255, 255), (screen_width * 0.02, screen_height * 0.8, screen_width * 0.96, screen_height * 0.18), 1)
        #text but conditional for state

        pygame.display.update()

    pygame.mixer.music.stop()
    if win:
        pygame.event.clear()
        victory_loop()
    else:
        pygame.event.clear()
        gameover_loop()

    # player = Player("Me", 10, [1, 2, 3, 4, 5])
    # player.setHP(player.getHP() - 1)
    # player.nextCard()

def victory_loop():
    victory = True

    #pygame.mixer.music.load("audio/music/victory_music_placeholder.wav")
    #ygame.mixer.music.play(-1)

    while victory:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    victory = False

        titleText = pygame.font.SysFont('Arial', 80)
        TextSurf, TextRect = text_objects("VICTORY!", titleText)
        TextRect.center = ((screen_width * 0.5), (screen_height * 0.4))
        screen.blit(TextSurf, TextRect)

        subtitleText = pygame.font.SysFont('Arial', 50)
        TextSurf2, TextRect2 = text_objects("End of Demo - Press SPACE to quit", subtitleText)
        TextRect2.center = ((screen_width * 0.5), (screen_height * 0.6))
        screen.blit(TextSurf2, TextRect2)
        pygame.display.update()

    pygame.quit()
    quit()

def gameover_loop():
    gameover = True

    #pygame.mixer.music.load("audio/music/gameover_music_placeholder.wav")
    #pygame.mixer.music.play(-1)

    while gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameover = False

        titleText = pygame.font.SysFont('Arial', 80)
        TextSurf, TextRect = text_objects("GAME OVER", titleText)
        TextRect.center = ((screen_width * 0.5), (screen_height * 0.4))
        screen.blit(TextSurf, TextRect)

        subtitleText = pygame.font.SysFont('Arial', 50)
        TextSurf2, TextRect2 = text_objects("End of Demo - Press SPACE to quit", subtitleText)
        TextRect2.center = ((screen_width * 0.5), (screen_height * 0.6))
        screen.blit(TextSurf2, TextRect2)

        pygame.display.update()

    pygame.quit()
    quit()
