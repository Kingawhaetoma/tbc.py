# tbc.py


Turn Based Combat Pseudocode

Import random

Create Character class

Name
HP
Armor
hitChance
maxdamage

For each above,
@property
Define [variable] (self)
Return __[variable] = value

@[variable].setter
Define [variable](self,value)
Variable is tested to be in range
Self.[variable] gets value in range


Define testInt
Takes in value
Checks to see if it is an int(integer) between min and max
If it is not a legal value set it to default


Define printStats
Print name
HP
Hit chance,
max damage,
armor.

Define Hit
If random value is less than hit chance, do damage between 1 and [maxDamage]
Print who hits who for how much, but also how much is absorbed by armor.
If damage is greater than armor, deal damage with armor value subtracted.

Define Fight
Print player and enemies HP
Player hits enemy and enemy hits player
If the player's HP is greater than the enemy's HP print”player wins” and vice versa.
Create an input function so as to quit the game.


Define Main
New variable gets character info from class
Other variable gets character info from character class
Variable.printStats runs
Variable2.printStats runs

Run main

Title: Character Battle Simulator

Description:
This program simulates battles between characters in a text-based game. It defines a Character class with attributes such as name, hit points, armor, hit chance, and max damage. It also includes a fight function to simulate battles between two characters.

Dependencies:
- random module

Character Class:
- Properties:
    - name: Name of the character.
    - hitPoints: Current hit points of the character.
    - armor: Armor points of the character.
    - hitChance: Chance of successfully hitting the opponent.
    - maxDamage: Maximum damage the character can inflict.
- Methods:
    - __init__(): Initializes the character with default or custom attributes.
    - testInt(): Validates integer values within specified bounds.
    - printStats(): Prints the attributes of the character.
    - hit(enemy): Simulates an attack on the enemy character.

Fight Function:
- Parameters: player (character object), enemy (character object)
- Description: Simulates a battle between two characters.
- Iterates through rounds of attacks until one character's hit points drop to or below zero.
- Prints the current hit points of both characters after each round.
- Allows the user to choose whether to continue the fight or quit.

Main Function:
- Creates instances of the Character class to represent the player and the enemy.
- Calls the printStats method to display the attributes of the player character.
- Initiates the fight between the player and the enemy using the fight function.

Usage:
- Run the program to start the character battle simulator.
- Follow the prompts to observe battles between characters.



