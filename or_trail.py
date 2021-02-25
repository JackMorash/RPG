import random
from functools import partial
from queue import SimpleQueue

import pynput
from pynput import keyboard
from rich import print
from rich.console import Console

import or_events
from or_dates import print_date
from or_globalvars import vars
from or_map import map

console = Console()


def weather():
    """Function for determining weather type"""
    if vars.cold_weather == True:
        vars.weather == "Cold"
    elif vars.raining == True:
        vars.weather == "Rainy"
    else:
        vars.weather == "Fine"


def walking_trail():
    """Function for displaying main game UI"""
    while True:
        console.clear()
        if vars.dead == True:
            vars.death()
            break
# Prints UI

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
    [blue]4. Hunt for food[/blue]
    """)
# Determines which option the player selects from the UI
        option = input("What is your choice? ")
        if option == "1":
            begin()
        elif option == "2":
            map()
        elif option == "3":
            vars.print_inventory()
        elif option == "4":
            or_events.hunt()
        elif option == "exit".lower:
            return False


def begin():
    while True:
        if vars.amount_spent_on_food < 13:
            print("\n[red]You'd better do some hunting\
    or buy some food...And soon!![/red]\n")
        vars.cash_total = int(vars.cash_total)
        vars.total_mileage = int(vars.total_mileage)
        vars.total_mileage_previous_turn = vars.total_mileage
        if vars.has_illness or vars.is_injured:
            vars.cash_total -= 20
            if vars.cash_total < 0:
                print("[red]Looks like you don't have enough money \
    for a doctor... Guess you should have been born in a different country...\
    And a different century...Unlucky[/red]")
                vars.dead = True
            else:
                print("\n[blue]You go to get \
    yourself treated by a doctor[/blue]\n")
                print("\n[cyan]Doctor's bill is[/cyan] [green]$20[/green]\n")
                vars.is_injured = vars.has_illness = False
        else:

            queue = SimpleQueue()

            def on_press(key):
                """Function handling menu navigation"""
                queue.put(key)

            listener = keyboard.Listener(
                on_press=on_press, suppress=True)
            listener.start()

            while True:
                console.clear()
                print(f"""
                     Press ENTER to size up the situation
███████████████████████████████████████████████████████████████████████████████
    
    [cyan italic]Date: {print_date}[/cyan italic]
    [cyan italic]Weather: {vars.weather}[/cyan italic]
    [cyan italic]Health: {vars.health}[/cyan italic]
    [cyan italic]Food: {vars.amount_spent_on_food}[/cyan italic]
    [cyan italic]Next Landmark:[/cyan italic]
    [cyan italic]Miles Traveled: {vars.total_mileage}[/cyan italic]

███████████████████████████████████████████████████████████████████████████████
                        Press SPACE BAR to continue
""")

                key = queue.get()
                if key == keyboard.Key.space:
                    listener.stop()
                    walking_trail()
                    break
                elif key == keyboard.Key.enter:
                    listener.stop()
                    walking_trail()
                    break
                elif key == keyboard.Key.esc:
                    listener.stop()
                    break


walking_trail()
