import or_player
from or_name import name
from rich import print
from or_player import player


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
            or_player.job = "Banker"
            break
        elif job == "2":
            print("\nYou have chosen to be the \
[bold cyan]Carpenter[/bold cyan]")
            or_player.Player.job = "Carpenter"
            break
        elif job == "3":
            print("\nYou have chosen to be the \
[bold cyan]Farmer[/bold cyan]\n")
            or_player.Player.job = "Farmer"
            break
        elif job == "exit":
          return None
        elif ValueError:
            print("\n[bold red]Invalid selection, please enter a number \
[/bold red]\n")
        continue
    name()
