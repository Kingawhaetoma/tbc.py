# tbc.py
Character Class Documentation:

Description:
The Character class represents a character in a turn-based combat game. It includes attributes for the character's name, hit points, hit chance, maximum damage, and armor.

Planned Limitations:
1. Name: No specific limitations planned.
2. Hit Points: Should be a positive integer. There's no upper limit to hit points, but negative hit points indicate the character is defeated.
3. Hit Chance: Should be an integer between 0 and 100, representing the percentage chance of a successful attack.
4. Max Damage: Should be a positive integer. There's no upper limit to max damage.
5. Armor: Should be a non-negative integer, representing the amount of damage absorbed by the character's armor.

Algorithm for each method/function:

1. __init__(self, name, hit_points, hit_chance, max_damage, armor):
   - Description: Initializes a new instance of the Character class.
   - Inputs:
     - name: String representing the character's name.
     - hit_points: Integer representing the character's initial hit points.
     - hit_chance: Integer representing the character's hit chance (0 to 100).
     - max_damage: Integer representing the character's maximum damage.
     - armor: Integer representing the character's armor value.
   - Output: None
   - Steps:
     1. Set the name attribute to the provided name.
     2. Set the hit_points attribute to the provided hit_points.
     3. Set the hit_chance attribute to the provided hit_chance.
     4. Set the max_damage attribute to the provided max_damage.
     5. Set the armor attribute to the provided armor.

2. is_alive(self):
   - Description: Checks if the character is alive based on their hit points.
   - Inputs: None
   - Output: Boolean indicating whether the character is alive (True) or defeated (False).
   - Steps:
     1. Check if the hit_points attribute is greater than 0.
     2. Return True if the character is alive, otherwise return False.

3. attack(self, other):
   - Description: Performs an attack on another character.
   - Inputs:
     - other: Another instance of the Character class representing the target of the attack.
   - Output: None
   - Steps:
     1. Generate a random number between 1 and 100.
     2. If the random number is less than or equal to the attacker's hit_chance:
        a. Calculate the damage inflicted by generating a random number between 1 and the attacker's max_damage.
        b. Subtract the target's armor value from the calculated damage.
        c. Ensure the damage is non-negative.
        d. Subtract the final damage from the target's hit points.
        e. Print a message indicating the attack and the damage dealt.
     3. If the random number is greater than the hit_chance, print a message indicating a miss.

4. heal(self):
   - Description: Increases the character's hit points by a fixed amount.
   - Inputs: None
   - Output: None
   - Steps:
     1. Define a constant representing the amount of hit points to be healed.
     2. Add the healing amount to the character's hit points.
     3. Print a message indicating the healing action and the amount of hit points recovered.

5. printStats(self):
   - Description: Prints the character's attributes.
   - Inputs: None
   - Output: None
   - Steps:
     1. Print the character's name, hit points, hit chance, maximum damage, and armor attributes.

