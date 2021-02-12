from or_members import members
import or_player
from rich import print
from or_player import player
from rich.console import Console

console = Console()


def name():
    """Asks for a name for the player (wagon leader)"""
    print("\nWhat is the first name of the [blue]wagon leader?[/blue]")
    or_player.Player.name = input("\n--> ")
    console.clear()
    members()
