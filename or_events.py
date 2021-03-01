import random
import time
from functools import partial
from queue import SimpleQueue

from colorama import Back, Fore, Style
from rich.console import Console
from rich.table import Table

from or_globalvars import player, vars, vars2

console = Console()


def cold_weather():
    """Random event for cold weather"""
    # Checks for sufficient clothing
    vars.cold_weather = True
    enough_clothes = vars.amount_spent_on_clothing > 22 + (4 * random.random())
    c_message = "" if enough_clothes else "Don't "
    message = "\nCold weather, BRRRR! You {} have enough \
    clothing to keep you warm.\n".format(
        c_message
    )
    print(message)
    print("Press Enter to Continue...")
    if not enough_clothes:
        vars.is_sufficient_clothing = True
        vars.dead = True
        vars.death()


def heavy_rains():
    """Random event for heavy rain"""
    vars.raining = True
    print(f"\n{Fore.RED}Heavy rains...Time and supplies lost!{Fore.RESET}\n")
    # Removes random amount of food, bullets, random supplies
    vars.amount_spent_on_food -= 10
    vars.amount_spent_on_bullets -= 30
    vars.amount_spent_on_miscellaneous -= 15
    vars.total_mileage -= random.randint(5, 10)
    vars.raining = False


def got_shot():
    """Random event for getting shot"""
    print(
        f"\n{Fore.RED}You've been shot in the leg!\
 they take one of your oxen.{Fore.RESET}\n"
    )
    print(
        f"\n{Fore.BLUE}You ought to have a doctor look at \
your wound!{Fore.RESET}\n"
    )
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
        f"\n{Fore.RED}Your wagon breaks down! Time and supplies \
have been lost during repairs.{Fore.RESET}\n"
    )
    # Removes random amount of supplies, adds random miles
    vars.total_mileage -= random.randint(10, 15)
    vars.amount_spent_on_miscellaneous -= 8


def ox_injuries():
    """Random event for an ox injury"""
    print(
        f"\n{Fore.RED}An ox injures your leg! You are slowed \
for the rest of the trip...{Fore.RESET}\n"
    )
    # Increases amount spent on oxen, mileage
    vars.total_mileage -= 25
    vars.amount_spent_on_animals -= 20


def ox_wander():
    """Random event for an ox wandering off"""
    print(
        f"\n{Fore.RED}An ox wanders off, you take time to look for it.{Fore.RESET}\n"
    )
    # Adds 17 to mileage
    vars.total_mileage -= 17


def helpful_indians():
    """Random event for appearence of helpful indians"""
    print(
        f"\n{Fore.CYAN}Helpful Native Americans help you \
look for food!{Fore.RESET}\n"
    )
    # Adds extra food to inventory
    vars.amount_spent_on_food += 14


def unsafe_water():
    """Random event for using unsafe water"""
    print(
        f"\n{Fore.RED}Your water is contaminated, you take the time looking for a\
 fresh spring.{Fore.RESET}\n"
    )
    # Adds random amount to mileage
    vars.total_mileage -= random.randint(0, 8)


def wagon_fire():
    """Random event for a wagon fire"""
    print(
        f"\n{Fore.RED}A fire has erupted in your wagon!\
 Some food and supplies were lost...{Fore.RESET}\n"
    )
    # Removes random amount of food, bullets, supplies. Adds to mileage
    vars.amount_spent_on_food -= 40
    vars.amount_spent_on_bullets -= 25
    vars.amount_spent_on_miscellaneous -= random.randint(5, 8)
    vars.total_mileage -= 15


def heavy_fog():
    """Random event for heavy fog"""
    print(
        f"\n{Fore.RED}A thick fog rolls in and you spend \
time navigating through it{Fore.RESET}\n"
    )
    # Adds random amount to mileage
    vars.total_mileage -= random.randint(5, 10)


def snake_poison():
    """Random event for getting bitten"""
    if vars.amount_spent_on_miscellaneous < 0:
        print(
            f"\n{Fore.RED}You die of a snakebite as you have no medicine.{Fore.RESET}\n"
        )
        vars.dead = True
        vars.death()
    else:
        print(
            f"\n{Fore.RED}A poisonous snake bites you!{Fore.RESET}\
 {Fore.BLUE}Luckily you manage to kill it before it harms anybody else.\
{Fore.RESET}\n"
        )
        # Removes bullets, supplies.
        vars.amount_spent_on_bullets -= 10
        vars.amount_spent_on_miscellaneous -= 5
        # Determines if player has enough supplies to live, if not, player dies.


def wagon_swamped():
    """Random event for getting your wagon swamped"""
    print(
        f"\n{Fore.RED}The wagon gets swamped while traversing the river, \
some of your food and clothing gets lost.{Fore.RESET}\n"
    )
    # Removes some food, clothing. Adds mileage
    vars.amount_spent_on_food -= 30
    vars.amount_spent_on_clothing -= 20
    vars.total_mileage -= random.randint(0, 20)


def hail_storm():
    """Random event for a hail storm"""
    print(
        f"\n{Fore.RED}A hail storm rolls in! \
some of your supplies are damaged.{Fore.RESET}\n"
    )
    # Adds random amount to mileage, removes bullets and supplies
    vars.total_mileage -= random.randint(5, 10)
    vars.amount_spent_on_bullets -= 20
    vars.amount_spent_on_miscellaneous -= random.randint(4, 5)


def wrong_trail():
    """Random event for taking the wrong trail"""
    # Takes random number of days to add to current_date
    x = random.randint(2, 5)
    print(f"{Fore.RED}Wrong trail...You loose {x} days{Fore.RESET}")
    vars.current_date += x


def disease():
    """Random event for party member catching a disease"""
    vars2.rndmem()
    vars2.random_disease()
    print(
        f"\n{Fore.RED}{vars2.random_member} has {vars2.disease}.{Fore.RESET}\n"
    )
    print(
        f"{Fore.CYAN}You can use medicine on them or \
wait to see if they pull through.{Fore.RESET}\n"
    )
    # Input for if the player decides to give afflicted party member medicine
    # or not
    option = input("Use medicine? (Y/N): ")
    if option == "y":
        print(
            f"\n{Fore.CYAN}You give medicine to \
{vars2.random_member}.{Fore.RESET}\n"
        )
    elif option == "n":
        print(
            f"{Fore.BLUE}You decide not to \
give {vars2.random_member} medicine.{Fore.RESET}\n"
        )
        vars2.member_is_sick = True
    elif option == "exit":
        return False


def lost_member():
    """Random event for your son getting lost"""
    vars2.rndmem()
    print(
        f"\n{Fore.RED}{vars2.random_member} gets lost!\
 You spend the day looking for them...{Fore.RESET}\n"
    )
    # Adds 10 to mileage
    vars.total_mileage -= 10


def arm_broke():
    """Random event for a broken arm"""
    vars2.rndmem()
    print(
        f"\n{Fore.RED}Uh oh! {vars2.random_member} broke \
their arm!{Fore.RESET}\n"
    )
    print(
        f"\n{Fore.BLUE}You stop and use some supplies to make a \
sling.{Fore.RESET}\n"
    )
    # Increases amount spent on supplies, mileage
    vars.total_mileage -= random.randint(5, 10)
    vars.amount_spent_on_miscellaneous -= random.randint(5, 10)


def eating():
    """Determines if the food you eat will get you sick"""
    RND = random.random()
    if vars.choice_of_eating == 1:
        disease()
    elif vars.choice_of_eating == 3:
        if RND < 0.5:
            disease()
    else:
        if RND < 0.25:
            disease()


def animals_attack():
    """Random event for a wolf attack"""
    print(f"\n{Fore.RED}Wild animals attack your group!{Fore.RESET}\n")
    print(f"\n{Fore.RED}Prepare to draw...{Fore.RESET}")
    time.sleep(random.randint(1, 3))
    # Determines shooting level, whether you miss or not, or have enough bullets
    response_time = vars.shooting()
    if vars.amount_spent_on_bullets < 0:
        print(f"\n{Fore.RED}You were too low on bullets!{Fore.RESET}\n")
        print(f"\n{Fore.RED}The wolves overpower your group!{Fore.RESET}\n")
        vars.dead = True
        vars.death()
    # Determines if you were fast enough to win the battle
    if response_time <= 3.5:
        print(
            f"\n{Fore.CYAN}Nice shootin'! \
They didn't get much.{Fore.RESET}\n"
        )
    else:
        print(
            f"\n{Fore.RED}You were too slow on the draw, \
they took your food and clothes!{Fore.RESET}\n"
        )
        vars.amount_spent_on_bullets -= 10 * response_time
        vars.amount_spent_on_clothing -= 4 * response_time
        vars.amount_spent_on_food -= 1 * response_time


def bandits_attack():
    """Random event for a bandit attack"""
    print(f"\n{Fore.RED}Bandits attack!{Fore.RESET}\n")
    print(f"\n{Fore.RED}Prepare to draw...{Fore.RESET}")
    time.sleep(random.randint(1, 3))
    # Determines shooting level, whether you miss or not, or have enough bullets
    response_time = vars.shooting()
    vars.amount_spent_on_bullets -= 20 * response_time

    if vars.amount_spent_on_bullets < 0:
        print(
            f"\n{Fore.RED}You ran out of bullets! They take a bunch of\
 your {Fore.GREEN}money!{Fore.RESET}\n"
        )
        vars.cash_total //= 3
        vars.got_shot = True
    # Determines if you were fast enough to win the battle
    else:
        if response_time > 3:
            print(
                f"\n{Fore.RED}Too slow! They shot you.\
 Seek medical attention!{Fore.RESET}"
            )
            vars.amount_spent_on_bullets -= 10 * response_time
            vars.got_shot = True
        else:
            vars.amount_spent_on_bullets -= 1 * response_time
            print("\nQuickest draw outside of Dodge City!!\n")
            print("\nYou got 'em!\n")


def hunt():
    """Event for if the player chooses to hunt for more food"""
    # Determines if the player has enough bullets to hunt
    if vars.amount_spent_on_bullets <= 0:
        print("\nTough...You need more bullets to go hunting\n")
        input("Press Enter to Continue...")
    else:
        if vars.total_mileage > 45:
            vars.total_mileage += 20
        RND = random.randint(30, 50)
        # Determines if the player typed the word fast enough
        print("\nYou begin to look for animals...\n")
        time.sleep(2)
        print("\nFound one!\n")
        response_time = vars.shooting()
        if response_time < 2:
            print("Right between the eyes, you got a big one!!!")
            print("Full bellies tonight!")
            input("\nPress Enter to Continue...")
            vars.amount_spent_on_food += RND // 2
            vars.amount_spent_on_bullets -= RND // 3
        else:
            print("You missed and your dinner got away...")
            input("\nPress Enter to Continue...")
        if vars.amount_spent_on_bullets <= 0 and vars.cash_total <= 0:
            continue_on()


def choices():
    """Choices for what the player wants to do when passing a fort landmark"""
    console.clear()
    print(
        f"Do you want to: \n\n {Fore.BLUE}1. Stop at the fort\
\n 2. Hunt\n 3. Continue{Fore.RESET}\n"
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
            f"{Fore.RED}\nYou decide to continue on with no food or ammunition \
With no food and no ability to hunt, you \
starve to death{Fore.RESET}\n"
        )
        input("Press Enter to Continue")
        vars.death()
    else:
        return True


def fort():
    spacer = " " * 20
    oxen_price = 25.00
    clothing_price = 12.50
    ammunition_price = 2.50
    misc_price = 20.00
    food_price = 1.00

    console.clear()
    options = [
        f"{Back.WHITE + Fore.BLACK}  1. Oxen             {spacer}{oxen_price} \
per ox      ".ljust(
            50
        ),
        f"{Back.RESET + Fore.RESET}  2. Clothing         \
{spacer}{clothing_price} per set".ljust(
            50
        ),
        f"{Back.WHITE + Fore.BLACK}  3. Ammunition       \
{spacer}{ammunition_price} per box      ".ljust(
            50
        ),
        f"{Back.RESET + Fore.RESET}  4. Misc. Supplies   {spacer}{misc_price} \
per crate".ljust(
            50
        ),
        f"{Back.WHITE + Fore.BLACK}  5. Food             {spacer}{food_price} \
per pound    ".ljust(
            50
        ),
        f"{Back.RESET + Fore.RESET}  6. Leave store".ljust(50),
    ]
    print(f"\n{Fore.GREEN}You have ${vars.cash_total}{Fore.RESET}\n")
    print(f"{Fore.CYAN}You may buy:{Fore.RESET}\n")
    for i in options:
        print(i)

    selected = input("\nWhich number? ")

    if selected == "1":
        amount_ox = input(f"\n{Fore.CYAN}How many ox? {Fore.RESET}")

        if oxen_price * int(amount_ox) * 25 > vars.cash_total:
            print(f"{Fore.RED}You can't spend that much on oxen{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        if vars.cash_total <= 0:
            print(f"{Fore.RED} You can't spend any more.{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        elif vars.cash_total > 0:
            vars.cash_total = int(vars.cash_total - (int(amount_ox) * 25))
            vars.amount_spent_on_animals = int(
                (vars.amount_spent_on_animals + int(amount_ox) * 25)
            )
            fort()
        else:
            print(f"\n{Fore.RED}Please enter a number{Fore.RESET}\n")
        console.clear()

    if selected == "2":
        amount_sets = input(f"\n{Fore.CYAN}How many sets? {Fore.RESET}")

        if clothing_price * int(amount_sets) * 12.5 > vars.cash_total:
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
            vars.cash_total = int(vars.cash_total - (int(amount_sets) * 12.5))
            vars.amount_spent_on_clothing = int(
                (vars.amount_spent_on_clothing + int(amount_sets) * 12.5)
            )
            fort()
        else:
            print(f"\n{Fore.RED}Please enter a number{Fore.RESET}\n")
        console.clear()

    if selected == "3":
        amount_boxes = input(f"\n{Fore.CYAN}How many boxes? {Fore.RESET}")

        if ammunition_price * int(amount_boxes) * 2.5 > vars.cash_total:
            print(f"{Fore.RED}You can't spend that much on ammo{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        if vars.cash_total <= 0:
            print(f"{Fore.RED} You can't spend any more.{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        elif vars.cash_total > 0:
            vars.cash_total = int(vars.cash_total - (int(amount_boxes) * 2.5))
            vars.amount_spent_on_bullets = int(
                (vars.amount_spent_on_bullets + int(amount_boxes) * 2.5)
            )
            fort()
        else:
            print(f"\n{Fore.RED}Please enter a number{Fore.RESET}\n")
        console.clear()
    if selected == "4":
        amount_parts = input(f"\n{Fore.CYAN}How many boxes? {Fore.RESET}")

        if misc_price * int(amount_parts) > vars.cash_total:
            print(
                f"{Fore.RED}You can't spend that \
much on supplies{Fore.RESET}"
            )
            input("Press Enter to Continue...")
            fort()
        if vars.cash_total <= 0:
            print(f"{Fore.RED} You can't spend any more.{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        elif (
            vars.cash_total
            and int(vars.cash_total - int(amount_parts * 20)) >= 0
        ):
            vars.cash_total = int(vars.cash_total - (int(amount_parts) * 20))
            vars.amount_spent_on_bullets = int(
                (vars.amount_spent_on_bullets + int(amount_parts) * 20)
            )
            fort()
        else:
            print(f"\n{Fore.RED}Please enter a number{Fore.RESET}\n")
        console.clear()

    if selected == "5":
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
            print("\n{Fore.RED}Please enter a number{Fore.RESET}\n")
        console.clear()


def eating_quality():
    """Function for choosing how well the
    player wants to divide their rations"""
    console.clear()
    while vars.choice_of_eating > 0 or vars.choice_of_eating < 4:
        print(f"{Fore.CYAN}Change food rations{Fore.RESET}")
        print(f"\nCurrently {vars.food_quality}\n")
        print(
            f"{Fore.CYAN}The amount of food the people in your party\n\
eat each day can change. These amounts are: {Fore.RESET}"
        )
        print(
            f"\n{Fore.BLUE}  1. Filling - mesals are large and generous\n\
  2. Meager - meals are small, but adequate\n\
  3. Bare Bones - meals are very small; everyone stays hungry{Fore.RESET}\n"
        )
        vars.choice_of_eating = vars.input_int("What is your choice? ")
        if vars.choice_of_eating == 1:
            vars.food_quality = "Filling"
            vars.choice_of_eating = 1
            break
        if vars.choice_of_eating == 2:
            vars.food_quality = "Meager"
            vars.choice_of_eating = 2
            break
        if vars.choice_of_eating == 3:
            vars.food_quality = "Bare Bones"
            vars.choice_of_eating = 3
            break
        eaten = (vars.amount_spent_on_food - 8) - (5 * vars.choice_of_eating)
        if eaten < 0:
            print(f"{Fore.RED}You can't eat that well.{Fore.RESET}\n")
            input("Press Enter to Continue... ")
            continue


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
    wrong_trail,
]

if len(player.members) == 0:
    del events_list[15]


def events():
    """Function for determining which event occurs"""
    random.choice(events_list)()
    input("Press enter to Continue...")
