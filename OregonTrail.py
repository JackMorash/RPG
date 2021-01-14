# Course: CS 30
# Period: 1
# Date Created: 21/01/14
# Date last Modified: 21/01/14
# Name: Jack Morash
# Description: Creates a numerical list of items from an inventory

food = ['Apple', 'Loaf of Bread']
weapons = ['Sword', 'Flail']
potions = ['Healing Potion', 'Swiftness Potion']

# Creates numerical list for food items

print(f"Food Items:")
for i, item in enumerate(food, 1):
    print(f"\n{i}. {item}")
print()

# Creates numerical list for weapons
# Note: I added weapons just to make sure in case they were required

print(f"Weapons:")
for i, item in enumerate(weapons, 1):
    print(f"\n{i}. {item}")
print()

# Creates numerical list for potions

print(f"Potions:")
for i, item in enumerate(food, 1):
    print(f"\n{i}. {item}")
print()
