import random
from re import A
from threading import Event
from time import sleep

from pynput import keyboard
from rich import print
from rich.console import Console

import or_events
from or_dates import get_date
from or_globalvars import vars, vars2
from or_map import print_map

console = Console()


class KeyListener:
    def __init__(self):
        self.event = Event()

    def on_press(self, key):
        if key == keyboard.Key.space:
            self.event.set()

    def start(self):
        self.listener = keyboard.Listener(
            on_press=self.on_press, suppress=True
        )
        self.listener.start()

    def stop(self):
        self.listener.stop()
        self.event.clear()


listener = KeyListener()


def update():
    """Refreshed trail UI, updates date, mileage, checks player variables"""
    vars.current_date += 1
    vars.total_mileage += 15
    vars.amount_spent_on_food -= int(3 / vars.choice_of_eating)
    vars.hp()
    next_landmark()
    if vars2.member_is_sick == True:
        if random.randint(0, 100) < 10:
            print(
                f"[red]{vars2.random_member} \
has died of {vars2.disease}.\n"
            )
            vars2.dead_member()
            vars2.member_is_sick = False
            input("Press Enter to Continue... ")
    if vars.amount_spent_on_food <= 0:
        console.clear()
        print(
            "[red]You have run out of food. You and your party starve \
to death before reaching Oregon City...[/red]"
        )
        input("Press Enter to Continue...")
        vars.dead = True
        vars.death()
    if random.random() < 0.3:
        or_events.events()


def weather():
    """Function for determining weather type"""
    if vars.cold_weather == True:
        vars.weather = "Cold"
    elif vars.raining == True:
        vars.weather = "Rainy"
    else:
        vars.weather = "Fine"


def walking_trail():
    """Function for displaying main game UI"""
    while True:
        console.clear()
        if vars.dead == True:
            vars.death()
        # Prints UI

        print(
            f"""
                            {get_date().center(22)}
                     {(vars.location).center(35)}
███████████████████████████████████████████████████████████████████████████████

    [cyan italic]Weather: {vars.weather}[/cyan italic]
    [cyan italic]Health: {vars.health}[/cyan italic]
    [cyan italic]Rations: {vars.food_quality}[/cyan italic]
    [cyan italic]Next Landmark: {vars.distance_to_landmark} miles[/cyan italic]
    [cyan italic]Miles Traveled: {vars.total_mileage} miles[/cyan italic]

███████████████████████████████████████████████████████████████████████████████

[u italic]You May[/u italic]:

    [blue]1. Continue on Trail[/blue]
    [blue]2. Check map[/blue]
    [blue]3. Check Supplies[/blue]
    [blue]4. Hunt for food[/blue]
    [blue]5. Change food rations[/blue]
    [blue]6. Stop to rest[/blue]
    [blue]7. Talk to people[/blue]\n"""
        )
        # Determines which option the player selects from the UI
        option = input("What is your choice? ")
        if option == "1":
            begin()
        elif option == "2":
            print_map()
        elif option == "3":
            vars.print_inventory()
        elif option == "4":
            or_events.hunt()
        elif option == "exit".lower:
            return False
        elif option == "5":
            or_events.eating_quality()
        elif option == "6":
            or_events.wait()
        elif option == "exit":
            quit()
        if vars.reached_landmark == True:
            if option == "7":
                landmark_message()


def landmark_message():
    """Function for determining which message displays when selecting
    the "Talk to people" option. Based on location."""
    # Message if player has just begun
    if vars.location == "Independence, Missouri":
        console.clear()
        vars.message = f"""[blue]A traveller, Miles Hendricks, \
tells you:[/blue][i cyan]\n
"Did you read the Missouri Republican today? -- Says some\n \
folk start for Oregon without carrying spare parts, not even\n \
an extra wagon axle. Must think\n \
they grow on trees! Hope they're \
lucky enough to find an abandoned wagon[/i cyan]" 
"""
        print(vars.message)
        vars.cont()
    # Message if player has reached Kansas River
    if vars.location == "Kansas River":
        console.clear()
        vars.message = f"""[blue]A Ferry Operator tells you:[/blue]\n\n \
[i cyan]"Don't try to ford any river\ndeeper than the wagon bed --\n \
about two and a half feet.\n \
You'll swamp your wagon and loose your supplies. You can\n \
caulk the wagon bed and float\n \
it -- or be smart and hire me\n \
to take your wagon on my\n \
ferry!"[i cyan]
"""
        print(vars.message)
        vars.cont()
    # Message if player has reached Big Blue River
    if vars.location == "Big Blue River":
        console.clear()
        vars.message = f"""[blue]A lady, Marnie Stewart, \
tells you:[/blue]\n\n [i cyan]"This prairie is mighty pretty\n \
with all the wild flowers and\n \
tall grasses. But there's too\n \
much of it! I miss not having\n \
a town nearby. I wonder how \n \
many days until I see a town --\n \
a town with real shops, a \n \
church, people..."[i cyan]
"""
        print(vars.message)
        vars.cont()
    # Message if player has reached Fort Kearney
    if vars.location == "Fort Kearney":
        console.clear()
        vars.message = f"""[blue]A Fort Kearney scout \
tells you:[/blue]\n\n [i cyan]"The game is still plentiful\n \
along here, but gettin' harder\n \
to find. With so many\n \
overlanders, I don't expect it\n \
to last mor'n a few years.\n \
Folks shoot the game for sport,\n \
take a small piece, and let the\n \
rest rot in the sun"[i cyan]
"""
        print(vars.message)
        vars.cont()
    # Message if player has reached Chimney Rock
    if vars.location == "Chimney Rock":
        console.clear()
        vars.message = f"""[blue]Alonzo Delano \
tells you:[/blue]\n\n [i cyan]"About noon yesterday we came\n \
in sight of Chimney Rock\n \
looming up in the disance like\n \
the lofty tower of some town.\n \
We did not tire gazing on it.\n \
It was about 20 miles from us,\n \
and stayed in sight 'til we\n \
reached it today."[i cyan]
"""
        print(vars.message)
        vars.cont()
    # Message if player has reached Fort Laramie
    if vars.location == "Fort Laramie":
        console.clear()
        vars.message = f"""[blue]A woman traveller \
tells you:[/blue]\n\n [i cyan]"Be warned, stranger. Don't\n \
dig a water hole! Drink only\n \
river water. Salty as the\n \
Platte River is == it's better\n \
than the cholera. We buried my\n \
husband last week. Could use\n \
some help with this harness, if\n \
you can spare the time."[i cyan]
"""
        print(vars.message)
        vars.cont()
    # Message if player has reached Independence Rock
    if vars.location == "Independence Rock":
        console.clear()
        vars.message = f"""[blue]Aunt Rebecca Sims \
tells you:[/blue]\n\n [i cyan]"No butter or cheese or fresh\n \
fruit since Fort Laramie!\n \
Bless me, but I'd rather have\n \
my larder full of food back\n \
East than have our names carved\n \
on that rock! Well, tis a\n \
sight more cheery than all the\n \
graves we passed."[i cyan]
"""
        print(vars.message)
        vars.cont()
    # Message if player has reached South Pass
    if vars.location == "South Pass":
        console.clear()
        vars.message = f"""[blue]An Arapaho Indian \
tells you:[/blue]\n\n [i cyan]"When the white man first\n \
crossed our lands, their wagons\n \
were few. Now they crowd the\n \
trail in great numbers. The\n \
land is overgrazed with their\n \
many animals. Do white men\n \
still live in the East? My\n \
people talk of moving."[i cyan]
"""
        print(vars.message)
        vars.cont()
    # Message if player has reached Green River
    if vars.location == "Green River":
        console.clear()
        vars.message = f"""[blue]Big Louie \
tells you:[/blue]\n\n [i cyan]"Five dollars to ferry us over\n \
the Green River? Those\n \
ferrymen'll make a hundred\n \
dollars before breakfast!\n \
We'll keep down river until we\n \
fund a place to ford our wagon\n \
and animals. What little money\n \
we have left, we'll keep!"[i cyan]
"""
        print(vars.message)
        vars.cont()
    # Message if player has reached Soda Springs
    if vars.location == "Soda Springs":
        console.clear()
        vars.message = f"""[blue]A young boy \
tells you:[/blue]\n\n [i cyan]"My job every day is to find\n \
wood for the cook fire.\n \
Sometimes it's very hard to\n \
find enough, so I store extra\n \
pieces in a box under the\n \
wagon. On the prairie I\n \
gathered buffalo chips to burn\n \
when there wasn't any wood"[i cyan]
"""
        print(vars.message)
        vars.cont()
    # Message if player has reached Fort Hall
    if vars.location == "Fort Hall":
        console.clear()
        vars.message = f"""[blue]A fellow traveller \
tells you:[/blue]\n\n [i cyan]"Fort Hall is a busy fort! The\n \
wide stretches of meadow grass\n \
here are just what our tired\n \
animals need. As for me, I'll\n \
fix up the wagon leaks.\n \
Amanda's real anxious to wash\n \
all the clothes and linens in\n \
one of those clear streams."[i cyan]
"""
        print(vars.message)
        vars.cont()
    # Message if player has reached Snake River
    if vars.location == "Snake River":
        console.clear()
        vars.message = f"""[blue]Big Louie \
tells you:[/blue]\n\n [i cyan]"See that wild river? That's\n \
the Snake. Many a craft's been\n \
swamped in her foaming rapids.\n \
Her water travel all the way\n \
to Oregon! We'll be crossing\n \
her soon, and then again after\n \
Fort Boise. Take care at the\n \
crossing"[i cyan]
"""
        print(vars.message)
        vars.cont()
    # Message if player has reached Fort Boise
    if vars.location == "Fort Boise":
        console.clear()
        vars.message = f"""[blue]Aunt Rebecca \
tells you:[/blue]\n\n [i cyan]"At every fort along the trail,\n \
prices have been higher than at\n \
the previous fort! This is\n \
outrageous! They're taking\n \
advantage of us! If I had the\n \
chance to do it agian, I'd buy\n \
more supplies in Independence"[i cyan]
"""
        print(vars.message)
        vars.cont()
    # Message if player has reached Blue Mountains
    if vars.location == "Blue Mountains":
        console.clear()
        vars.message = f"""[blue]Marnie Stewart \
tells you:[/blue]\n\n [i cyan]"We followed the edge of the\n \
desert from Fort Boise to the\n \
forbidding wall of the Blue\n \
Mountains. The hills were\n \
deadful steep! Locking both\n \
wheels and coming down slow, we\n \
got down safe. Poor animals!\n \
No grass or water for days."[i cyan]
"""
        print(vars.message)
        vars.cont()
    # Message if player has reached The Dalles
    if vars.location == "The Dalles":
        console.clear()
        vars.message = f"""[blue]A toll collector \
tells you:[/blue]\n\n [i cyan]"I collect the tolls for the\n \
Barlow Road -- a bargain at\n \
twice the price! Until last\n \
year the overlander had no\n \
choice -- everyone floated the\n \
Columbia. Now with Mr.\n \
Barlow's new road, you can\n \
drive your wagon right into\n \
Oregon City!"[i cyan]
"""
        print(vars.message)
        vars.cont()


def begin():
    """Function for continueing on the trail"""
    while True:
        # Determines if player has reached Oregon City
        if vars.total_mileage >= vars.GOAL_IN_MILES:
            console.clear()
            print(
                "\n[green]Congratulations! You have finally made it to \
Oregon City. You've braved the periless west \
and can finally settle yourself and your party members![/green]"
            )
            input("Press Enter to Continue...")
            exit()

        # Determines if player has enough food to not starve to death
        if vars.amount_spent_on_food < 13:
            print(
                "\n[red]You'd better do some hunting \
or buy some food...And soon!![/red]\n"
            )
            input("\nPress Enter to Continue...")
        vars.total_mileage_previous_turn = vars.total_mileage
        # Determines if player can afford a doctor
        if vars.has_illness or vars.is_injured:
            vars.cash_total -= 20
            if vars.cash_total < 0:
                print(
                    "[red]Looks like you don't have enough money \
for a doctor... Guess you should have been born in a different country...\
And a different century...[/red]"
                )
                input("\nPress Enter to Continue...")
                vars.dead = True
                vars.death()
            # If player can afford a doctor, player is treated
            else:
                print(
                    "\n[blue]You go to get \
yourself treated by a doctor[/blue]"
                )
                print(
                    "\n[cyan]Doctor's bill is[/cyan] \
[green]$20[/green]\n"
                )
                input("\nPress Enter to Continue...")
                vars.is_injured = vars.has_illness = False
        # Calls function for determining if the player has reached landmark
        # assuming all prior if statements have been passed
        else:
            landmark()
        # Determines if the month has exceeded maximum number of days, if not,
        # keyboard listener is started, game loop begins
        if vars.current_date < 31:
            listener.start()
            size_up = listener.event.wait(1)
            listener.stop()
            if size_up:
                walking_trail()
                break
            else:
                update()
        # If month has exceeded 31 days, days resets to 1, next month occurs
        else:
            next_landmark()
            del vars.dates[0]
            vars.current_date = 1

        console.clear()
        # Ui for game loop
        print(
            f"""
                            {vars.location}
                     Press SPACE to size up the situation
███████████████████████████████████████████████████████████████████████████████

    [cyan italic]Date: {get_date()}[/cyan italic]
    [cyan italic]Weather: {vars.weather}[/cyan italic]
    [cyan italic]Health: {vars.health}[/cyan italic]
    [cyan italic]Food: {vars.amount_spent_on_food/0.2}[/cyan italic]
    [cyan italic]Next Landmark: {vars.distance_to_landmark} miles[/cyan italic]
    [cyan italic]Miles Traveled: {vars.total_mileage} miles[/cyan italic]

███████████████████████████████████████████████████████████████████████████████
            """
        )


def next_landmark():
    """Function determines how far the next landmark is"""
    if vars.location == "Independence, Missouri":
        vars.distance_to_landmark = -vars.total_mileage + 100
    if vars.location == "Kansas River":
        vars.distance_to_landmark = -vars.total_mileage + 185
    if vars.location == "Big Blue River":
        vars.distance_to_landmark = -vars.total_mileage + 300
    if vars.location == "Fort Kearney":
        vars.distance_to_landmark = -vars.total_mileage + 550
    if vars.location == "Chimney Rock":
        vars.distance_to_landmark = -vars.total_mileage + 650
    if vars.location == "Fort Laramie":
        vars.distance_to_landmark = -vars.total_mileage + 850
    if vars.location == "Independence Rock":
        vars.distance_to_landmark = -vars.total_mileage + 950
    if vars.location == "South Pass":
        vars.distance_to_landmark = -vars.total_mileage + 980
    if vars.location == "Green River" and vars.green_river_crossing == True:
        vars.distance_to_landmark = -vars.total_mileage + 1000
    if vars.location == "Soda Springs":
        vars.distance_to_landmark = -vars.total_mileage + 1100
    if vars.location == "Fort Bridger" and vars.fort_bridger == True:
        vars.distance_to_landmark = -vars.total_mileage + 1200
    if vars.location == "Snake River":
        vars.distance_to_landmark = -vars.total_mileage + 1370
    if vars.location == "Fort Boise":
        vars.distance_to_landmark = -vars.total_mileage + 1500
    if vars.location == "Grande Ronde Valley":
        vars.distance_to_landmark = -vars.total_mileage + 1650
    if vars.location == "Blue Mountains":
        vars.distance_to_landmark = -vars.total_mileage + 1700
    if vars.location == "Fort Walla Walla":
        vars.distance_to_landmark = -vars.total_mileage + 1800
    if vars.location == "The Dalles":
        vars.distance_to_landmark = -vars.total_mileage + 1770


def landmark():
    """Function determines which landmark the player should encounter based
    on how many miles the player has reached"""
    # Landmark flag for "Kansas River"
    if vars.total_mileage > 100 and vars.kansas_river_passed == False:
        if vars.kansas_river_passed == False:
            vars.location = "Kansas River"
            kansas_river()
            vars.kansas_river_passed = True
    # Landmark flag for "Big Blue River"
    if vars.total_mileage > 185 and vars.big_blue_river_passed == False:
        vars.location = "Big Blue River"
        big_blue_river()
        vars.big_blue_river_passed = True
    # Landmark flag for "Fort Kearney"
    if vars.total_mileage > 300 and vars.fort_kearney_passed == False:
        vars.location = "Fort Kearney"
        fort_kearney()
        vars.fort_kearney_passed = True
    # Landmark flag for "Chimney Rock"
    if vars.total_mileage > 550 and vars.chimney_rock_passed == False:
        vars.location = "Chimney Rock"
        chimney_rock()
        vars.chimney_rock_passed = True
    # Landmark flag for "Fort Laramie"
    if vars.current_date > 650 and vars.fort_laramie_passed == False:
        vars.location = "Fort Laramie"
        fort_laramie()
        vars.fort_laramie_passed = True
    # Landmark flag for "Independence Rock"
    if vars.total_mileage > 850 and vars.independence_rock_passed == False:
        vars.location = "Independence Rock"
        independence_rock()
        vars.independence_rock_passed = True
    # Landmark flag for "South Pass"
    if vars.total_mileage > 950 and vars.south_pass_passed == False:
        vars.location = "South Pass"
        south_pass()
        vars.south_pass_passed = True
    # Landmark flag for "Green River"
    if (
        vars.total_mileage > 980
        and vars.green_river_passed == False
        and green_river == True
    ):
        vars.location = "Green River"
        green_river()
        vars.green_river_passed = True
    # Landmark flag for "Soda Springs"
    if vars.total_mileage > 1000 and vars.soda_springs_passed == False:
        vars.location = "Soda Springs"
        soda_springs()
        vars.soda_springs_passed = True
    # Landmark flag for "Fort Bridger"
    if (
        vars.total_mileage > 1100
        and vars.fort_bridger_passed == False
        and fort_bridger == True
    ):
        vars.location = "Fort Bridger"
        fort_bridger()
        vars.fort_bridger_passed = True
    # Landmark flag for "Fort Hall"
    if vars.total_mileage > 1200 and vars.fort_hall_passed == False:
        vars.location = "Fort Hall"
        fort_hall()
        vars.fort_hall_passed = True
    # Landmark flag for "Snake River"
    if vars.total_mileage > 1370 and vars.snake_river_passed == False:
        vars.location = "Snake River"
        snake_river()
        vars.snake_river_passed = True
    # Landmark flag for "Fort Boise"
    if vars.total_mileage > 1500 and vars.fort_boise_passed == False:
        vars.location = "Fort Boise"
        fort_boise()
        vars.fort_boise_passed = True
    # Landmark flag for "Grande Ronde Valley"
    if vars.total_mileage > 1650 and vars.grande_ronde_valley_passed == False:
        vars.location = "Grande Ronde Valley"
        grande_ronde_valley()
        vars.grande_ronde_valley_passed = True
    # Landmark flag for "Blue Mountains"
    if vars.total_mileage > 1700 and vars.blue_mountains_passed == False:
        vars.location = "Blue Mountains"
        blue_mountains()
        vars.blue_mountains_passed = True
    # Landmark flag for "Fort Walla Walla"
    if (
        vars.total_mileage > 1800
        and vars.fort_walla_walla_passed == False
        and vars.fort_walla_walla == True
    ):
        vars.location = "Fort Walla Walla"
        fort_walla_walla()
        vars.fort_walla_walla_passed = True
    # Landmark flag for "The Dalles"
    if (
        vars.total_mileage > 1770
        and vars.the_dalles_passed == False
        and vars.the_dalles == True
    ):
        vars.location = "The Dalles"
        the_dalles()
        vars.the_dalles_passed = True


def kansas_river():
    """Function determines landmark properties for "Kansas River" """
    while True:
        a = 10
        b = 90
        x = random.randint(0, a)
        y = random.randint(0, b)
        console.clear()
        print(
            "\n[italic blue]You are now at the \
Kansas River Crossing[/italic blue]"
        )
        print(
            "\n[italic blue]You must cross the river in order to continue. \
The river at this point is currently 631 feet across and \
5.2 feet deep in the middle[/italic blue]"
        )
        print(
            f"\n[cyan]Weather: {vars.weather}\nRiver width: 631 Feet\n\
River depth: 5.2 Feet\n\n [u italic blue]You may: [/u italic blue][cyan]\n\n\
 1. Attempt to ford the river\n 2. Caulk the wagon and float it across\
 \n 3. Wait to see if the conditions improve\n 4. Get more information[/cyan]"
        )
        option = input("\n\nWhat is your choice? ")
        if option == "1" and x < 30:
            vars.kansas_river_passed = True
            or_events.wagon_swamped()
            input("\nPress Enter to Continue...")
            break
        if option == "1" and x > 30:
            vars.kansas_river_passed = True
            print(
                "\n[italic cyan]You had no \
trouble crossing the river[/italic cyan]"
            )
            input("\nPress Enter to Continue...")
            break
        elif option == "2" and y < 40:
            vars.kansas_river_passed = True
            or_events.wagon_swamped()
            input("\nPress Enter to Continue...")
            break
        elif option == "2" and y > 40:
            vars.kansas_river_passed = True
            print(
                "\n[italic cyan]You had no \
trouble crossing the river[/italic cyan]"
            )
            input("\nPress Enter to Continue...")
            break
        elif option == "3":
            vars.current_date += 1
            console.clear()
            print(
                "\n[blue]You decide to camp \
by the river for the night.[/blue]\n"
            )
            a = a * 2
            b = b * 2
            input("Press Enter to Continue...")
        elif option == "4":
            console.clear()
            print(
                "\n To ford a river means to\n pull your wagon across a\n\
 shallow part of the river,\n with the oxen still\n attached.\n"
            )
            input("\nPress Enter to Continue...\n")
            console.clear()
            print(
                "\n To calk the wagon means to\n seal it so that no water\
 can\n get in. The wagon can then\n be floated across like a\n boat.\n"
            )
            input("\nPress Enter to Continue...\n")
            console.clear()
            print(
                "\n To use a ferry means to put\n your wagon on top of a\
 flat\n boat that belongs to someone\n else. The owner of the\n ferry will\
 take your wagon\n across the river.\n"
            )
            input("\nPress Enter to Continue...\n")
        elif option == "exit":
            return False


def big_blue_river():
    """Function determines landmark properties for "Big Blue River" """
    while True:
        a = 90
        b = 200
        x = random.randint(0, a)
        y = random.randint(0, b)
        console.clear()
        print(
            "\n[italic blue]You are now at the [/italic blue]\
[cyan]Big Blue River Crossing[/cyan]"
        )
        print(
            "\n[italic blue]You must cross the river in order to continue. \
The river at this point is currently 235 feet across and \
3.1 feet deep in the middle[/italic blue]"
        )
        print(
            f"\n[cyan]Weather: {vars.weather}\nRiver width: 235 Feet\n\
River depth: 3.1 Feet\n [u italic blue]\nYou may: \n[/u italic blue][cyan]\n\
 1. Attempt to ford the river\n 2. Caulk the wagon and float it across\
 \n 3. Wait to see if the conditions improve\n 4. Get more information[/cyan]"
        )
        option = input("\nWhat is your choice? ")
        if option == "1" and x < 5:
            vars.big_blue_river_passed = True
            or_events.wagon_swamped()
            input("\nPress Enter to Continue...")
            break
        elif option == "1" and x > 5:
            vars.big_blue_river_passed = True
            print(
                "\n[italic cyan]You had no \
trouble crossing the river[/italic cyan]"
            )
            input("\nPress Enter to Continue...")
            break
        elif option == "2" and y < 30:
            vars.big_blue_river_passed = True
            or_events.wagon_swamped()
            input("Press Enter to Continue...")
            break
        elif option == "2" and y > 30:
            vars.big_blue_river_passed = True
            print(
                "\n[italic cyan]You had no \
trouble crossing the river[/italic cyan]"
            )
            input("\nPress Enter to Continue...")
            break
        elif option == "3":
            vars.current_date += 1
            console.clear()
            print(
                "\n[blue]You decide to camp \
by the river for the night.[/blue]\n"
            )
            a = a * 2
            b = b * 2
            input("Press Enter to Continue...")
        elif option == "4":
            console.clear()
            print(
                "\n To ford a river means to\n pull your wagon across a\n\
 shallow part of the river,\n with the oxen still\n attached.\n"
            )
            input("\nPress Enter to Continue...\n")
            console.clear()
            print(
                "\n To calk the wagon means to\n seal it so that no water\
 can\n get in. The wagon can then\n be floated across like a\n boat.\n"
            )
            input("\nPress Enter to Continue...\n")
            console.clear()
            print(
                "\n To use a ferry means to put\n your wagon on top of a\
 flat\n boat that belongs to someone\n else. The owner of the\n ferry will\
 take your wagon\n across the river.\n"
            )
            input("\nPress Enter to Continue...\n")
        elif option == "exit":
            return False


def fort_kearney():
    """Function determines landmark properties for "Fort Kearney" """
    console.clear()
    print(
        "[italic blue]You have arrived at [cyan]Fort Kearney[/cyan], \
take the time to buy some supplies...[/italic blue]"
    )
    input("Press Enter to Continue...")
    or_events.choices()


def chimney_rock():
    """Function determines landmark properties for "Chimney Rock" """
    console.clear()
    print(
        "[italic cyan]You have reached Chimney Rock, what a \
beautiful sight![/italic cyan]"
    )
    input("Press Enter to Continue...")


def fort_laramie():
    """Function determines landmark properties for "Fort Laramie" """
    console.clear()
    print(
        "[italic blue]You have arrived at [cyan]Fort Laramie[/cyan], \
take the time to buy some supplies...[/italic blue]"
    )
    input("Press Enter to Continue...")
    or_events.choices()


def independence_rock():
    """Function determines landmark properties for "Independence rock" """
    console.clear()
    print(
        "[italic cyan]You have reached Independence rock, \
it appears to be even grander than chimney rock...[/italic cyan]"
    )
    input("Press Enter to Continue...")


def south_pass():
    """Function determines landmark properties for "South Pass" """
    print(
        "[cyan]The trail divides here. You may:\n\n \
1. Head for Green River Crossing\n\n 2. Head for Fort Bridger\n\n \
3. See the map"
    )
    direction = vars.input_int("What is your choice? ")
    if direction == 1:
        vars.green_river_crossing = True
        vars.has_cleared_south_pass = True
    elif direction == 2:
        vars.fort_bridger = True
        vars.has_cleared_south_pass = True
    elif direction == 3:
        print_map()


def fort_bridger():
    """Function determines landmark properties for "Fort Bridger" """
    console.clear()
    print(
        "[italic blue]You have arrived at [cyan]Fort Bridger[/cyan], \
take the time to buy some supplies...[/italic blue]"
    )
    input("Press Enter to Continue...")
    or_events.choices()


def green_river():
    """Function determines landmark properties for "Green River" """
    while True:
        a = 90
        b = 200
        x = random.randint(0, a)
        y = random.randint(0, b)
        console.clear()
        print(
            "\n[italic blue]You are now at the [/italic blue]\
[cyan]Green River Crossing[/cyan]"
        )
        print(
            "\n[italic blue]You must cross the river in order to continue. \
The river at this point is currently 405 feet across and \
20.7 feet deep in the middle[/italic blue]"
        )
        print(
            f"\n[cyan]Weather: {vars.weather}\nRiver width: 405 Feet\n\
River depth: 20.7 Feet\n [u italic blue]\nYou may: \n[/u italic blue][cyan]\n\
 1. Attempt to ford the river\n 2. Caulk the wagon and float it across\
 \n 3. Wait to see if the conditions improve\n 4. Get more information[/cyan]"
        )
        option = input("\nWhat is your choice? ")
        if option == "1" and x < 5:
            vars.green_river_passed = True
            or_events.wagon_swamped()
            input("\nPress Enter to Continue...")
            break
        elif option == "1" and x > 5:
            vars.green_river_passed = True
            print(
                "\n[italic cyan]You had no \
trouble crossing the river[/italic cyan]"
            )
            input("\nPress Enter to Continue...")
            break
        elif option == "2" and y < 30:
            vars.green_river_passed = True
            or_events.wagon_swamped()
            input("Press Enter to Continue...")
            break
        elif option == "2" and y > 30:
            vars.green_river_passed = True
            print(
                "\n[italic cyan]You had no \
trouble crossing the river[/italic cyan]"
            )
            input("\nPress Enter to Continue...")
            break
        elif option == "3":
            vars.current_date += 1
            console.clear()
            print(
                "\n[blue]You decide to camp \
by the river for the night.[/blue]\n"
            )
            a = a * 2
            b = b * 2
            input("Press Enter to Continue...")
        elif option == "4":
            console.clear()
            print(
                "\n To ford a river means to\n pull your wagon across a\n\
 shallow part of the river,\n with the oxen still\n attached.\n"
            )
            input("\nPress Enter to Continue...\n")
            console.clear()
            print(
                "\n To calk the wagon means to\n seal it so that no water\
 can\n get in. The wagon can then\n be floated across like a\n boat.\n"
            )
            input("\nPress Enter to Continue...\n")
            console.clear()
            print(
                "\n To use a ferry means to put\n your wagon on top of a\
 flat\n boat that belongs to someone\n else. The owner of the\n ferry will\
 take your wagon\n across the river.\n"
            )
            input("\nPress Enter to Continue...\n")
        elif option == "exit":
            return False


def soda_springs():
    """Function determines landmark properties for "Soda Springs" """
    console.clear()
    print(
        "[italic cyan]You have reached Soda Springs, what a \
beautiful sight![/italic cyan]"
    )
    input("Press Enter to Continue...")


def fort_hall():
    """Function determines landmark properties for "Fort Hall" """
    console.clear()
    print(
        "[italic blue]You have arrived at [cyan]Fort Hall[/cyan], \
take the time to buy some supplies...[/italic blue]"
    )
    input("Press Enter to Continue...")
    or_events.choices()


def snake_river():
    """Function determines landmark properties for "Snake River" """
    while True:
        a = 90
        b = 200
        x = random.randint(0, a)
        y = random.randint(0, b)
        console.clear()
        print(
            "\n[italic blue]You are now at the [/italic blue]\
[cyan]Snake River Crossing[/cyan]"
        )
        print(
            "\n[italic blue]You must cross the river in order to continue. \
The river at this point is currently 1005 feet across and \
6.8 feet deep in the middle[/italic blue]"
        )
        print(
            f"\n[cyan]Weather: {vars.weather}\nRiver width: 1005 Feet\n\
River depth: 6.8 Feet\n [u italic blue]\nYou may: \n[/u italic blue][cyan]\n\
1. Attempt to ford the river\n 2. Caulk the wagon and float it across\
    \n 3. Wait to see if the conditions improve\n\
 4. Get more information[/cyan]"
        )
        option = input("\nWhat is your choice? ")
        if option == "1" and x < 5:
            vars.snake_river_passed = True
            or_events.wagon_swamped()
            input("\nPress Enter to Continue...")
            break
        elif option == "1" and x > 5:
            vars.snake_river_passed = True
            print(
                "\n[italic cyan]You had no \
trouble crossing the river[/italic cyan]"
            )
            input("\nPress Enter to Continue...")
            break
        elif option == "2" and y < 30:
            vars.snake_river_passed = True
            or_events.wagon_swamped()
            input("Press Enter to Continue...")
            break
        elif option == "2" and y > 30:
            vars.snake_river_passed = True
            print(
                "\n[italic cyan]You had no \
trouble crossing the river[/italic cyan]"
            )
            input("\nPress Enter to Continue...")
            break
        elif option == "3":
            vars.current_date += 1
            console.clear()
            print(
                "\n[blue]You decide to camp \
by the river for the night.[/blue]\n"
            )
            input("Press Enter to Continue...")
            a = a * 2
            b = b * 2
        elif option == "4":
            console.clear()
            print(
                "\n To ford a river means to\n pull your wagon across a\n\
shallow part of the river,\n with the oxen still\n attached.\n"
            )
            input("\nPress Enter to Continue...\n")
            console.clear()
            print(
                "\n To calk the wagon means to\n seal it so that no water\
can\n get in. The wagon can then\n be floated across like a\n boat.\n"
            )
            input("\nPress Enter to Continue...\n")
            console.clear()
            print(
                "\n To use a ferry means to put\n your wagon on top of a\
flat\n boat that belongs to someone\n else. The owner of the\n ferry will\
take your wagon\n across the river.\n"
            )
            input("\nPress Enter to Continue...\n")
        elif option == "exit":
            return False


def fort_boise():
    """Function determines landmark properties for "Fort Boise" """
    console.clear()
    print(
        "[italic blue]You have arrived at [cyan]Fort Boise[/cyan], \
take the time to buy some supplies...[/italic blue]"
    )
    input("Press Enter to Continue...")
    or_events.choices()


def grande_ronde_valley():
    """Function determines landmark properties for "Grande Ronde Valley" """
    console.clear()
    print(
        "[italic cyan]You have reached Grande Ronde Valley, what a \
beautiful sight![/italic cyan]"
    )
    input("Press Enter to Continue...")


def blue_mountains():
    """Function determines landmark properties for "Blue Mountains" """
    print(
        "[cyan]The trail divides here. You may:\n\n \
1. Head for Fort Walla Walla\n\n 2. Head for The Dalles\n\n 3. See the map"
    )
    direction = vars.input_int("What is your choice? ")
    if direction == 1:
        vars.fort_walla_walla = True
        vars.has_cleared_blue_montains = True
    elif direction == 2:
        vars.the_dalles = True
        vars.has_cleared_blue_montains = True
    elif direction == 3:
        print_map()


def fort_walla_walla():
    """Function determines landmark properties for "Fort Boise" """
    console.clear()
    print(
        "[italic blue]You have arrived at [cyan]Fort Walla Walla[/cyan], \
take the time to buy some supplies...[/italic blue]"
    )
    input("Press Enter to Continue...")
    or_events.fort()


def the_dalles():
    """Function determines landmark properties for "The Dalles" """
    console.clear()
    print(
        "[italic cyan]You have arrived in The Dalles, \
not far until Oregon City now![/italic cyan]"
    )
    input("Press Enter to Continue...")
