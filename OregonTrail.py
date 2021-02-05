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
from rich.table import Table

# Creates empty list for party member names
mem_names = []
console = Console()

# Create player class, defines various attrubutes applicable to the player


class Player:
    def __init__(self, name, job):
        self.name = name
        self.job = job
        self.money = 1600
        self.bullets = 0
        self.water = 0
        self.oxen = 0
        self.parts = 0
        self.medicine = 0
        self.clothes = 0
        self.food = 0
        self.cholera = False
        self.typhoid = False
        self.measles = False
        self.cold = False
        self.alive = True
        self.repair = False
        self.miles = 500


def name():
    """Asks for a name for the player (wagon leader)"""
    print("\nWhat is the first name of the [blue]wagon leader?[/blue]")
    Player.name = input("\n--> ")
    members()


def store():
    """Prints store message, creates store interface"""
    print("\n[cyan italic] Hello, I'm Matt. So you're going to Oregon! I can\
fix you up with what you need:\n\n\n - [blue]A team of oxen to pull your wagon\
\n - Clothing for both winter and summer[/blue]\n\n")
    key = input("Press Enter to continue")
    console = Console()
# Store interface, not yet able to interact
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Goods")
    table.add_column("Price", justify="right")
    table.add_row(
        "1. Oxen",
        "[green]$0[/green]"
    )
    table.add_row(
        "2. Food",
        "[green]$0[/green]",
    )
    table.add_row(
        "3. Clothing",
        "[green]$0[/green]"
    )
    table.add_row(
        "4. Ammunition",
        "[green]$0[/green]"
    )
    table.add_row(
        "5. Spare Parts",
        "[green]$0[/green]"
    )
    console.print(table)


def date():
    """Displays storyline message, selects date for departure"""
    print("\nIt is 1848, your jumping off place for Oregon is \
[red]Independence, Missouri[/red]. You must decide which month to \
leave [red]Independence[/red]")
    print("\n [green]1. March[green/]\n [green]2. April[/green]\n [green]\
3. May[/green]\n [green]4. June[/green]\n [green]5. July[/green]")
# Options for month of departure
    while True:
        month = input("\n-->")
        if month == "1":
            break
        elif month == "2":
            break
        elif month == "3":
            break
        elif month == "4":
            break
        elif month == "5":
            break
        else:
            print("\n[red]Invalid Selection, please enter a number[/red]")
        continue
    print(f"\nBefore leaving [red]Independence[/red] you should buy equipment \
and supplies. You have [green]$1600.00[/green] in cash, but you dont have to spend it \
all now.\n\n You can buy whatever you need at\
 [cyan]Matt's General Store[/cyan]")
    store()


# Asks for the names of party members, adds them to list
def members():
    """Function determines names of party members"""
    print("What are the names of your other 4 party members?")
# Inputs for party member names
    member1 = input("\nFirst member: ")
    member2 = input("\nSecond member: ")
    member3 = input("\nThird member: ")
    member4 = input("\nFourth member: ")
    mem_names.append(member1)
    mem_names.append(member2)
    mem_names.append(member3)
    mem_names.append(member4)
    date()


def job():
    """Function determines what job the player selects"""
    while True:
        print("\nMany kinds of people made the trip to Oregon")
        print("\n[u]You may:[/u]\n")
        print("1. Be a [bold cyan]Banker[/bold cyan] from [i]Boston[/i]\n\n")
        print("2. Be a [bold cyan]Carpenter[/bold cyan] from [i]Ohio[/i]\n\n")
        print("3. Be a [bold cyan]Farmer[/bold cyan] from [i]Illinois[/i]\n\n")
        print("[green]What is your choice?[/green]")
# Handles job input selection
        job = input("\n--> ")
        if job == "1":
            print("\nYou have chosen to be the \
[bold cyan]Banker[/bold cyan]\n")
            Player.job = "Banker"
            break
        elif job == "2":
            print("\nYou have chosen to be the \
[bold cyan]Carpenter[/bold cyan]")
            Player.job = "Carpenter"
            break
        elif job == "3":
            print("\nYou have chosen to be the \
[bold cyan]Farmer[/bold cyan]\n")
            Player.job = "Farmer"
            break
        elif ValueError:
            print("\n[bold red]Invalid selection, please enter a number \
[/bold red]\n")
        continue
    name()


while True:
    """Function for displaying main menu"""
    print(
        "\n \n [u]Welcome to [bold red]Oregon Trail[/bold red]: \
 Python Edition![/u]\n")

# Menu option selection handlers
    print("1.) Start")
    print("2.) Exit")
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
    else:
        print("[bold red]Invalid Selection[/bold red]")
