import random
import or_helpers


def cold_weather(this_vars):
    enough_clothes = this_vars.amount_spent_on_clothing > 22 + \
        (4 * random.random())
    c_message = "" if enough_clothes else "Don't "
    message = "[red]Cold weather, BRRRR! You {} have enough \
clothing to keep you warm.[/red]".format(
        c_message)
    print(message)
    if not enough_clothes:
        this_vars.is_sufficient_clothing = True
        this_vars.dead = True


def heavy_rains(this_vars):
    print("Heavy rains...Time and supplies lost!")
    this_vars.amount_spent_on_food -= 10
    this_vars.amount_spent_on_bullets -= 500
    this_vars.amount_spent_on_miscellaneous -= 15
    this_vars.total_mileage -= (10 * random.random()) - 5


def got_shot(this_vars):
    print("[red]You've been shot in the leg!\
 they take one of your oxen.[/red]")
    print("[blue]You ought to have a doctor look at your wound![/blue]")
    this_vars.is_injured = True
    this_vars.amount_spent_on_miscellaneous -= 5
    this_vars.amount_spent_on_animals -= 20


##### events array #####
def weather(this_vars):
    if this_vars.total_mileage > this_vars.SOUTH_PASS_IN_MILES:
        cold_weather(this_vars)
    else:
        heavy_rains(this_vars)


def wagon_break_down(this_vars):
    print("Your wagon breaks down! Time and supplies \
have been lost during repairs.")
    this_vars.total_mileage -= 15 - (5 * random.random())
    this_vars.amount_spent_on_miscellaneous -= 8


def ox_injuries(this_vars):
    print("[red]An ox injures your leg! You are slowed \
for the rest of the trip...[/red]")
    this_vars.total_mileage -= 25
    this_vars.amount_spent_on_animals -= 20


def arm_broke(this_vars):
    print("[red]Uh oh! Your daughter broke her arm![/red]")
    print("[blue]You stop and use some supplies to make a sling.[/blue]")
    this_vars.total_mileage -= 5 - (4 * random.random())
    this_vars.amount_spent_on_miscellaneous -= 2 - (3 * random.random())


def ox_wander(this_vars):
    print("[red]An ox wanders off, you take time to look for it.[/red]")
    this_vars.total_mileage -= 17


def helpful_indians(this_vars):
    print("[/cyan]Helpful Native Americans help you look for food![/cyan]")
    this_vars.amount_spent_on_food += 14


def lost_son(this_vars):
    print("[red]Your son gets lost!\
 You spend the day looking for him...[/red]")
    this_vars.total_mileage -= 10


def unsafe_water(this_vars):
    print("[red]The water is contaminated, you take the time looking for a\
 fresh spring.[/red]")
    this_vars.total_mileage -= (10*random.random()) - 2


def wagon_fire(this_vars):
    print("[red]A fire has erupted in your wagon!\
 Some food and supplies were lost...[/red]")
    this_vars.amount_spent_on_food -= 40
    this_vars.amount_spent_on_bullets -= 400
    this_vars.amount_spent_on_miscellaneous -= (8*random.random()) - 3
    this_vars.total_mileage -= 15


def heavy_fog(this_vars):
    print("[red]A thick fog rolls in and you spend \
time navigating through it[/red]")
    this_vars.total_mileage -= 10 - (5*random.random())


def snake_poison(this_vars):
    print("[red]A poisonous snake bites you![/red]\
 [blue]Luckily you manage to kill it before it harms anybody else.[/blue]")
    this_vars.amount_spent_on_bullets -= 10
    this_vars.amount_spent_on_miscellaneous -= 5
    if this_vars.amount_spent_on_miscellaneous < 0:
        print("[red]You die of a snakebite as you have no medicine.[/red]")
        this_vars.dead = True


def wagon_swamped(this_vars):
    print("[red]The wagon gets swamped while traversing a river, \
some of your food and clothing gets lost.[/red]")
    this_vars.amount_spent_on_food -= 30
    this_vars.amount_spent_on_clothing -= 20
    this_vars.total_mileage -= 20 - (20*random.random())


def hail_storm(this_vars):
    print("[red]A hail storm rolls in!\
 some of your supplies are damaged.[/red]")
    this_vars.total_mileage -= 5 - (10*random.random())
    this_vars.amount_spent_on_bullets -= 200
    this_vars.amount_spent_on_miscellaneous -= 4 - (3*random.random())


def eating(this_vars):
    RND = random.random()
    if this_vars.choice_of_eating == 1:
        or_helpers.illness(this_vars)
    elif this_vars.choice_of_eating == 3:
        if RND < .5:
            or_helpers.illness(this_vars)
    else:
        if RND < .25:
            or_helpers.illness(this_vars)


def animals_attack(this_vars):
    print("[red]Wild animals attack your group![/red]")
    response_time = or_helpers.shooting(this_vars.shooting_level)
    if this_vars.amount_spent_on_bullets <= 38:
        print("[red]You were too low on bullets![/red]")
        print("[red]The wolves overpower your group![/red]")
        this_vars.is_injured = True
        this_vars.dead = True
        return

    if response_time <= 2:
        print("[cyan italic]Nice shootin'! They didn't get much.[cyan italic]")
    else:
        print("[red]You were too slow on the draw, \
they took your food and clothes![/red]")
        this_vars.amount_spent_on_bullets -= (20 * response_time)
        this_vars.amount_spent_on_clothing -= (4 * response_time)
        this_vars.amount_spent_on_food -= (8 * response_time)


def bandits_attack(this_vars):
    print("[red]Bandits attack!")
    response_time = or_helpers.shooting(this_vars.shooting_level)
    this_vars.amount_spent_on_bullets -= (20 * response_time)

    if this_vars.amount_spent_on_bullets < 0:
        print("[red]You ran out of bullets! They take a bunch of\
 your [/red][green]money![/green]")
        this_vars.cash_total /= 3
        got_shot(this_vars)
    else:
        if response_time > 1:
            got_shot(this_vars)
        else:
            print("QUICKEST DRAW OUTSIDE OF DODGE CITY!!!")
            print("You got 'em!")


##### events array #####

events_list = [weather, wagon_break_down, ox_injuries, arm_broke,
               ox_wander, helpful_indians, lost_son, unsafe_water,
               wagon_fire, heavy_fog, snake_poison, wagon_swamped,
               hail_storm, eating, animals_attack, bandits_attack]


def events(this_vars):
    ev = random.choice(events_list)
    ev(this_vars)
