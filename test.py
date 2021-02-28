import random
import time
from functools import partial
from queue import SimpleQueue

from colorama import Back, Fore
from rich.console import Console
from rich.table import Table

from or_globalvars import player, vars, vars2

console = Console()


def fort():
    spacer = " " * 20
    oxen_price = 25.00
    clothing_price = 12.50
    ammunition_price = 2.50
    wheels_price = 12.50
    axles_price = 12.50
    tounges_price = 12.50
    food_price = 0.25

    console.clear()
    options = [
        f"{Back.WHITE + Fore.BLACK}  1. Oxen         {spacer}{oxen_price} per ox      ".ljust(
            50
        ),
        f"{Back.RESET + Fore.RESET}  2. Clothing     {spacer}{clothing_price} per set".ljust(
            50
        ),
        f"{Back.WHITE + Fore.BLACK}  3. Ammunition   {spacer}{ammunition_price} per box      ".ljust(
            50
        ),
        f"{Back.RESET + Fore.RESET}  4. Wagon wheels {spacer}{wheels_price} per wheel".ljust(
            50
        ),
        f"{Back.WHITE + Fore.BLACK}  5. Wagon axles  {spacer}{axles_price} per axle    ".ljust(
            50
        ),
        f"{Back.RESET + Fore.RESET}  6. Wagon tounges{spacer}{tounges_price} per tounge  ".ljust(
            50
        ),
        f"{Back.WHITE + Fore.BLACK}  7. Food         {spacer}{food_price} per pound   ".ljust(
            50
        ),
        f"{Back.RESET + Fore.RESET}  8. Leave store".ljust(50),
    ]
    print(f"{Fore.CYAN}You may buy:{Fore.RESET}\n")
    for i in options:
        print(i)

    selected = input("\nWhich number? ")

    if selected == "1":
        amount_ox = input(f"\n{Fore.CYAN}How many ox? {Fore.RESET}")

        if oxen_price * int(amount_ox) > vars.cash_total:
            print(f"{Fore.RED}You can't spend that much on oxen{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        if vars.cash_total <= 0:
            print(f"{Fore.RED} You can't spend any more.{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        elif vars.cash_total > 0:
            vars.cash_total = int(vars.cash_total - (int(amount_ox)))
            vars.amount_spent_on_animals = int(
                (vars.amount_spent_on_animals + int(amount_ox))
            )
            fort()
        else:
            print("\n[red]Please enter a number[/red]\n")
        console.clear()

    if selected == "2":
        amount_sets = input(f"\n{Fore.CYAN}How many sets? {Fore.RESET}")

        if clothing_price * int(amount_sets) > vars.cash_total:
            print(
                f"{Fore.RED}You can't spend that much on clothing{Fore.RESET}"
            )
            input("Press Enter to Continue...")
            fort()
        if vars.cash_total <= 0:
            print(f"{Fore.RED} You can't spend any more.{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        elif vars.cash_total > 0:
            vars.cash_total = int(vars.cash_total - (int(amount_sets)))
            vars.amount_spent_on_clothing = int(
                (vars.amount_spent_on_clothing + int(amount_sets))
            )
            fort()
        else:
            print("\n[red]Please enter a number[/red]\n")
        console.clear()

    if selected == "3":
        amount_boxes = input(f"\n{Fore.CYAN}How many boxes? {Fore.RESET}")

        if ammunition_price * int(amount_boxes) > vars.cash_total:
            print(f"{Fore.RED}You can't spend that much on ammo{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        if vars.cash_total <= 0:
            print(f"{Fore.RED} You can't spend any more.{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        elif vars.cash_total > 0:
            vars.cash_total = int(vars.cash_total - (int(amount_boxes)))
            vars.amount_spent_on_bullets = int(
                (vars.amount_spent_on_bullets + int(amount_boxes))
            )
            fort()
        else:
            print("\n[red]Please enter a number[/red]\n")
        console.clear()
    if selected == "4":
        amount_wheels = input(f"\n{Fore.CYAN}How many wheels? {Fore.RESET}")

        if wheels_price * int(amount_wheels) > vars.cash_total:
            print(f"{Fore.RED}You can't spend that much on wheels{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        if vars.cash_total <= 0:
            print(f"{Fore.RED} You can't spend any more.{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        elif vars.cash_total > 0:
            vars.cash_total = int(vars.cash_total - (int(amount_wheels)))
            vars.amount_spent_on_miscellaneous = int(
                (vars.amount_spent_on_miscellaneous + int(amount_wheels))
            )
            fort()
        else:
            print("\n[red]Please enter a number[/red]\n")
        console.clear()

    if selected == "5":
        amount_axles = input(f"\n{Fore.CYAN}How many axles? {Fore.RESET}")

        if axles_price * int(amount_axles) > vars.cash_total:
            print(f"{Fore.RED}You can't spend that much on axles{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        if vars.cash_total <= 0:
            print(f"{Fore.RED} You can't spend any more.{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        elif vars.cash_total > 0:
            vars.cash_total = int(vars.cash_total - (int(amount_axles)))
            vars.amount_spent_on_miscellaneous = int(
                (vars.amount_spent_on_miscellaneous + int(amount_axles))
            )
            fort()
        else:
            print("\n[red]Please enter a number[/red]\n")
        console.clear()

    if selected == "6":
        amount_tounges = input(f"\n{Fore.CYAN}How many tounges? {Fore.RESET}")

        if tounges_price * int(amount_tounges) > vars.cash_total:
            print(
                f"{Fore.RED}You can't spend that much on tounges{Fore.RESET}"
            )
            input("Press Enter to Continue...")
            fort()
        if vars.cash_total <= 0:
            print(f"{Fore.RED} You can't spend any more.{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        elif vars.cash_total > 0:
            vars.cash_total = int(vars.cash_total - (int(amount_tounges)))
            vars.amount_spent_on_miscellaneous = int(
                (vars.amount_spent_on_miscellaneous + int(amount_tounges))
            )
            fort()
        else:
            print("\n[red]Please enter a number[/red]\n")
        console.clear()

    if selected == "7":
        amount_pounds = input(f"\n{Fore.CYAN}How many pounds? {Fore.RESET}")

        if food_price * int(amount_pounds) > vars.cash_total:
            print(f"{Fore.RED}You can't spend that much on food{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        if vars.cash_total <= 0:
            print(f"{Fore.RED} You can't spend any more.{Fore.RESET}")
            input("Press Enter to Continue...")
            fort()
        elif vars.cash_total > 0:
            vars.cash_total = int(vars.cash_total - (int(amount_pounds)))
            vars.amount_spent_on_food = int(
                (vars.amount_spent_on_food + int(amount_pounds))
            )
            fort()
        else:
            print("\n[red]Please enter a number[/red]\n")
        console.clear()


fort()
