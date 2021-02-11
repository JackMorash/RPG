from or_members import members
import or_player
from rich import print
from or_player import player


def name():
    """Asks for a name for the player (wagon leader)"""
    print("\nWhat is the first name of the [blue]wagon leader?[/blue]")
    name = input("\n--> ")
    if name == "exit":
      return None
    members()
