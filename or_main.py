# Course: CS 30
# Period: 1
# Date Created: 21/02/04
# Date last Modified: 21/02/05
# Name: Jack Morash
# Description: Final project for CS30,
# a remake of the original Oregon Trail CLI game from 1978
# originally written in BASIC, i've re-written it from scratch in Python.
import time

from rich import print
from rich.console import Console
from rich.markdown import Markdown

from or_jobs import job

# Creates empty list for party member names
mem_names = []
console = Console()

console.clear()


def menu():
    """Function for displaying main menu"""
    while True:
        print("""
 _____                              _____         _ _ 
|  _  |                            |_   _|       (_) |
| | | |_ __ ___  __ _  ___  _ __     | |_ __ __ _ _| |
| | | | '__/ _ \/ _` |/ _ \| '_ \    | | '__/ _` | | |
\ \_/ / | |  __/ (_| | (_) | | | |   | | | | (_| | | |
 \___/|_|  \___|\__, |\___/|_| |_|   \_/_|  \__,_|_|_|
                 __/ |                                
                |___/
        \n \n [u]Welcome to [bold red]Oregon Trail[/bold red]:\
Python Edition![/u]\n""")

    # Menu option selection handlers
        print("1.) Start")
        print("2.) Exit")
        print("3.) Changelog")
        option = input("\n--> ")
        if option == "start":
            console.clear()
            job()
            break
        elif option == "exit":
            return False
        elif option == "1":
            console.clear()
            job()
            break
        elif option == "2":
            return False
        elif option == "3":
            console.clear()
            with open("changelog.md") as md:
                markdown = Markdown(md.read())
            console.print(markdown)
        else:
            print("[bold red]Invalid Selection[/bold red]")
            time.sleep(3)
            continue


menu()
