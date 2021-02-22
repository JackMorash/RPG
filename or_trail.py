from rich import print
from rich.console import Console

import or_dates
import or_events
import or_globalvars
import or_map

health = or_globalvars.health()
console = Console()


def weather():
    if vars.cold_weather == True:
        weather == "Cold"
    elif vars.raining == True:
        weather == "Rainy"
    else:
        weather == "Fine"


def walking_trail(turn_number):
    while True:
        console.clear()
        print("{} {}, 1847".format(
            "SUNDAY", "MARCH 1"))
        print(f"""
===============================================================================
    [cyan italic]Weather: {weather}[/cyan italic]
    [cyan italic]Health: {health}[/cyan italic]
    [cyan italic]Pace:[/cyan italic]
    [cyan italic]Rations:[/cyan italic]
===============================================================================
[u italic]You May[/u italic]:
    
    [u blue]1. Continue on Trail[/u blue]
    [u blue]2. Check supplies[/u blue]
    [u blue]3. Check map[/u blue]
    [u blue]4. Check Supplies[/u blue]
    """)
        option = input("What is your choice? ")
        if option == "1":
            or_events.events()
        elif option == "2":
            print()
        elif option == "3":
            or_map.map()
        elif option == "4":
            or_globalvars.print_inventory()
        elif option == "exit".lower:
            return False


walking_trail(1)
