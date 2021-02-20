from rich import print
from rich.console import Console

import or_player
from or_members import members
from or_player import player

console = Console()


def name():
    """Asks for a name for the player (wagon leader)"""
    print("\nWhat is the first name of the [blue]wagon leader?[/blue]")
    or_player.Player.name = input("\n--> ")
    console.clear()
    if input == "exit":
        return None
    elif input == ValueError:
        print("[bold red]Invalid Input[/bold red]")
    members()
