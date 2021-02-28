import random
import time
from functools import partial
from queue import SimpleQueue

from colorama import Back, Fore, Style
from rich import print
from rich.console import Console
from rich.table import Table

from or_globalvars import player, vars, vars2

console = Console()


def cold_weather():
    """Random event for cold weather"""
    # Checks for sufficient clothing
    while True:
        vars.cold_weather = True
        enough_clothes = vars.amount_spent_on_clothing > 22 + (
            4 * random.random()
        )
        c_message = "" if enough_clothes else "Don't "
        message = "\n[red]Cold weather, BRRRR! You {} have enough \
    clothing to keep you warm.[/red]\n".format(
            c_message
        )
        print(message)
        if not enough_clothes:
            vars.is_sufficient_clothing = True
            vars.dead = True
            vars.death()
            return False


def heavy_rains():
    """Random event for heavy rain"""
    vars.raining = True
    print("\n[red]Heavy rains...Time and supplies lost![/red]\n")
    # Removes random amount of food, bullets, random supplies
    vars.amount_spent_on_food -= 10
    vars.amount_spent_on_bullets -= 500
    vars.amount_spent_on_miscellaneous -= 15
    vars.total_mileage -= random.randint(5, 10)
    vars.raining = False


def got_shot():
    """Random event for getting shot"""
    print(
        "\n[red]You've been shot in the leg!\
 they take one of your oxen.[/red]\n"
    )
    print("\n[blue]You ought to have a doctor look at your wound![/blue]\n")
    # Applies injured var. Removes random amount of supplies, oxen
    vars.is_injured = True
    vars.amount_spent_on_miscellaneous -= 5
    vars.amount_spent_on_animals -= 20


def weather():
    """Random event for handling both weather events"""
    # Determines what weather event to use
    if vars.total_mileage > vars.SOUTH_PASS_IN_MILES:
        cold_weather()
    else:
        heavy_rains()


def wagon_break_down():
    """Random event for wagon breaking down"""
    print(
        "\n[red]Your wagon breaks down! Time and supplies \
have been lost during repairs.[/red]\n"
    )
    # Removes random amount of supplies, adds random miles
    vars.total_mileage -= random.randint(10, 15)
    vars.amount_spent_on_miscellaneous -= 8


def ox_injuries():
    """Random event for an ox injury"""
    print(
        "\n[red]An ox injures your leg! You are slowed \
for the rest of the trip...[/red]\n"
    )
    # Increases amount spent on oxen, mileage
    vars.total_mileage -= 25
    vars.amount_spent_on_animals -= 20


def ox_wander():
    """Random event for an ox wandering off"""
    print("\n[red]An ox wanders off, you take time to look for it.[/red]\n")
    # Adds 17 to mileage
    vars.total_mileage -= 17


def helpful_indians():
    """Random event for appearence of helpful indians"""
    print("\n[cyan]Helpful Native Americans help you look for food![/cyan]\n")
    # Adds extra food to inventory
    vars.amount_spent_on_food += 14


def unsafe_water():
    """Random event for using unsafe water"""
    print(
        "\n[red]Your water is contaminated, you take the time looking for a\
 fresh spring.[/red]\n"
    )
    # Adds random amount to mileage
    vars.total_mileage -= random.randint(0, 8)


def wagon_fire():
    """Random event for a wagon fire"""
    print(
        "\n[red]A fire has erupted in your wagon!\
 Some food and supplies were lost...[/red]\n"
    )
    # Removes random amount of food, bullets, supplies. Adds to mileage
    vars.amount_spent_on_food -= 40
    vars.amount_spent_on_bullets -= 400
    vars.amount_spent_on_miscellaneous -= random.randint(5, 8)
    vars.total_mileage -= 15


def heavy_fog():
    """Random event for heavy fog"""
    print(
        "\n[red]A thick fog rolls in and you spend \
time navigating through it[/red]\n"
    )
    # Adds random amount to mileage
    vars.total_mileage -= random.randint(5, 10)


def snake_poison():
    """Random event for getting bitten"""
    print(
        "\n[red]A poisonous snake bites you![/red]\
 [blue]Luckily you manage to kill it before it harms anybody else.[/blue]\n"
    )
    # Removes bullets, supplies.
    vars.amount_spent_on_bullets -= 10
    vars.amount_spent_on_miscellaneous -= 5
    # Determines if player has enough supplies to live, if not, player dies.
    if vars.amount_spent_on_miscellaneous < 0:
        print("\n[red]You die of a snakebite as you have no medicine.[/red]\n")
        vars.dead = True
        vars.death()
        return False


def wagon_swamped():
    """Random event for getting your wagon swamped"""
    print(
        "\n[red]The wagon gets swamped while traversing the river, \
some of your food and clothing gets lost.[/red]\n"
    )
    # Removes some food, clothing. Adds mileage
    vars.amount_spent_on_food -= 30
    vars.amount_spent_on_clothing -= 20
    vars.total_mileage -= random.randint(0, 20)


def hail_storm():
    """Random event for a hail storm"""
    print(
        "\n[red]A hail storm rolls in! \
some of your supplies are damaged.[/red]\n"
    )
    # Adds random amount to mileage, removes bullets and supplies
    vars.total_mileage -= random.randint(5, 10)
    vars.amount_spent_on_bullets -= 200
    vars.amount_spent_on_miscellaneous -= random.randint(4, 5)


def wrong_trail():
    """Random event for taking the wrong trail"""
    # Takes random number of days to add to current_date
    x = random.randint(2, 5)
    print(f"[red]Wrong trail...You loose {x} days[/red]")
    vars.current_date += x


def disease():
    """Random event for party member catching a disease"""
    vars2.rndmem()
    vars2.random_disease()
    print(f"\n[red]{vars2.random_member} has {vars2.disease}.[/red]\n")
    print(
        f"[cyan]You can use medicine on them or \
wait to see if they pull through.[/cyan]\n"
    )
    # Input for if the player decides to give afflicted party member medicine
    # or not
    option = input("Use medicine? (Y/N): ")
    if option == "y":
        print(f"\n[cyan]You give medicine to {vars2.random_member}.[cyan]\n")
    elif option == "n":
        print(
            f"[blue]You decide not to \
give {vars2.random_member} medicine.[blue]\n"
        )
        vars2.member_is_sick = True
    elif option == "exit":
        return False


def lost_member():
    """Random event for your son getting lost"""
    vars2.rndmem()
    print(
        f"\n[red]{vars2.random_member} gets lost!\
 You spend the day looking for them...[/red]\n"
    )
    # Adds 10 to mileage
    vars.total_mileage -= 10


def arm_broke():
    """Random event for a broken arm"""
    vars2.rndmem()
    print(f"\n[red]Uh oh! {vars2.random_member} broke their arm![/red]\n")
    print("\n[blue]You stop and use some supplies to make a sling.[/blue]\n")
    # Increases amount spent on supplies, mileage
    vars.total_mileage -= random.randint(5, 10)
    vars.amount_spent_on_miscellaneous -= random.randint(5, 10)


def eating():
    """Determines if the food you eat will get you sick"""
    RND = random.random()
    if vars.choice_of_eating == 1:
        vars.illness()
    elif vars.choice_of_eating == 3:
        if RND < 0.5:
            vars.illness()
    else:
        if RND < 0.25:
            vars.illness()


def animals_attack():
    """Random event for a wolf attack"""
    print("\n[red]Wild animals attack your group![/red]\n")
    print("\n[red]Prepare to draw...[/red]")
    time.sleep(random.randint(1, 3))
    # Determines shooting level, whether you miss or not, or have enough bullets
    response_time = vars.shooting()
    if vars.amount_spent_on_bullets <= 20:
        print("\n[red]You were too low on bullets![/red]\n")
        print("\n[red]The wolves overpower your group![/red]\n")
        vars.dead = True
        vars.death()
        return False
    # Determines if you were fast enough to win the battle
    if response_time <= 3.5:
        print(
            "\n[cyan italic]Nice shootin'! \
They didn't get much.[/cyan italic]\n"
        )
    else:
        print(
            "\n[red]You were too slow on the draw, \
they took your food and clothes![/red]\n"
        )
        vars.amount_spent_on_bullets -= 10 * response_time
        vars.amount_spent_on_clothing -= 4 * response_time
        vars.amount_spent_on_food -= 8 * response_time


def bandits_attack():
    """Random event for a bandit attack"""
    print("\n[red]Bandits attack![/red]\n")
    print("\n[red]Prepare to draw...[/red]")
    time.sleep(random.randint(1, 3))
    # Determines shooting level, whether you miss or not, or have enough bullets
    response_time = vars.shooting()
    vars.amount_spent_on_bullets -= 20 * response_time

    if vars.amount_spent_on_bullets < 0:
        print(
            "\n[red]You ran out of bullets! They take a bunch of\
 your [/red][green]money![/green]\n"
        )
        vars.cash_total //= 3
        vars.got_shot = True
    # Determines if you were fast enough to win the battle
    else:
        if response_time > 3.5:
            print(
                "\n[red]Too slow! They shot you.\
 Seek medical attention![/red]"
            )
            vars.got_shot = True
        else:
            print("\nQUICKEST DRAW OUTSIDE OF DODGE CITY!!\n")
            print("\nYou got 'em!\n")


def hunt():
    """Event for if the player chooses to hunt for more food"""
    # Determines if the player has enough bullets to hunt
    if vars.amount_spent_on_bullets <= 39:
        print("\nTough...You need more bullets to go hunting\n")
        choices()
    else:
        vars.total_mileage -= 45
        RND = random.randint(30, 50)
        response_time = vars.shooting()
        # Determines if the player typed the word fast enough
        if response_time <= 1:
            print("\nYou begin to look for animals...\n")
            time.sleep(2)
            print("\nFound one!\n")
            print("Right between the eyes, you got a big one!!!")
            print("Full bellies tonight!")
            input("\n-->")
            vars.amount_spent_on_food = RND // 2
            vars.amount_spent_on_bullets = RND // 3
        elif 100 * RND < 2 * response_time:
            print("You missed and your dinner got away...")
            input("\nPress Enter to Continue...")
        else:
            print("Nice shot--Right on target--Good eatin' tonight!")
            vars.amount_spent_on_food = (vars.amount_spent_on_food + 48) - (
                2 * response_time
            )
            vars.amount_spent_on_bullets = (
                vars.amount_spent_on_bullets - 10
            ) - (3 * response_time)
        input("\n-->")
        continue_on()


def choices():
    """Choices for what the player wants to do when passing a fort landmark"""
    console.clear()
    print(
        "[u]Do you want to:[/u] \n\n [blue]1. Stop at the fort\
\n 2. Hunt\n 3. Continue[/blue]\n"
    )
    # Handles which option the player selects
    option = input("-->")
    if option == "1":
        fort()
    elif option == "2":
        hunt()
    elif option == "3":
        return True


def continue_on():
    """Determines if the player has enough food to live and if they have
    enough ammo to hunt"""
    if vars.amount_spent_on_food < 13:
        vars.dead = True
        print(
            "[red]\nYou decide to continue on with no food or ammunition \
With no food and no ability to hunt, you \
starve to death[/red]\n"
        )
        input("\n-->")
        vars.death()
        return False


def oxen():
    """Function for handling the purchase of oxen"""
    while True:
        print(
            "\n[cyan italic]There are 2 oxen in a yoke;\n\
I recommend at least 3 yoke.\nI charge [green]$40[/green] a yoke.\n\
[/cyan italic]"
        )
        amount = input("How many yoke do you want?: ")
        oxen_total = float(amount)
        if (oxen_total * 40.00) > vars.cash_total:
            print("[red]You can't spend that much on oxen[/red]")
            time.sleep(1.5)
            continue
        if vars.cash_total <= 0:
            print("\n[red] You can't spend any more.[/red]")
            time.sleep(1.5)
            console.clear()
            fort()
            continue
        elif vars.cash_total > 0:
            vars.cash_total = int(vars.cash_total - (oxen_total * 40.00))
            vars.amount_spent_on_animals = int(
                (vars.amount_spent_on_animals + oxen_total)
            )
            fort()
            break
        else:
            print("\n[red]Please enter a number[/red]\n")
            continue
        console.clear()
        fort()


def food():
    """Function for handling the purchase of food"""
    while True:
        print(
            "\n[cyan italic]I recommend you take at least 200 pounds of food\
 for each person in your group. I see that you have 5 people in total.\
 You'll need flour, sugar, bacon, and coffee.\
 My total is [green]¢20 a pound[/green][/cyan italic]\n"
        )
        amount = input("\nHow many pounds of food do you want?: ")
        food_total = float(amount)
        if (food_total * 0.20) > vars.cash_total:
            print("[red]You can't spend that much on food[/red]")
            time.sleep(1.5)
            continue
        if vars.cash_total <= 0:
            print("\n[red] You can't spend any more.[/red]")
            time.sleep(1.5)
            console.clear()
            fort()
            continue
        elif vars.cash_total > 0:
            vars.cash_total = int(vars.cash_total - (food_total * 0.20))
            vars.amount_spent_on_food = int(
                vars.amount_spent_on_food + food_total
            )
            console.clear()
            fort()
            break
        else:
            print("\n[red]Please enter a number[/red]\n")
        console.clear()
        fort()


def clothes():
    """Function for handling the purchase of clothes"""
    while True:
        print(
            "\n[cyan italic]You'll need warm clothing in the mountains.\
 I recommend taking at least 2 sets of clothes per person.\
 Each set is [green]$10.00.[/green][/cyan italic]\n"
        )
        amount = input(
            "\nHow many sets of\
 clothes do you want?: "
        )
        clothes_total = float(amount)
        if (clothes_total * 40.00) > vars.cash_total:
            print("[red]You can't spend that much on clothes[/red]")
            time.sleep(1.5)
            continue
        if vars.cash_total <= 0:
            print("\n[red] You can't spend any more.[/red]")
            time.sleep(1.5)
            console.clear()
            fort()
            break
        elif vars.cash_total > 0:
            vars.cash_total = int(vars.cash_total - (clothes_total * 40.00))
            vars.amount_spent_on_clothing = int(
                vars.amount_spent_on_clothing + clothes_total
            )
            console.clear()
            fort()
            break
        else:
            print("\n[red]Please enter a number[/red]\n")
            continue
        console.clear()
        fort()


def bullets():
    """Function for handling the purchase of bullets"""
    while True:
        print(
            "\n[cyan italic]I sell ammunition in boxes of 20 bullets. Each\
box costs [green]$2.00.[/green][/cyan italic]\n"
        )
        amount = input("\nHow many boxes do you want?: ")
        bullets_total = float(amount)
        # Determines if the player can spend enough bullets
        if (bullets_total * 2.00) > vars.cash_total:
            print(
                "[red]You can't buy that many bullets, it's not like\
you are an American or something...oh wait[/red]"
            )
            time.sleep(1.5)
            continue
        # Determines if the player can afford bullets
        if vars.cash_total <= 0:
            print("\n[red] You can't spend any more.[/red]\n")
            time.sleep(1.5)
            console.clear()
            fort()
            break
        # Adds bullets to total player bullets
        elif vars.cash_total > 0:
            vars.cash_total = int(vars.cash_total - (bullets_total * 2.00))
            vars.amount_spent_on_bullets = int(
                vars.amount_spent_on_bullets + bullets_total
            )
            console.clear()
            fort()
            break
        else:
            print("\n[red]Please enter a number[/red]\n")
            continue
        console.clear()
        fort()


def parts():
    """Function for handling the purchase of misc. parts"""
    while True:
        print(
            "\n[cyan italic]It's a good idea to have a few spare parts for\
 your wagon. Here are the totals:\
\nWagon wheel - [green]$10 each[/green]\
\nWagon axle - [green]$10 each[/green]\
\nWagon tongue - [green]$10 each[/green]\n"
        )
        amount1 = input("How many wagon wheels do you want?: ")
        amount2 = input("How many wagon axles do you want?: ")
        amount3 = input("How many wagon tongues do you want?: ")
        wheels = float(amount1)
        axles = float(amount2)
        tongues = float(amount3)
        parts_total = wheels + axles + tongues
        if (parts_total) > vars.cash_total:
            print("[red]You can't spend that much on spare parts[/red]")
            time.sleep(1.5)
            continue
        if vars.cash_total <= 0:
            print("\n[red] You can't spend any more.[/red]")
            time.sleep(1.5)
            console.clear()
            fort()
            break
        elif vars.cash_total > 0:
            vars.cash_total = int(vars.cash_total - (parts_total * 10.00))
            vars.amount_spent_on_miscellaneous = int(
                vars.amount_spent_on_miscellaneous + parts_total
            )
            console.clear()
            fort()
            break
        else:
            print("[red]Please enter a number[/red]")
            continue
        console.clear()
        fort()


def fort():
    spacer = " " * 20
    oxen_price = 25.00
    clothing_price = 12.50
    ammunition_price = 2.50
    wheels_price = 12.50
    axles_price = 12.50
    tounges_price = 12.50
    food_price = 0.25

    console.clear()
    options = [
        f"{Back.WHITE + Fore.BLACK}  1. Oxen         {spacer}{oxen_price} per ox      ".ljust(
            50
        ),
        f"{Back.RESET + Fore.RESET}  2. Clothing     {spacer}{clothing_price} per set".ljust(
            50
        ),
        f"{Back.WHITE + Fore.BLACK}  3. Ammunition   {spacer}{ammunition_price} per box      ".ljust(
            50
        ),
        f"{Back.RESET + Fore.RESET}  4. Wagon wheels {spacer}{wheels_price} per wheel".ljust(
            50
        ),
        f"{Back.WHITE + Fore.BLACK}  5. Wagon axles  {spacer}{axles_price} per axle    ".ljust(
            50
        ),
        f"{Back.RESET + Fore.RESET}  6. Wagon tounges{spacer}{tounges_price} per tounge  ".ljust(
            50
        ),
        f"{Back.WHITE + Fore.BLACK}  7. Food         {spacer}{food_price} per pound   ".ljust(
            50
        ),
        f"{Back.RESET + Fore.RESET}  8. Leave store".ljust(50),
    ]
    print(f"{Fore.CYAN}You may buy:{Fore.RESET}\n")
    for i in options:
        print(i)

    selected = input("\nWhich number? ")

    if selected == "1":
        amount_ox = input(f"\n{Fore.CYAN}How many ox? {Fore.RESET}")

        if oxen_price * int(amount_ox) > vars.cash_total:
            print(f"{Fore.RED}You can't spend that much on oxen{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        if vars.cash_total <= 0:
            print(f"{Fore.RED} You can't spend any more.{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        elif vars.cash_total > 0:
            vars.cash_total = int(vars.cash_total - (int(amount_ox)))
            vars.amount_spent_on_animals = int(
                (vars.amount_spent_on_animals + int(amount_ox))
            )
            fort()
        else:
            print("\n[red]Please enter a number[/red]\n")
        console.clear()

    if selected == "2":
        amount_sets = input(f"\n{Fore.CYAN}How many sets? {Fore.RESET}")

        if clothing_price * int(amount_sets) > vars.cash_total:
            print(
                f"{Fore.RED}You can't spend that much on clothing{Fore.RESET}"
            )
            input("Press Enter to Continue...")
            fort()
        if vars.cash_total <= 0:
            print(f"{Fore.RED} You can't spend any more.{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        elif vars.cash_total > 0:
            vars.cash_total = int(vars.cash_total - (int(amount_sets)))
            vars.amount_spent_on_clothing = int(
                (vars.amount_spent_on_clothing + int(amount_sets))
            )
            fort()
        else:
            print("\n[red]Please enter a number[/red]\n")
        console.clear()

    if selected == "3":
        amount_boxes = input(f"\n{Fore.CYAN}How many boxes? {Fore.RESET}")

        if ammunition_price * int(amount_boxes) > vars.cash_total:
            print(f"{Fore.RED}You can't spend that much on ammo{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        if vars.cash_total <= 0:
            print(f"{Fore.RED} You can't spend any more.{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        elif vars.cash_total > 0:
            vars.cash_total = int(vars.cash_total - (int(amount_boxes)))
            vars.amount_spent_on_bullets = int(
                (vars.amount_spent_on_bullets + int(amount_boxes))
            )
            fort()
        else:
            print("\n[red]Please enter a number[/red]\n")
        console.clear()
    if selected == "4":
        amount_wheels = input(f"\n{Fore.CYAN}How many wheels? {Fore.RESET}")

        if wheels_price * int(amount_wheels) > vars.cash_total:
            print(f"{Fore.RED}You can't spend that much on wheels{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        if vars.cash_total <= 0:
            print(f"{Fore.RED} You can't spend any more.{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        elif vars.cash_total > 0:
            vars.cash_total = int(vars.cash_total - (int(amount_wheels)))
            vars.amount_spent_on_miscellaneous = int(
                (vars.amount_spent_on_miscellaneous + int(amount_wheels))
            )
            fort()
        else:
            print("\n[red]Please enter a number[/red]\n")
        console.clear()

    if selected == "5":
        amount_axles = input(f"\n{Fore.CYAN}How many axles? {Fore.RESET}")

        if axles_price * int(amount_axles) > vars.cash_total:
            print(f"{Fore.RED}You can't spend that much on axles{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        if vars.cash_total <= 0:
            print(f"{Fore.RED} You can't spend any more.{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        elif vars.cash_total > 0:
            vars.cash_total = int(vars.cash_total - (int(amount_axles)))
            vars.amount_spent_on_miscellaneous = int(
                (vars.amount_spent_on_miscellaneous + int(amount_axles))
            )
            fort()
        else:
            print("\n[red]Please enter a number[/red]\n")
        console.clear()

    if selected == "6":
        amount_tounges = input(f"\n{Fore.CYAN}How many tounges? {Fore.RESET}")

        if tounges_price * int(amount_tounges) > vars.cash_total:
            print(
                f"{Fore.RED}You can't spend that much on tounges{Fore.RESET}"
            )
            input("Press Enter to Continue...")
            fort()
        if vars.cash_total <= 0:
            print(f"{Fore.RED} You can't spend any more.{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        elif vars.cash_total > 0:
            vars.cash_total = int(vars.cash_total - (int(amount_tounges)))
            vars.amount_spent_on_miscellaneous = int(
                (vars.amount_spent_on_miscellaneous + int(amount_tounges))
            )
            fort()
        else:
            print("\n[red]Please enter a number[/red]\n")
        console.clear()

    if selected == "7":
        amount_pounds = input(f"\n{Fore.CYAN}How many pounds? {Fore.RESET}")

        if food_price * int(amount_pounds) > vars.cash_total:
            print(f"{Fore.RED}You can't spend that much on food{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        if vars.cash_total <= 0:
            print(f"{Fore.RED} You can't spend any more.{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        elif vars.cash_total > 0:
            vars.cash_total = int(vars.cash_total - (int(amount_pounds)))
            vars.amount_spent_on_food = int(
                (vars.amount_spent_on_food + int(amount_pounds))
            )
            fort()
        else:
            print("\n[red]Please enter a number[/red]\n")
        console.clear()


def eating_quality():
    """Function for choosing how well the
    player wants to divide their rations"""
    console.clear()
    while vars.choice_of_eating > 0 or vars.choice_of_eating < 4:
        print("[u cyan]Change food rations[/u cyan]")
        print(f"\nCurrently {vars.food_quality}\n")
        print(
            "[cyan]The amount of food the people in your party\n\
eat each day can change. These amounts are: [/cyan]"
        )
        print(
            "\n[blue]  1. Filling - mesals are large and generous\n\
  2. Meager - meals are small, but adequate\n\
  3. Bare Bones - meals are very small; everyone stays hungry[/blue]\n"
        )
        vars.choice_of_eating = vars.input_int("What is your choice? ")
        if vars.choice_of_eating == 1:
            vars.food_quality = "Filling"
            vars.choice_of_eating = 1
        if vars.choice_of_eating == 2:
            vars.food_quality = "Meager"
            vars.choice_of_eating = 2
        if vars.choice_of_eating == 3:
            vars.food_quality = "Bare Bones"
            vars.choice_of_eating = 3
        eaten = (vars.amount_spent_on_food - 8) - (5 * vars.choice_of_eating)
        if eaten < 0:
            print("[red]You can't eat that well.[/red]\n")
            input("Press Enter to Continue... ")
        else:
            vars.amount_spent_on_food -= 200
            vars.total_mileage += (
                vars.total_mileage + 200 + (vars.amount_spent_on_animals - 220)
            ) // random.randint(5, 10)
            vars.is_blizzard = vars.is_sufficient_clothing = False
            break


def wait():
    console.clear()
    vars.current_date += int(input("How many days would you like to wait?: "))
    if vars.current_date > 31:
        del vars.dates[0]
        vars.current_date = 1


# events array
events_list = [
    weather,
    wagon_break_down,
    ox_injuries,
    arm_broke,
    ox_wander,
    helpful_indians,
    lost_member,
    unsafe_water,
    wagon_fire,
    heavy_fog,
    snake_poison,
    hail_storm,
    eating,
    animals_attack,
    bandits_attack,
    disease,
    wrong_trail,
]

if len(player.members) == 0:
    del events_list[15]


def events():
    """Function for determining which event occurs"""
    random.choice(events_list)()
    input("Press enter to Continue...")
