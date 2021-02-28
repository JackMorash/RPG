import time

from rich import print
from rich.console import Console

from or_globalvars import player, vars
from or_store import matt_message

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
            print(
                "\nYou have chosen to be the \
[bold cyan]Banker[/bold cyan]\n"
            )
            player.job = "Banker"
            time.sleep(2)
            console.clear()
            break
        elif job == "2":
            print(
                "\nYou have chosen to be the \
[bold cyan]Carpenter[/bold cyan]"
            )
            player.job = "Carpenter"
            time.sleep(2)
            console.clear()
            break
        elif job == "3":
            print(
                "\nYou have chosen to be the \
[bold cyan]Farmer[/bold cyan]\n"
            )
            player.job = "Farmer"
            time.sleep(2)
            console.clear()
            break
        elif job == "exit":
            return None
        else:
            print(
                "\n[bold red]Invalid selection, please enter a number \
[/bold red]\n"
            )
    console.clear()
    name()


def members():
    """Function determines names of party members"""
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
    player.members.append(member1)
    player.members.append(member2)
    player.members.append(member3)
    player.members.append(member4)
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


def choose_date():
    """Displays storyline message, selects date for departure"""
    print(
        "\nIt is 1848, your jumping off place for Oregon is \
[red]Independence, Missouri[/red]. You must decide which month to \
leave [red]Independence[/red]"
    )
    print(
        "\n [green]1. March[green/]\n [green]2. April[/green]\n [green]\
3. May[/green]\n [green]4. June[/green]\n [green]5. July[/green]"
    )
    # Options for month of departure
    while True:
        month = input("\n-->")
        if month == "1":
            console.clear()
            matt_message()
            break
        elif month == "2":
            del vars.dates[0]
            console.clear()
            matt_message()
            break
        elif month == "3":
            del vars.dates[0:1]
            console.clear()
            matt_message()
            break
        elif month == "4":
            del vars.dates[0:2]
            console.clear()
            matt_message()
            break
        elif month == "5":
            del vars.dates[0:3]
            console.clear()
            matt_message()
            break
        elif month == "exit":
            console.clear()
            return None
        else:
            print("\n[red]Invalid Selection, please enter a number[/red]")
    console.clear()
