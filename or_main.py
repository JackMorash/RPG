# Course: CS 30
# Period: 1
# Date Created: 21/02/04
# Date last Modified: 21/02/05
# Name: Jack Morash
# Description: Final project for CS30,
# a remake of the original Oregon Trail CLI game from 1978
# originally written in BASIC, i've re-written it from scratch in Python.
from rich.console import Console
from rich.markdown import Markdown
from rich import print
from or_jobs import job
from or_player import player

# Creates empty list for party member names
mem_names = []
console = Console()


def menu():
    while True:
        """Function for displaying main menu"""
        print("\n \n [u]Welcome to [bold red]Oregon Trail[/bold red]:\
Python Edition![/u]\n")

    # Menu option selection handlers
        print("1.) Start")
        print("2.) Exit")
        print("3.) Changelog")
        option = input("\n--> ")
        if option == "start":
            job()
            break
        elif option == "exit":
            continue
        elif option == "1":
            job()
            break
        elif option == "2":
            continue
        elif option == "3":
            with open("changelog.md") as md:
                markdown = Markdown(md.read())
            console.print(markdown)
        else:
            print("[bold red]Invalid Selection[/bold red]")


menu()
