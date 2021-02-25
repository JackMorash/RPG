import random
from re import A
from time import sleep

from rich import print
from rich.console import Console

import or_events
from or_dates import get_date
from or_globalvars import vars
from or_map import map

console = Console()


def update():
    vars.current_date += 1
    vars.total_mileage += 15
    if random.random() < 0.3:
        or_events.events()


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
    [cyan italic]Rations: {vars.amount_spent_on_food} lb of food [/cyan italic]

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
        vars.cash_total = vars.cash_total
        vars.total_mileage = vars.total_mileage
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
            landmark()
        if vars.current_date < 31:
            sleep(1)
            update()
        else:
            del vars.dates[0]
            vars.current_date = 1

        console.clear()
        print(f"""
                     Press ENTER to size up the situation
███████████████████████████████████████████████████████████████████████████████

    [cyan italic]Date: {get_date()}[/cyan italic]
    [cyan italic]Weather: {vars.weather}[/cyan italic]
    [cyan italic]Health: {vars.health}[/cyan italic]
    [cyan italic]Food: {vars.amount_spent_on_food}[/cyan italic]
    [cyan italic]Next Landmark:[/cyan italic]
    [cyan italic]Miles Traveled: {vars.total_mileage} miles[/cyan italic]

███████████████████████████████████████████████████████████████████████████████
""")


def landmark():
    if vars.total_mileage > 100:
        if vars.kansas_river_passed == False:
            kansas_river()
    if vars.total_mileage > 185:
        if vars.big_blue_river_passed == False:
            big_blue_river()
    if vars.total_mileage > 300:
        if vars.fort_kearney_passed == False:
            fort_kearney()


def kansas_river():
    while True:
        a = 10
        b = 90
        x = random.randint(0, a)
        y = random.randint(0, b)
        console.clear()
        print("\n[italic blue]You are now at the \
Kansas River Crossing[/italic blue]")
        print("\n[italic blue]You must cross the river in order to continue. \
The river at this point is currently 631 feet across and \
5.2 feet deep in the middle[/italic blue]")
        print(f"\n[cyan]Weather: {vars.weather}\nRiver width: 631 Feet\n\
River depth: 5.2 Feet\n\n [u italic blue]You may: [/u italic blue][cyan]\n\n\
 1. Attempt to ford the river\n 2. Caulk the wagon and float it across\
 \n 3. Wait to see if the conditions improve\n 4. Get more information[/cyan]")
        option = input("\n\nWhat is your choice? ")
        if option == "1":
            if x < 30:
                vars.kansas_river_passed = True
                or_events.wagon_swamped()
                input("\nPress Enter to Continue...")
                break
            if x > 30:
                vars.kansas_river_passed = True
                print("\n[italic cyan]You had no \
trouble crossing the river[/italic cyan]")
                input("\nPress Enter to Continue...")
                break
        elif option == "2":
            if y < 40:
                vars.kansas_river_passed = True
                or_events.wagon_swamped()
                input("\nPress Enter to Continue...")
                break
            if y > 40:
                vars.kansas_river_passed = True
                print("\n[italic cyan]You had no \
trouble crossing the river[/italic cyan]")
                input("\nPress Enter to Continue...")
                break
        elif option == "3":
            vars.current_date += 1
            console.clear()
            print("\n[blue]You decide to camp \
by the river for the night.[/blue]\n")
            a = a*2
            b = b*2
            input("Press Enter to Continue...")
        elif option == "4":
            console.clear()
            print("\n To ford a river means to\n pull your wagon across a\n\
 shallow part of the river,\n with the oxen still\n attached.\n")
            input("\nPress Enter to Continue...\n")
            console.clear()
            print("\n To calk the wagon means to\n seal it so that no water\
 can\n get in. The wagon can then\n be floated across like a\n boat.\n")
            input("\nPress Enter to Continue...\n")
            console.clear()
            print("\n To use a ferry means to put\n your wagon on top of a\
 flat\n boat that belongs to someone\n else. The owner of the\n ferry will\
 take your wagon\n across the river.\n")
            input("\nPress Enter to Continue...\n")
        elif option == "exit":
            return False


def big_blue_river():
    while True:
        a = 90
        b = 200
        x = random.randint(0, a)
        y = random.randint(0, b)
        console.clear()
        print("\n[italic blue]You are now at the \
Big Blue River Crossing[/italic blue]")
        print("\n[italic blue]You must cross the river in order to continue. \
The river at this point is currently 235 feet across and \
3.1 feet deep in the middle[/italic blue]")
        print(f"\n[cyan]Weather: {vars.weather}\nRiver width: 235 Feet\n\
River depth: 3.1 Feet\n [u italic blue]\nYou may: \n[/u italic blue][cyan]\n\
 1. Attempt to ford the river\n 2. Caulk the wagon and float it across\
 \n 3. Wait to see if the conditions improve\n 4. Get more information[/cyan]")
        option = input("\nWhat is your choice? ")
        if option == "1":
            if x < 5:
                vars.big_blue_river_passed = True
                or_events.wagon_swamped()
                input("\nPress Enter to Continue...")
                break
            if x > 5:
                vars.big_blue_river_passed = True
                print("\n[italic cyan]You had no \
trouble crossing the river[/italic cyan]")
                input("\nPress Enter to Continue...")
                break
        elif option == "2":
            if y < 30:
                vars.big_blue_river_passed = True
                or_events.wagon_swamped()
                input("Press Enter to Continue...")
                break
            if y > 30:
                vars.big_blue_river_passed = True
                print("\n[italic cyan]You had no \
trouble crossing the river[/italic cyan]")
                input("\nPress Enter to Continue...")
                break
            break
        elif option == "3":
            vars.current_date += 1
            console.clear()
            print("\n[blue]You decide to camp \
by the river for the night.[/blue]\n")
            a = a*2
            b = b*2
            input("Press Enter to Continue...")
        elif option == "4":
            console.clear()
            print("\n To ford a river means to\n pull your wagon across a\n\
 shallow part of the river,\n with the oxen still\n attached.\n")
            input("\nPress Enter to Continue...\n")
            console.clear()
            print("\n To calk the wagon means to\n seal it so that no water\
 can\n get in. The wagon can then\n be floated across like a\n boat.\n")
            input("\nPress Enter to Continue...\n")
            console.clear()
            print("\n To use a ferry means to put\n your wagon on top of a\
 flat\n boat that belongs to someone\n else. The owner of the\n ferry will\
 take your wagon\n across the river.\n")
            input("\nPress Enter to Continue...\n")
        elif option == "exit":
            return False


def fort_kearney():
    console.clear()
    print("[italic cyan]You have arrived at Fort Kearney, take the time to \
buy some supplies...[/italic cyan]")
    input("Press Enter to Continue...")
    or_events.fort()
    # def chimney_rock():


def fort_laramie():
    console.clear()
    print("[italic cyan]You have arrived at Fort Laramie, take the time to \
buy some supplies...[/italic cyan]")
    input("Press Enter to Continue...")
    or_events.fort()
    # def independence_rock():
    # def south_pass():


def fort_bridger():
    console.clear()
    print("[italic cyan]You have arrived at Fort Bridger, take the time to \
buy some supplies...[/italic cyan]")
    input("Press Enter to Continue...")
    or_events.fort()


def green_river():
    while True:
        a = 90
        b = 200
        x = random.randint(0, a)
        y = random.randint(0, b)
        console.clear()
        print("\n[italic blue]You are now at the \
Green River Crossing[/italic blue]")
        print("\n[italic blue]You must cross the river in order to continue. \
The river at this point is currently 235 feet across and \
3.1 feet deep in the middle[/italic blue]")
        print(f"\n[cyan]Weather: {vars.weather}\nRiver width: 235 Feet\n\
River depth: 3.1 Feet\n [u italic blue]\nYou may: \n[/u italic blue][cyan]\n\
 1. Attempt to ford the river\n 2. Caulk the wagon and float it across\
 \n 3. Wait to see if the conditions improve\n 4. Get more information[/cyan]")
        option = input("\nWhat is your choice? ")
        if option == "1":
            if x < 5:
                vars.green_river_passed = True
                or_events.wagon_swamped()
                input("\nPress Enter to Continue...")
                break
            if x > 5:
                vars.green_river_passed = True
                print("\n[italic cyan]You had no \
trouble crossing the river[/italic cyan]")
                input("\nPress Enter to Continue...")
                break
        elif option == "2":
            if y < 30:
                vars.green_river_passed = True
                or_events.wagon_swamped()
                input("Press Enter to Continue...")
                break
            if y > 30:
                vars.green_river_passed = True
                print("\n[italic cyan]You had no \
trouble crossing the river[/italic cyan]")
                input("\nPress Enter to Continue...")
                break
            break
        elif option == "3":
            vars.current_date += 1
            console.clear()
            print("\n[blue]You decide to camp \
by the river for the night.[/blue]\n")
            a = a*2
            b = b*2
            input("Press Enter to Continue...")
        elif option == "4":
            console.clear()
            print("\n To ford a river means to\n pull your wagon across a\n\
 shallow part of the river,\n with the oxen still\n attached.\n")
            input("\nPress Enter to Continue...\n")
            console.clear()
            print("\n To calk the wagon means to\n seal it so that no water\
 can\n get in. The wagon can then\n be floated across like a\n boat.\n")
            input("\nPress Enter to Continue...\n")
            console.clear()
            print("\n To use a ferry means to put\n your wagon on top of a\
 flat\n boat that belongs to someone\n else. The owner of the\n ferry will\
 take your wagon\n across the river.\n")
            input("\nPress Enter to Continue...\n")
        elif option == "exit":
            return False

    # def soda_springs():


def fort_hall():
    console.clear()
    print("[italic cyan]You have arrived at Fort Bridger, take the time to \
buy some supplies...[/italic cyan]")
    input("Press Enter to Continue...")
    or_events.fort()


def snake_river():
    while True:
        a = 90
        b = 200
        x = random.randint(0, a)
        y = random.randint(0, b)
        console.clear()
        print("\n[italic blue]You are now at the \
Snake River Crossing[/italic blue]")
        print("\n[italic blue]You must cross the river in order to continue. \
The river at this point is currently 235 feet across and \
3.1 feet deep in the middle[/italic blue]")
        print(f"\n[cyan]Weather: {vars.weather}\nRiver width: 235 Feet\n\
River depth: 3.1 Feet\n [u italic blue]\nYou may: \n[/u italic blue][cyan]\n\
1. Attempt to ford the river\n 2. Caulk the wagon and float it across\
    \n 3. Wait to see if the conditions improve\n\
 4. Get more information[/cyan]")
        option = input("\nWhat is your choice? ")
        if option == "1":
            if x < 5:
                vars.snake_river_passed = True
                or_events.wagon_swamped()
                input("\nPress Enter to Continue...")
                break
            if x > 5:
                vars.snake_river_passed = True
                print("\n[italic cyan]You had no \
trouble crossing the river[/italic cyan]")
                input("\nPress Enter to Continue...")
                break
        elif option == "2":
            if y < 30:
                vars.snake_river_passed = True
                or_events.wagon_swamped()
                input("Press Enter to Continue...")
                break
            if y > 30:
                vars.snake_river_passed = True
                print("\n[italic cyan]You had no \
trouble crossing the river[/italic cyan]")
                input("\nPress Enter to Continue...")
                break
            break
        elif option == "3":
            vars.current_date += 1
            console.clear()
            print("\n[blue]You decide to camp \
by the river for the night.[/blue]\n")
            input("Press Enter to Continue...")
            a = a*2
            b = b*2
        elif option == "4":
            console.clear()
            print("\n To ford a river means to\n pull your wagon across a\n\
shallow part of the river,\n with the oxen still\n attached.\n")
            input("\nPress Enter to Continue...\n")
            console.clear()
            print("\n To calk the wagon means to\n seal it so that no water\
can\n get in. The wagon can then\n be floated across like a\n boat.\n")
            input("\nPress Enter to Continue...\n")
            console.clear()
            print("\n To use a ferry means to put\n your wagon on top of a\
flat\n boat that belongs to someone\n else. The owner of the\n ferry will\
take your wagon\n across the river.\n")
            input("\nPress Enter to Continue...\n")
        elif option == "exit":
            return False


def fort_boise():
    console.clear()
    print("[italic cyan]You have arrived at Fort Boise, take the time to \
buy some supplies...[/italic cyan]")
    input("Press Enter to Continue...")
    or_events.fort()
    # def grande_ronde_valley():
    # def blue_mountains


def fort_walla_walla():
    console.clear()
    print("[italic cyan]You have arrived at Fort Walla Walla, take the time to\
 buy some supplies...[/italic cyan]")
    input("Press Enter to Continue...")
    or_events.fort()
    # def the_dalles


walking_trail()
