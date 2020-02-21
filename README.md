# Shoot: A turn-based RPG/visual novel by Allen Bao

Welcome to Shoot! This demo features a "vertical slice" of the full game. 
Many aspects of the game are missing in this stage, including the majority of the story, the characters, and the puzzle minigames.
This demo, however, does deliver the game's introduction cutscene, as well as a more detailed look at the main battle system, designed after rock-paper-scissors.

# How to install and execute (Windows 32-bit):
Source: 
- Make sure Python 3.7 and the pip tool are installed on your computer.
- Make sure the Python package "pygame" is installed on your computer. To do this, run python3 -m pip install -U pygame --user from the command line.
- Download and unzip the Shoot directory/repository. 
- Re-enter the command line and navigate to the Shoot directory. 
- Run the command: python setup.py build
- This will create a directory called build. Navigate to build/exe.win32-3.7, and run the file "main.exe".
- The game should now start!

Binary (recommended): 
- Create a folder called "Shoot" wherever you would like the game to be installed.
- Run the installer (Shoot-0.0.0-win32.msi). 
- Type in the directory path leading to your "Shoot" folder and click Next.
- Once the installation is complete, navigate to your shoot folder and run the file "main.exe".
- The game should now start!

# Features:
1. Introduction screen 
2. Short visual novel-style scene to introduce the basic premise
3. Ability card selection screen (5 cards are given to you at random - you must choose the order in which they appear in your roster.)
4. Main battle using your chosen ability cards
5. Game over and victory screens

# How to play/Outline of each section:
Story sections:
- Click with the left mouse button to progress through the text.

Shoot Preparation/Card Selection:
- Five of the seven available cards to pick are randomly chosen and laid out for you.
  - Left click on each of them in any order you wish to lock them into that order for the battle.
- You may left click on the RESET button to reselect your choices.
- Left click on the CONFIRM button to lock in your selection and progress to the battle.

Battle:
- During each turn, you must click on a selection of Rock, Paper, or Scissors to fight against your opponent's selection.
- After, you are presented with all of your ability cards in the same order in which you selected them.
  - Hover over any of the cards with your cursor to see a description of their effects.
  - You are only allowed to use the next available ability card. The other four on the side of the screen show you the order in which they will appear, but cannot be selected.
  - You may also choose not to use an ability card this turn by clicking on the SKIP button.
  - Only if you use a card, the order will rotate and you will be able to use the next card in the following turn.
- After the card selection, you may either click on the RESET button to start over, or the SHOOT button to lock in your choices.
- The game will then show what you and the opponent have selected, then perform damage calculations. Left click to progress through the text.

End screen:
- If you or your opponent have reached 0 HP, the demo will end with either a victory or a game over screen.
- Thanks for playing!

# Music and assets used:
All music is from the game "Your Turn to Die" by Nankidai.
All sound effects are from opengameart.org and freesound.org.
