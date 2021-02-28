# Course: CS 30
# Period: 1
# Date Created: 21/02/04
# Date last Modified: 21/02/05
# Name: Jack Morash
# Description: Final project for CS30,
# a remake of the original Oregon Trail CLI game from 1978
# originally written in BASIC, i've re-written it from scratch in Python.
# IMPORTANT: When running in repl, make sure to manually install the
# xlib package. You must also click into the VM window in order to operate
# the UI elements

from functools import partial
from queue import SimpleQueue

from colorama import Back, Fore, Style
from pynput import keyboard
from rich.console import Console
from rich.markdown import Markdown

import or_jobs

console = Console()


options = [
    "Start".ljust(50),
    "Learn about Oregon Trail".ljust(50),
    "Changelog".ljust(50),
    "Exit".ljust(50),
]

selected = 0
queue = SimpleQueue()


def main_menu():
    """Function for displaying main menu and options"""
    console.clear()
    print(
        fr"""{Fore.WHITE}
 _____                              _____         _ _
|  _  |                            |_   _|       |_  |
| | | |_ __ ___  __ _  ___  _ __     | |_ __ __ _ _| |
| | | | '__/ _ \/ _` |/ _ \| '_ \    | | '__/ _` | | |
\ \_/ / | |  __/ |_| | |_| | | | |   | | | | |_| | | |
 \___/|_|  \___|\__, |\___/|_| |_|   \_/_|  \__,_|_|_|
                 __/ |
                |___/
        
Welcome to {Fore.RED}Oregon Trail: {Fore.RESET}Python Edition!
"""
    )

    for i, option in enumerate(options):
        if i == selected:
            print(Back.WHITE, Fore.BLACK, option, Back.RESET, Fore.RESET)
        else:
            print(option)
    print("\nUse the arrow keys and enter to navigate the menu")


def message():
    """Displays the story of Oregon Trail"""
    console.clear()
    print(
        f"""    This program simulates a trip over the oregon trail from
    Independence, Missouri to Oregon City, Oregon in 1847.
    your family of five will cover the 2040 mile Oregon Trail
    in 5-6 months --- if you make it alive.
    You had saved {Fore.GREEN}$90{Fore.RESET} to spend for the trip,\
and you've just
    paid {Fore.GREEN}$200{Fore.RESET} for a wagon.
    You will need to spend the rest of your money on the
    following items:
    {Fore.CYAN}
        Oxen - you can spend {Fore.GREEN}$200-$300{Fore.CYAN} on your team
        the more you spend, the faster you'll go
        because you'll have better animals
        Food - the more you have, the less chance there
        is of getting sick
        Ammunition - 81 buys a belt of 50 bullets
        you will need bullets for attacks by animals
        and bandits, and for hunting food
        Clothing - this is especially important for the cold
        weather you will encounter when crossing the mountains
        Miscellaneous supplies - this includes medicine and
        other things you will need for sickness
        and emergency repairs
    {Fore.RESET}
    You can spend all your money before you start your trip -
    or you can save some of your cash to spend at forts along
    the way when you run low. However, items cost more at
    the forts. you can also go hunting along the way to get
    more food.
    Whenever you have to use your trusty rifle along the way,
    you will be told to type in a word (one that sounds like a
    gun shot). The faster you type in that word and hit the
    "return" key, the better luck you'll have with your gun.
    At each turn, all items are shown in dollar amounts
    except bullets
    when asked to enter money amounts, don't use a "$" "."
    good luck!!!
    """
    )
    input(f"\nPress Enter to Continue")
    console.clear()


def op(selected):
    """Function for determining what each selected option does"""
    if selected == 0:
        console.clear()
        or_jobs.job()
    elif selected == 1:
        message()
    elif selected == 2:
        console.clear()
        with open("changelog.md") as md:
            markdown = Markdown(md.read())
        console.print(markdown)
        input(f"\nPress Enter to Continue")
        console.clear()
    elif selected == 3:
        exit()


def on_press(key):
    """Function handling menu navigation"""
    queue.put(key)


listener = keyboard.Listener(on_press=on_press, suppress=True)
listener.start()

while True:
    main_menu()
    key = queue.get()
    if key == keyboard.Key.up and selected > 0:
        selected -= 1
    elif key == keyboard.Key.down and selected < len(options) - 1:
        selected += 1
    elif key == keyboard.Key.enter:
        if selected == 2:
            op(selected)
        else:
            listener.stop()
            op(selected)
    elif key == keyboard.Key.esc:
        listener.stop()
        break
main_menu()
