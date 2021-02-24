import random

from rich import print

from or_globalvars import vars


def cold_weather():
    """Random event for cold weather"""
# Checks for sufficient clothing
    while True:
        vars.cold_weather == True
        enough_clothes = vars.amount_spent_on_clothing > 22 + \
            (4 * random.random())
        c_message = "" if enough_clothes else "Don't "
        message = "\n[red]Cold weather, BRRRR! You {} have enough \
    clothing to keep you warm.[/red]\n".format(
            c_message)
        print(message)
        if not enough_clothes:
            vars.is_sufficient_clothing = True
            vars.dead = True


def heavy_rains():
    """Random event for heavy rain"""
    while True:
        vars.raining = True
        print("\nHeavy rains...Time and supplies lost!\n")
    # Removes random amount of food, bullets, random supplies
        vars.amount_spent_on_food -= 10
        vars.amount_spent_on_bullets -= 500
        vars.amount_spent_on_miscellaneous -= 15
        vars.total_mileage -= (10 * random.random()) - 5
        break


def got_shot():
    """Random event for getting shot"""
    print("\n[red]You've been shot in the leg!\
 they take one of your oxen.[/red]\n")
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
    print("\n[red]Your wagon breaks down! Time and supplies \
have been lost during repairs.[/red]\n")
# Removes random amount of supplies, adds random miles
    vars.total_mileage -= 15 - (5 * random.random())
    vars.amount_spent_on_miscellaneous -= 8


def ox_injuries():
    """Random event for an ox injury"""
    print("\n[red]An ox injures your leg! You are slowed \
for the rest of the trip...[/red]\n")
# Increases amount spent on oxen, mileage
    vars.total_mileage -= 25
    vars.amount_spent_on_animals -= 20


def arm_broke():
    """Random event for a broken arm"""
    print("\n[red]Uh oh! Your daughter broke her arm![/red]\n")
    print("\n[blue]You stop and use some supplies to make a sling.[/blue]\n")
# Increases amount spent on supplies, mileage
    vars.total_mileage -= 5 - (4 * random.random())
    vars.amount_spent_on_miscellaneous -= 2 - (3 * random.random())


def ox_wander():
    """Random event for an ox wandering off"""
    print("\n[red]An ox wanders off, you take time to look for it.[/red]\n")
# Adds random amount to mileage
    vars.total_mileage -= 17


def helpful_indians():
    """Random event for appearence of helpful indians"""
    print("\n[cyan]Helpful Native Americans help you look for food![/cyan]\n")
# Adds extra food to inventory
    vars.amount_spent_on_food += 14


def lost_son():
    """Random event for your son getting lost"""
    print("\n[red]Your son gets lost!\
 You spend the day looking for him...[/red]\n")
# Adds random amount to mileage
    vars.total_mileage -= 10


def unsafe_water():
    """Random event for using unsafe water"""
    print("\n[red]The water is contaminated, you take the time looking for a\
 fresh spring.[/red]\n")
# Adds random amount to mileage
    vars.total_mileage -= (10*random.random()) - 2


def wagon_fire():
    """Random event for a wagon fire"""
    print("\n[red]A fire has erupted in your wagon!\
 Some food and supplies were lost...[/red]\n")
# Removes random amount of food, bullets, supplies. Adds to mileage
    vars.amount_spent_on_food -= 40
    vars.amount_spent_on_bullets -= 400
    vars.amount_spent_on_miscellaneous -= (8*random.random()) - 3
    vars.total_mileage -= 15


def heavy_fog():
    """Random event for heavy fog"""
    print("\n[red]A thick fog rolls in and you spend \
time navigating through it[/red]\n")
# Adds random amount to mileage
    vars.total_mileage -= 10 - (5*random.random())


def snake_poison():
    """Random event for getting bitten"""
    print("\n[red]A poisonous snake bites you![/red]\
 [blue]Luckily you manage to kill it before it harms anybody else.[/blue]\n")
# Removes bullets, supplies.
    vars.amount_spent_on_bullets -= 10
    vars.amount_spent_on_miscellaneous -= 5
# Determines if player has enough supplies to live, if not, player dies.
    if vars.amount_spent_on_miscellaneous < 0:
        print("\n[red]You die of a snakebite as you have no medicine.[/red]\n")
        vars.dead = True


def wagon_swamped():
    """Random event for getting your wagon swamped"""
    print("\n[red]The wagon gets swamped while traversing a river, \
some of your food and clothing gets lost.[/red]\n")
# Removes some food, clothing. Adds mileage
    vars.amount_spent_on_food -= 30
    vars.amount_spent_on_clothing -= 20
    vars.total_mileage -= 20 - (20*random.random())


def hail_storm():
    """Random event for a hail storm"""
    print("\n[red]A hail storm rolls in!\
 some of your supplies are damaged.[/red]\n")
# Adds random amount to mileage, removes bullets and supplies
    vars.total_mileage -= 5 - (10*random.random())
    vars.amount_spent_on_bullets -= 200
    vars.amount_spent_on_miscellaneous -= 4 - (3*random.random())


def eating():
    """Determines if the food you eat will get you sick"""
    RND = random.random()
    if vars.choice_of_eating == 1:
        vars.illness()
    elif vars.choice_of_eating == 3:
        if RND < .5:
            vars.illness()
    else:
        if RND < .25:
            vars.illness()


def animals_attack():
    """Random event for a wolf attack"""
    print("\n[red]Wild animals attack your group![/red]\n")
# Determines shooting level, whether you miss or not, or have enough bullets
    response_time = vars.shooting()
    if vars.amount_spent_on_bullets <= 38:
        print("\n[red]You were too low on bullets![/red]\n")
        print("\n[red]The wolves overpower your group![/red]\n")
        vars.is_injured = True
        vars.dead = True

    if response_time <= 2:
        print("\n[cyan italic]Nice shootin'! \
They didn't get much.[/cyan italic]\n")
    else:
        print("\n[red]You were too slow on the draw, \
they took your food and clothes![/red]\n")
        vars.amount_spent_on_bullets -= (20 * response_time)
        vars.amount_spent_on_clothing -= (4 * response_time)
        vars.amount_spent_on_food -= (8 * response_time)


def bandits_attack():
    """Random event for a bandit attack"""
    print("\n[red]Bandits attack![/red]\n")
# Determines shooting level, whether you miss or not, or have enough bullets
    response_time = vars.shooting()
    vars.amount_spent_on_bullets -= (20 * response_time)

    if vars.amount_spent_on_bullets < 0:
        print("\n[red]You ran out of bullets! They take a bunch of\
 your [/red][green]money![/green]\n")
        vars.cash_total /= 3
        vars.got_shot = True
    else:
        if response_time > 1:
            vars.got_shot = True
        else:
            print("\nQUICKEST DRAW OUTSIDE OF DODGE CITY!!\n")
            print("\nYou got 'em!\n")


# events array

events_list = [weather, wagon_break_down, ox_injuries, arm_broke,
               ox_wander, helpful_indians, lost_son, unsafe_water,
               wagon_fire, heavy_fog, snake_poison, wagon_swamped,
               hail_storm, eating, animals_attack, bandits_attack]


def events():
    """Function for determining which event occurs"""
    random.choice(events_list)()
