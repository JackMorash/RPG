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

# Create player class, defines various attrubutes applicable to the player


class Player:
    def __init__(self, name, job):
        self.name = name
        self.job = job
        self.money = 0
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
# The main menu, as well as
# the name selection and explainations of various story


def menu():
    while True:
        print("\nMany kinds of people made the trip to Oregon")
        print("\n[u]You may:[/u]\n")
        print("1. Be a [bold cyan]Banker[/bold cyan] from [i]Boston[/i]\n\n")
        print("2. Be a [bold cyan]Carpenter[/bold cyan] from [i]Ohio[/i]\n\n")
        print("3. Be a [bold cyan]Farmer[/bold cyan] from [i]Illinois[/i]\n\n")
        print("[green]What is your choice?[/green]")
        player = input("\n-->")
        if player == "1":
            print(
                "You have chosen to be the [bold cyan]Banker[/bold cyan], \
is this correct?[Y/N]")
            input("\n-->")
            if input == "y":
                break
        elif player == "2":
            print(
                "You have chosen to be the [bold cyan]Carpenter[/bold cyan], \
is this correct?[Y/N]")
            input("\n-->")
            if input == "y":
                break
        elif player == "3":
            print(
                "You have chosen to be the [bold cyan]Farmer[/bold cyan], \
is this correct?[Y/N]")
            input("\n-->")
            if input == "y":
                break
        else:
            print("Invalid selection, please choose a person")
        continue


while True:
    print(
        "\n \n [u]Welcome to [bold red]Oregon Trail[/bold red]: \
Python Edition![/u]\n")
    print("1.) Start")
    print("2.) Exit")
    option = input("\n-->")
    if option == "start":
        menu()
        break
    elif option == "exit":
        continue
    elif option == "1":
        menu()
        break
    elif option == "2":
        continue
    else:
        print("Goodbye")
