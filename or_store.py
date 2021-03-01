import time
from re import T

from rich import print
from rich.console import Console
from rich.progress import track
from rich.table import Table

from or_globalvars import player, vars
from or_trail import walking_trail

console = Console()


def oxen():
    """Function for handling the purchase of oxen"""
    while True:
        try:
            print(
                "\n[cyan italic]There are 2 oxen in a yoke;\n\
I recommend at least 3 yoke.\nI charge [green]$40[/green] a yoke.\n\
[/cyan italic]"
            )
            amount = input("How many yoke do you want?: ")
            oxen_total = int(amount)

            if (oxen_total * 40.00) > vars.cash_total:
                print("[red]You can't spend that much on oxen[/red]")
                time.sleep(1.5)
                continue
            if vars.cash_total <= 0:
                print("\n[red] You can't spend any more.[/red]")
                time.sleep(1.5)
                console.clear()
                store()
                continue
            elif vars.cash_total > 0:
                vars.cash_total = int(vars.cash_total - (oxen_total * 40.00))
                vars.amount_spent_on_animals = int(
                    vars.amount_spent_on_animals + oxen_total * 40.00
                )
                store()
        except ValueError:
            print("\n[red]Please enter a number[/red]\n")
            input("\nPress Enter to Continue")
            console.clear()
            store()


def food():
    """Function for handling the purchase of food"""
    while True:
        try:
            print(
                "\n[cyan italic]I recommend you take at least 200 pounds of food\
 for each person in your group. I see that you have 5 people in total.\
 You'll need flour, sugar, bacon, and coffee.\
 My total is [green]¢20[/green] a pound[/cyan italic]\n"
            )
            amount = input("\nHow many pounds of food do you want?: ")
            food_total = int(amount)
            if (food_total * 0.20) > vars.cash_total:
                print("[red]You can't spend that much on food[/red]")
                time.sleep(1.5)
                continue
            if vars.cash_total <= 0:
                print("\n[red] You can't spend any more.[/red]")
                time.sleep(1.5)
                console.clear()
                store()
                continue
            elif vars.cash_total > 0:
                vars.cash_total = int(vars.cash_total - (food_total * 0.20))
                vars.amount_spent_on_food = int(
                    vars.amount_spent_on_food + food_total * 0.20
                )
                console.clear()
                store()
                break
        except ValueError:
            print("\n[red]Please enter a number[/red]\n")
            input("\nPress Enter to Continue")
            console.clear()
            store()


def clothes():
    """Function for handling the purchase of clothes"""
    while True:
        try:
            print(
                "\n[cyan italic]You'll need warm clothing in the mountains.\
 I recommend taking at least 2 sets of clothes per person.\
 Each set is [green]$10.00.[/green][/cyan italic]\n"
            )
            amount = input(
                "\nHow many sets of\
 clothes do you want?: "
            )
            clothes_total = int(amount)
            if (clothes_total * 40.00) > vars.cash_total:
                print("[red]You can't spend that much on clothes[/red]")
                time.sleep(1.5)
                continue
            if vars.cash_total <= 0:
                print("\n[red] You can't spend any more.[/red]")
                time.sleep(1.5)
                console.clear()
                store()
                break
            elif vars.cash_total > 0:
                vars.cash_total = int(
                    vars.cash_total - (clothes_total * 10.00)
                )
                vars.amount_spent_on_clothing = int(
                    vars.amount_spent_on_clothing + clothes_total * 10.00
                )
                console.clear()
                store()
                break
        except ValueError:
            print("\n[red]Please enter a number[/red]\n")
            input("\nPress Enter to Continue")
            console.clear()
            store()


def bullets():
    """Function for handling the purchase of bullets"""
    while True:
        try:
            print(
                "\n[cyan italic]I sell ammunition in boxes of 20 bullets. Each\
box costs [green]$2.00.[/green][/cyan italic]\n"
            )
            amount = input("\nHow many boxes do you want?: ")
            bullets_total = int(amount)
            # Determines if the player can spend enough bullets
            if (bullets_total * 2.00) > vars.cash_total:
                print(
                    "[red]You can't buy that many bullets, it's not like \
you are an American or something...oh wait[/red]"
                )
                time.sleep(1.5)
                continue
            # Determines if the player can afford bullets
            if vars.cash_total <= 0:
                print("\n[red] You can't spend any more.[/red]\n")
                time.sleep(1.5)
                console.clear()
                store()
                break
            # Adds bullets to total player bullets
            elif vars.cash_total > 0:
                vars.cash_total = int(vars.cash_total - (bullets_total * 2.00))
                vars.amount_spent_on_bullets = int(
                    vars.amount_spent_on_bullets + bullets_total * 2.00
                )
                console.clear()
                store()
                break
        except ValueError:
            print("\n[red]Please enter a number[/red]\n")
            input("\nPress Enter to Continue")
            console.clear()
            store()


def parts():
    """Function for handling the purchase of misc. parts"""
    while True:
        try:
            print(
                "\n[cyan italic]It's a good idea to have miscellaneous \
supplies such as medicine for when party members become ill, and wagon parts \
for when your wagon breaks down[/cyan italic]"
            )
            amount = input("How mmany supplies do you want? ")
            misc = int(amount)
            parts_total = misc
            if (parts_total) > vars.cash_total:
                print("[red]You can't spend that much on misc supplies[/red]")
                time.sleep(1.5)
                continue
            if vars.cash_total <= 0:
                print("\n[red] You can't spend any more.[/red]")
                time.sleep(1.5)
                console.clear()
                store()
                break
            elif vars.cash_total > 0:
                vars.cash_total = int(vars.cash_total - (parts_total * 10.00))
                vars.amount_spent_on_miscellaneous = int(
                    vars.amount_spent_on_miscellaneous + parts_total * 10.00
                )
                console.clear()
                store()
                break
        except ValueError:
            print("[red]Please enter a number[/red]")
            input("\nPress Enter to Continue")
            console.clear()
            store()


def matt_message():
    """Prints store message, creates store interface"""
    for step in track(range(13), description="Beginning Your Journey..."):
        time.sleep(0.2)
    time.sleep(1.5)
    console.clear()
    print(
        "\nBefore leaving [red]Independence[/red] you should buy equipment \
and supplies. You have [green]$1600.00[/green] in cash, but you \
dont have to spend it \
all now.\n\nYou can buy whatever you need at \
[red]Matt's General Store[/red]"
    )
    input("Press Enter to continue...")
    console.clear()
    print(
        "\n[cyan italic] Hello, I'm Matt. So you're going to Oregon! I can\
 fix you up with what you need:\n\n\n [blue]- A team of oxen to pull your \
wagon\
\n - Clothing for both winter and summer[/blue]\n\n"
    )
    input("Press Enter to continue...")
    console.clear()
    store()


def store():
    """Function for creating the store UI"""
    # Determines price of each type of item
    p = vars.amount_spent_on_miscellaneous
    b = vars.amount_spent_on_bullets
    c = vars.amount_spent_on_clothing
    f = vars.amount_spent_on_food
    o = vars.amount_spent_on_animals
    # Creates store UI using table library
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Goods")
    table.add_column("Spent", justify="right")
    # Creates "oxen" portion of the table
    table.add_row("1. Oxen", f"[green]${o}[/green]")
    # Creates "food" portion of the table
    table.add_row(
        "2. Food",
        f"[green]${f}[/green]",
    )
    # Creates "clothing" portion of the table
    table.add_row(
        "3. Clothing",
        f"[green]${c}[/green]",
    )
    # Creates "ammunition" portion of the table
    table.add_row(
        "4. Ammunition",
        f"[green]${b}[/green]",
    )
    # Creates "parts" portion of the table
    table.add_row(
        "5. Misc. (Medicine, Wagon parts etc.)",
        f"[green]${p}[/green]",
    )
    # Creates the total spent portion of the table
    table.add_row("\nTotal", f"\n[green]${o+f+c+b+p}[/green]")
    console.print(table)

    while True:
        # Displays and handles store options and which option the player selects
        try:
            print(
                "Which item would you like to buy?\n\n[cyan italic]\
Type 'leave' to exit the store[/cyan italic]"
            )
            selection = input("\n-->")
            if selection == "1":
                console.clear()
                oxen()
            elif selection == "2":
                console.clear()
                food()
                break
            elif selection == "3":
                console.clear()
                clothes()
                break
            elif selection == "4":
                console.clear()
                bullets()
                break
            elif selection == "5":
                console.clear()
                parts()
                break
            elif selection == "exit":
                console.clear()
                exit()
            elif selection == "leave":
                # Determines if the player has enough oxen to play the game
                if vars.amount_spent_on_animals < 1:
                    print(
                        "[cyan italic] Don't forget,\
 you'll need oxen to pull your wagon![/cyan italic]"
                    )
                    input("Press Enter to Continue...")
                    console.clear()
                    store()
                elif vars.amount_spent_on_animals > 1:
                    console.clear()
                    print(
                        "[cyan italic]Well then, you are ready to start.\
 Good luck! You have a long and difficult\
 journey ahead of you...[/cyan italic]"
                    )
                input("Press Enter to Continue...")
                console.clear()
                walking_trail()
                break
        except ValueError:
            print("\n[red]Invalid Selection[/red]\n")
            input("\nPress Enter to Continue")
            continue
