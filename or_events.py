import random

from rich import print

from or_globalvars import vars


def cold_weather():
    """Random event for cold weather"""
# Checks for sufficient clothing
    enough_clothes = vars.amount_spent_on_clothing > 22 + \
        (4 * random.random())
    c_message = "" if enough_clothes else "Don't "
    message = "[red]Cold weather, BRRRR! You {} have enough \
clothing to keep you warm.[/red]".format(
        c_message)
    print(message)
    if not enough_clothes:
        vars.is_sufficient_clothing = True
        vars.dead = True


def heavy_rains():
    """Random event for heavy rain"""
    print("Heavy rains...Time and supplies lost!")
# Removes random amount of food, bullets, random supplies
    vars.amount_spent_on_food -= 10
    vars.amount_spent_on_bullets -= 500
    vars.amount_spent_on_miscellaneous -= 15
    vars.total_mileage -= (10 * random.random()) - 5


def got_shot():
    """Random event for getting shot"""
    print("[red]You've been shot in the leg!\
 they take one of your oxen.[/red]")
    print("[blue]You ought to have a doctor look at your wound![/blue]")
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
    print("Your wagon breaks down! Time and supplies \
have been lost during repairs.")
# Removes random amount of supplies, adds random miles
    vars.total_mileage -= 15 - (5 * random.random())
    vars.amount_spent_on_miscellaneous -= 8


def ox_injuries():
    """Random event for an ox injury"""
    print("[red]An ox injures your leg! You are slowed \
for the rest of the trip...[/red]")
# Increases amount spent on oxen, mileage
    vars.total_mileage -= 25
    vars.amount_spent_on_animals -= 20


def arm_broke():
    """Random event for a broken arm"""
    print("[red]Uh oh! Your daughter broke her arm![/red]")
    print("[blue]You stop and use some supplies to make a sling.[/blue]")
# Increases amount spent on supplies, mileage
    vars.total_mileage -= 5 - (4 * random.random())
    vars.amount_spent_on_miscellaneous -= 2 - (3 * random.random())


def ox_wander():
    """Random event for an ox wandering off"""
    print("[red]An ox wanders off, you take time to look for it.[/red]")
# Adds random amount to mileage
    vars.total_mileage -= 17


def helpful_indians():
    """Random event for appearence of helpful indians"""
    print("[/cyan]Helpful Native Americans help you look for food![/cyan]")
# Adds extra food to inventory
    vars.amount_spent_on_food += 14


def lost_son():
    """Random event for your son getting lost"""
    print("[red]Your son gets lost!\
 You spend the day looking for him...[/red]")
# Adds random amount to mileage
    vars.total_mileage -= 10


def unsafe_water():
    """Random event for using unsafe water"""
    print("[red]The water is contaminated, you take the time looking for a\
 fresh spring.[/red]")
# Adds random amount to mileage
    vars.total_mileage -= (10*random.random()) - 2


def wagon_fire():
    """Random event for a wagon fire"""
    print("[red]A fire has erupted in your wagon!\
 Some food and supplies were lost...[/red]")
# Removes random amount of food, bullets, supplies. Adds to mileage
    vars.amount_spent_on_food -= 40
    vars.amount_spent_on_bullets -= 400
    vars.amount_spent_on_miscellaneous -= (8*random.random()) - 3
    vars.total_mileage -= 15


def heavy_fog():
    """Random event for heavy fog"""
    print("[red]A thick fog rolls in and you spend \
time navigating through it[/red]")
# Adds random amount to mileage
    vars.total_mileage -= 10 - (5*random.random())


def snake_poison():
    """Random event for getting bitten"""
    print("[red]A poisonous snake bites you![/red]\
 [blue]Luckily you manage to kill it before it harms anybody else.[/blue]")
# Removes bullets, supplies.
    vars.amount_spent_on_bullets -= 10
    vars.amount_spent_on_miscellaneous -= 5
# Determines if player has enough supplies to live, if not, player dies.
    if vars.amount_spent_on_miscellaneous < 0:
        print("[red]You die of a snakebite as you have no medicine.[/red]")
        vars.dead = True


def wagon_swamped():
    """Random event for getting your wagon swamped"""
    print("[red]The wagon gets swamped while traversing a river, \
some of your food and clothing gets lost.[/red]")
# Removes some food, clothing. Adds mileage
    vars.amount_spent_on_food -= 30
    vars.amount_spent_on_clothing -= 20
    vars.total_mileage -= 20 - (20*random.random())


def hail_storm():
    """Random event for a hail storm"""
    print("[red]A hail storm rolls in!\
 some of your supplies are damaged.[/red]")
# Adds random amount to mileage, removes bullets and supplies
    vars.total_mileage -= 5 - (10*random.random())
    vars.amount_spent_on_bullets -= 200
    vars.amount_spent_on_miscellaneous -= 4 - (3*random.random())


def eating():
    """Determines if the food you eat will get you sick"""
    RND = random.random()
    if vars.choice_of_eating == 1:
        vars.illness(vars)
    elif vars.choice_of_eating == 3:
        if RND < .5:
            vars.illness(vars)
    else:
        if RND < .25:
            vars.illness(vars)


def animals_attack():
    """Random event for a wolf attack"""
    print("[red]Wild animals attack your group![/red]")
# Determines shooting level, whether you miss or not, or have enough bullets
    response_time = vars.shooting(vars.shooting_level)
    if vars.amount_spent_on_bullets <= 38:
        print("[red]You were too low on bullets![/red]")
        print("[red]The wolves overpower your group![/red]")
        vars.is_injured = True
        vars.dead = True

    if response_time <= 2:
        print("[cyan italic]Nice shootin'! They didn't get much.[cyan italic]")
    else:
        print("[red]You were too slow on the draw, \
they took your food and clothes![/red]")
        vars.amount_spent_on_bullets -= (20 * response_time)
        vars.amount_spent_on_clothing -= (4 * response_time)
        vars.amount_spent_on_food -= (8 * response_time)


def bandits_attack():
    """Random event for a bandit attack"""
    print("[red]Bandits attack!")
# Determines shooting level, whether you miss or not, or have enough bullets
    response_time = vars.shooting(vars.shooting_level)
    vars.amount_spent_on_bullets -= (20 * response_time)

    if vars.amount_spent_on_bullets < 0:
        print("[red]You ran out of bullets! They take a bunch of\
 your [/red][green]money![/green]")
        vars.cash_total /= 3
        got_shot(vars)
    else:
        if response_time > 1:
            got_shot(vars)
        else:
            print("QUICKEST DRAW OUTSIDE OF DODGE CITY!!")
            print("You got 'em!")


# events array

events_list = [weather, wagon_break_down, ox_injuries, arm_broke,
               ox_wander, helpful_indians, lost_son, unsafe_water,
               wagon_fire, heavy_fog, snake_poison, wagon_swamped,
               hail_storm, eating, animals_attack, bandits_attack]


def events():
    """Function for determining which event occurs"""
    random.choice(events_list)()


events()
