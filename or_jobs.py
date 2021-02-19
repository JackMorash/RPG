from rich import print
from rich.console import Console
import time
from or_dates import choose_date
from or_player import player
from rich.console import Console

console = Console()

console = Console()


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
            player.job = "Banker"
            time.sleep(2)
            console.clear()
            break
        elif job == "2":
            print("\nYou have chosen to be the \
[bold cyan]Carpenter[/bold cyan]")
            player.Player.job = "Carpenter"
            time.sleep(2)
            console.clear()
            break
        elif job == "3":
            print("\nYou have chosen to be the \
[bold cyan]Farmer[/bold cyan]\n")
            player.Player.job = "Farmer"
            time.sleep(2)
            console.clear()
            break
        elif job == "exit":
            return None
        elif ValueError:
            print("\n[bold red]Invalid selection, please enter a number \
[/bold red]\n")
        continue
    console.clear()
    name()


def members():
    """Function determines names of party members"""
    mem_names = []
    print("What are the names of your other 4 party members?")
# Inputs for party member names
    member1 = input("\nFirst member: ")
    if member1 == "exit":
        console.clear()
        return None
    member2 = input("\nSecond member: ")
    if member2 == "exit":
        console.clear()
        return None
    member3 = input("\nThird member: ")
    if member3 == "exit":
        console.clear()
        return None
    member4 = input("\nFourth member: ")
    if member4 == "exit":
        console.clear()
        return None
    mem_names.append(member1)
    mem_names.append(member2)
    mem_names.append(member3)
    mem_names.append(member4)
    console.clear()
    choose_date()


def name():
    """Asks for a name for the player (wagon leader)"""
    print("\nWhat is the first name of the [blue]wagon leader?[/blue]")
    name = input("\n--> ")
    if name == "exit":
        console.clear()
        return None
    console.clear()
    members()
