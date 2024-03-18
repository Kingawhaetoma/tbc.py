# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:08:36 2024

@author: kinga
"""
import tbc

def main():
    hero = tbc.Character("Hero", 20, 50, 5, 2)

    monster = tbc.Character("Monster", 20, 30, 5, 0)

    hero.printStats()
    monster.printStats()

    tbc.Fight(hero, monster)

if __name__ == "__main__":
    main()

    




