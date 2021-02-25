import random
import time

from rich import print
from rich.console import Console
from rich.table import Table

from or_globalvars import vars

console = Console()


def cold_weather():
    """Random event for cold weather"""
    # Checks for sufficient clothing
    while True:
        vars.cold_weather == True
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


def arm_broke():
    """Random event for a broken arm"""
    print(f"\n[red]Uh oh! {vars.member} broke their arm![/red]\n")
    print("\n[blue]You stop and use some supplies to make a sling.[/blue]\n")
    # Increases amount spent on supplies, mileage
    vars.total_mileage -= random.randint(5, 10)
    vars.amount_spent_on_miscellaneous -= random.randint(5, 10)


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


def lost_member():
    """Random event for your son getting lost"""
    print(
        f"\n[red]{vars.member} gets lost!\
 You spend the day looking for them...[/red]\n"
    )
    # Adds 10 to mileage
    vars.total_mileage -= 10


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


def dysentary():
    vars.random_member()
    print(f"\n[red]{vars.member} has dysentary.[/red]\n")
    print(
        f"\n[cyan]You can use medicine on them or \
wait to see if they pull through.[/cyan]\n"
    )
    option = input("Use medicine? (Y/N): ").lower
    if option == "y":
        print(f"[cyan]You give medicine to {vars.member}.[cyan]\n")
    elif option == "n":
        print(
            f"\n[blue]You decide not to \
give {vars.member} medicine.[blue]\n"
        )
        if random.randint(0, 10) > 5:
            print(f"[red]{vars.member} has died of dysentary.\n")
            vars.member_is_dead = True
    elif option == "exit":
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
        "\n[red]A hail storm rolls in!\
 some of your supplies are damaged.[/red]\n"
    )
    # Adds random amount to mileage, removes bullets and supplies
    vars.total_mileage -= random.randint(5, 10)
    vars.amount_spent_on_bullets -= 200
    vars.amount_spent_on_miscellaneous -= random.randint(4, 5)


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
    # Determines shooting level, whether you miss or not, or have enough bullets
    response_time = vars.shooting()
    if vars.amount_spent_on_bullets <= 20:
        print("\n[red]You were too low on bullets![/red]\n")
        print("\n[red]The wolves overpower your group![/red]\n")
        vars.is_injured = True
        vars.dead = True
        vars.death()
        return False
    # Determines if you were fast enough to win the battle
    if response_time <= 3:
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
        if response_time > 1.5:
            print(
                "\n[red]Too slow! They shot you.\
 Seek medical attention![/red]"
            )
            vars.got_shot = True
        else:
            print("\nQUICKEST DRAW OUTSIDE OF DODGE CITY!!\n")
            print("\nYou got 'em!\n")


def hunt():
    if vars.amount_spent_on_bullets <= 39:
        print("\nTough...You need more bullets to go hunting\n")
        choices()
    else:
        vars.total_mileage -= 45
        RND = random.randint(30, 50)
        response_time = vars.shooting()
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
    choice = 0
    choices_1 = []
    if vars.has_fort:
        while choice < 1 or choice > 3:
            print(
                "[u]Do you want to:[/u] \n\n [blue]1. Stop at the next fort\
\n 2. Hunt\n 3. Continue[/blue]"
            )
            choice = vars.input_int("\n-->")
        choices_1 = [fort, hunt, continue_on]
    else:
        while choice < 1 or choice > 2:
            print(
                "[u]Do you want to:[/u] \n\n [blue]1. Stop at the next fort\
\n 2. Hunt\n 3. Continue[/blue]"
            )
            choice = vars.input_int("\n-->")
        choices_1 = [hunt, continue_on]
    choices_1[choice - 1]()


def continue_on():
    while True:
        if vars.amount_spent_on_food < 13:
            vars.dead = True
            print(
                "[red]\nYou decide to continue on with no food or ammunition\
 With no food and no ability to hunt, you \
starve to death[/red]\n"
            )
            input("\n-->")
            vars.death()
            return False
        else:
            break


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
        elif ValueError:
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
        elif ValueError:
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
        elif ValueError:
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
        elif ValueError:
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
        elif ValueError:
            print("[red]Please enter a number[/red]")
            continue
        console.clear()
        fort()


def fort():
    """Function for creating the fort UI"""
    while True:

        # Determines price of each type of item
        p = vars.amount_spent_on_miscellaneous * 10.00
        b = vars.amount_spent_on_bullets * 2.00
        c = vars.amount_spent_on_clothing * 40.00
        f = vars.amount_spent_on_food * 0.20
        o = vars.amount_spent_on_animals * 40.00
        # Creates fort UI using table library
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Goods")
        table.add_column("Cost", justify="right")
        # Creates "oxen" portion of the table
        table.add_row(
            "1. Oxen",
            f"[green]${vars.amount_spent_on_animals * 40.00}[/green]",
        )
        # Creates "food" portion of the table
        table.add_row(
            "2. Food",
            f"[green]${vars.amount_spent_on_food * 0.20}[/green]",
        )
        # Creates "clothing" portion of the table
        table.add_row(
            "3. Clothing",
            f"[green]${vars.amount_spent_on_clothing * 40.00}[/green]",
        )
        # Creates "ammunition" portion of the table
        table.add_row(
            "4. Ammunition",
            f"[green]${vars.amount_spent_on_bullets * 2.00}[/green]",
        )
        # Creates "parts" portion of the table
        table.add_row(
            "5. Spare Parts",
            f"[green]${vars.amount_spent_on_miscellaneous * 10.00}[/green]",
        )
        # Creates the total spent portion of the table
        table.add_row("\nTotal", f"\n[green]${o+f+c+b+p}[/green]")
        console.print(table)

        while True:
            # Displays and handles fort options and which option the player selects
            print(
                "Which item would you like to buy?\n\n[cyan italic]\
    Type 'leave' to exit the fort[/cyan italic]"
            )
            selection = input("\n-->")
            if selection == "1":
                console.clear()
                oxen()
                break
            elif selection == "2":
                console.clear()
                food()
                break
            elif selection == "3":
                console.clear()
                clothes()
                break
            elif selection == "4":
                console.clear()
                bullets()
                break
            elif selection == "5":
                console.clear()
                parts()
                break
            elif selection == "exit":
                console.clear()
                return None
            elif selection == ValueError:
                print("[bold red]Invalid Selection[/bold red]")
                continue
            elif selection == "leave":
                # Determines if the player has enough oxen to play the game
                if vars.amount_spent_on_animals < 1:
                    print(
                        "[cyan italic] Don't forget,\
    you'll need oxen to pull your wagon![/cyan italic]"
                    )
                    input("Press Enter to Continue...")
                    console.clear()


def spend(value, purse):
    if value > purse:
        print("You don't have that much...Keep spending down.")
        print("You missed your chance to spend on that item.")
        return purse, value, False
    return purse - value, value, True


def eating_quality():
    vars.choice_of_eating = 0
    while vars.choice_of_eating < 1 or vars.choice_of_eating > 3:
        vars.choice_of_eating = vars.input_int(
            "Do you want to eat \n1. Poorly\n2. Moderately\n3. Well"
        )
    eaten = (vars.amount_spent_on_food - 8) - (5 * vars.choice_of_eating)
    if eaten < 0:
        print("You can't eat that well.")
    else:
        vars.amount_spent_on_food = eaten
        vars.total_mileage += (
            vars.total_mileage + 200 + (vars.amount_spent_on_animals - 220)
        ) // random.randint(5, 10)
        vars.is_blizzard = vars.is_sufficient_clothing = False


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
    dysentary,
]


def events():
    """Function for determining which event occurs"""
    random.choice(events_list)()
    input("Press enter to Continue...")
