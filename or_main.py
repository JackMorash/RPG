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

from colorama import Back, Fore, Style
from pynput import keyboard
from rich.console import Console
from rich.markdown import Markdown

import or_jobs

console = Console()


options = ["Start".ljust(50),
           "Changelog".ljust(50),
           "Exit".ljust(50)]

selected = 0


def main_menu():
    """Function for displaying main menu"""
    console.clear()
    print(f"""
 _____                              _____         _ _
|  _  |                            |_   _|       |_  |
| | | |_ __ ___  __ _  ___  _ __     | |_ __ __ _ _| |
| | | | '__/ _ \/ _` |/ _ \| '_ \    | | '__/ _` | | |
\ \_/ / | |  __/ |_| | |_| | | | |   | | | | |_| | | |
 \___/|_|  \___|\__, |\___/|_| |_|   \_/_|  \__,_|_|_|
                 __/ |
                |___/    
        \n \nWelcome to {Fore.RED}Oregon Trail: \
{Fore.RESET}Python Edition!\n""")

    for i, option in enumerate(options):
        if (i == selected):
            print(Back.WHITE, Fore.BLACK, option, Back.RESET, Fore.RESET)
        else:
            print(option)
    print("\nUse the arrow keys and enter to navigate the menu")

def op():
    global selected
    if selected == 0:
        console.clear()
        or_jobs.job()
    elif selected == 1:
        console.clear()
        with open("changelog.md") as md:
            markdown = Markdown(md.read())
        console.print(markdown)
    elif selected == 2:
        return False
# main_menu()


def on_press(key):
    global selected
    if key == keyboard.Key.esc:
        # Stop listener
        return False

    if key == keyboard.Key.up and selected != 0:
        selected -= 1
    elif key == keyboard.Key.down and selected != len(options)-1:
        selected += 1
    elif key == keyboard.Key.enter:
        op()
        return False
    main_menu()


main_menu()
with keyboard.Listener(
        on_press=on_press, suppress=True) as listener:
    listener.join()
