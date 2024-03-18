# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 09:40:35 2024

@author: kinga
"""

import random

class Character:
    def __init__(self, name, hit_points, hit_chance, max_damage, armor):
        self.name = name
        self.hit_points = hit_points
        self.hit_chance = hit_chance
        self.max_damage = max_damage
        self.armor = armor

    def is_alive(self):
        return self.hit_points > 0

    def attack(self, other):
        if random.randint(1, 100) <= self.hit_chance:
            damage = random.randint(1, self.max_damage)
            damage -= other.armor
            damage = max(damage, 0)
            other.hit_points -= damage
            print(f"{self.name} attacks {other.name} for {damage} damage!")
        else:
            print(f"{self.name} misses the attack on {other.name}!")

    def heal(self):
    # Increase hit points by a fixed amount
        heal_amount = 10  # Adjust this value as needed
        self.hit_points += heal_amount
        print(f"{self.name} uses a healing item and recovers {heal_amount} hit points.")


    def printStats(self):
        print(f"Name: {self.name}")
        print(f"Hit Points: {self.hit_points}")
        print(f"Hit Chance: {self.hit_chance}%")
        print(f"Max Damage: {self.max_damage}")
        print(f"Armor: {self.armor}")

def Fight(hero, monster):
    print("A battle begins!")
    
    while hero.is_alive() and monster.is_alive():
        input("Press <ENTER> to continue to the next round...")
        
        # Check hero's hit points
        if hero.hit_points <= 5:
            
            choice = input("Your hit points are low. Choose your action (fight/heal): ").lower()
            
            if choice == "heal":
                
                hero.heal()
                
                print("You use a healing item and recover some hit points.")
            else:
                hero.attack(monster)
                
                print(f"{hero.name} attacks {monster.name}...")
                
                if monster.is_alive():
                    
                    monster.attack(hero)
                    
                    print(f"{monster.name} attacks {hero.name}...")
        
        else:
            hero.attack(monster)
            
            print(f"{hero.name} attacks {monster.name}...")
            
            if monster.is_alive():
                
                monster.attack(hero)
                
                print(f"{monster.name} attacks {hero.name}...")
        
        print(f"{hero.name}: {hero.hit_points} HP")
        
        print(f"{monster.name}: {monster.hit_points} HP")
        
    if hero.is_alive():
        
        print(f"{monster.name} has been defeated!")
    else:
        print(f"{hero.name} has been defeated!")
