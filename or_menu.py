import colorama
from colorama import Back, Fore, Style, init
from pynput import keyboard
from rich.console import Console

init()
console = Console()


def on_press(key):
    try:
        print(''.format(
            key.char))
    except AttributeError:
        print(''.format(
            key))


# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,)
listener.start()

options = [f"{Back.WHITE + Fore.BLACK}Start".ljust(50),
           f"{Back.RESET + Fore.RESET}Changelog".ljust(50),
           f"{Back.RESET + Fore.RESET}Exit".ljust(50)]


def main_menu():
    """Function for displaying main menu"""
    console.clear()
    while True:
        print("""[white]	
 _____                              _____         _ _ 	
|  _  |                            |_   _|       |_  |	
| | | |_ __ ___  __ _  ___  _ __     | |_ __ __ _ _| |	
| | | | '__/ _ \/ _` |/ _ \| '_ \    | | '__/ _` | | |	
\ \_/ / | |  __/ |_| | |_| | | | |   | | | | |_| | | |	
 \___/|_|  \___|\__, |\___/|_| |_|   \_/_|  \__,_|_|_|	
                 __/ |                                	
                |___/	[/white]
        \n \n[u]Welcome to [bold red]Oregon Trail[/bold red]: \
Python Edition![/u]\n""")

    # Menu option selection handlers
        if on_press("s") == "{s}":
            options[1] = f"{Back.RESET}Start"
        for i in options:
            print(i)
        break


main_menu()
