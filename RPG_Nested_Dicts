# Course: CS 30
# Period: 1
# Date Created: 21/01/29
# Date last Modified: 21/01/29
# Name: Jack Morash
# Description: Creates nested dictionaries for inventories,
# characters and locations

characters = {
    "Soldier": {
        "name": "Jack",
        "age": 17,
        "strength": "Strong"
    },
    "Wizard": {
        "name": "John",
        "age": 87,
        "strength": "Frail"
    }
}

# Prints the info for each character
print("Characters:")
for character, data in characters.items():
    print(f"""\
{character}:
    Name: {data["name"]}
    Age: {data["age"]}
    Strength: {data["strength"]}
    """)

# Inventory items held by each character
inventories = {
    "Wizard": ["Potion", "Staff", "Book"],
    "Soldier": ["Claymore", "Dagger"]
}

# Print the inventory items as a comma separated list
print("Inventories:")
for inventory, data in inventories.items():
    print(f"""\
{inventory}:
    {', '.join(data)}
    """)

# Descriptions of each location
locations = {
    "Castle": "A large medival castle in bavaria",
    "Forest": "A dense forest with elm trees sprawled for miles"
}

# Prints each location with its description
print("Locations:")
for location, data in locations.items():
    print(f"{location}: {data}")
