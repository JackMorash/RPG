from or_dates import choose_date
from rich import print
from or_player import player


def members():
    """Function determines names of party members"""
    mem_names = []
    print("What are the names of your other 4 party members?")
# Inputs for party member names
    member1 = input("\nFirst member: ")
    if member1 == "exit":
      return None
    member2 = input("\nSecond member: ")
    if member2 == "exit":
      return None
    member3 = input("\nThird member: ")
    if member3 == "exit":
      return None
    member4 = input("\nFourth member: ")
    if member4 == "exit":
      return None
    mem_names.append(member1)
    mem_names.append(member2)
    mem_names.append(member3)
    mem_names.append(member4)
    choose_date()
