from rich import print
from rich.console import Console

import or_dates
import or_events
import or_map
from or_globalvars import vars

console = Console()


def weather():
    if vars.cold_weather == True:
        vars.weather == "Cold"
    elif vars.raining == True:
        vars.weather == "Rainy"
    else:
        vars.weather == "Fine"


def walking_trail(turn_number):
    while True:
        console.clear()
        print("{} {}, 1847".format(
            "SUNDAY", "MARCH 1"))
        print(f"""
███████████████████████████████████████████████████████████████████████████████
    
    [cyan italic]Weather: {vars.weather}[/cyan italic]
    [cyan italic]Health: {vars.health}[/cyan italic]
    [cyan italic]Pace:[/cyan italic]
    [cyan italic]Rations:[/cyan italic]

███████████████████████████████████████████████████████████████████████████████

[u italic]You May[/u italic]:
    
    [blue]1. Continue on Trail[/blue]
    [blue]2. Check map[/blue]
    [blue]3. Check Supplies[/blue]
    """)
        option = input("What is your choice? ")
        if option == "1":
            or_events.events()
        elif option == "2":
            or_map.map()
        elif option == "3":
            vars.print_inventory()
        elif option == "exit".lower:
            return False


walking_trail(1)
