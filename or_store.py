from rich import print
from rich.console import Console
from rich.table import Table
from or_player import player
from or_main import journey

oxen_total = 0
food_total = 0
clothes_total = 0
bullets_total = 0
parts_total = 0


def oxen():
    while True:
        print("\n[cyan italic]There are 2 oxen in a yoke;\n\
I recommend at least 3 yoke.\nI charge [green]$40[/green] a yoke.\n\
[/cyan italic]")
        amount = input("How many yoke do you want?: ")
        oxen_total = float(amount)
        if (oxen_total * 40.00) > player.money:
            print("[red]You can't spend that much on oxen[/red]")
            continue
        if player.money <= 0:
            print("\n[red] You can't spend any more.[/red]")
            continue
        elif player.money > 0:
            player.money = player.money - (oxen_total * 40.00)
            player.oxen = player.oxen + oxen_total
            print(player.oxen)
            print(player.money)
            store()
            break
        elif ValueError:
            print("\n[red]Please enter a number[/red]\n")
            continue


def food():
    while True:
        print("\n[cyan italic]I recommend you take at least 200 pounds of food\
 for each person in your group. I see that you have 5 people in total.\
 You'll need flour, sugar, bacon, and coffee.\
 My total is [green]¢20 a pound[/green][/cyan italic]\n")
        amount = input("\nHow many pounds of food do you want?: ")
        food_total = float(amount)
        if (food_total * 0.20) > player.money:
            print("[red]You can't spend that much on food[/red]")
            continue
        if player.money <= 0:
            print("\n[red] You can't spend any more.[/red]")
            continue
        elif player.money > 0:
            player.money = player.money - (food_total * 0.20)
            player.food = player.food + food_total
            store()
            break
        elif ValueError:
            print("\n[red]Please enter a number[/red]\n")
        store()


def clothes():
    while True:
        print("\n[cyan italic]You'll need warm clothing in the mountains.\
 I recommend taking at least 2 sets of clothes per person.\
 Each set is [green]$10.00.[/green][/cyan italic]\n")
        amount = input("\nHow many sets of\
 clothes do you want?: ")
        clothes_total = float(amount)
        if (clothes_total * 40.00) > player.money:
            print("[red]You can't spend that much on clothes[/red]")
            continue
        if player.money <= 0:
            print("\n[red] You can't spend any more.[/red]")
            break
        elif player.money > 0:
            player.money = player.money - (clothes_total * 40.00)
            player.clothes = player.clothes + clothes_total
            store()
            break
        elif ValueError:
            print("\n[red]Please enter a number[/red]\n")
            continue
        store()


def bullets():
    while True:
        print("\n[cyan italic]I sell ammunition in boxes of 20 bullets. Each\
box costs [green]$2.00.[/green][/cyan italic]\n")
        amount = input("\nHow many boxes do you want?: ")
        bullets_total = float(amount)
        if (bullets_total * 2.00) > player.money:
            print("[red]You can't buy that many bullets, it's not like\
you are an American or something...oh wait[/red]")
            continue
        if player.money <= 0:
            print("\n[red] You can't spend any more.[/red]\n")
            break
        elif player.money > 0:
            player.money = player.money - (bullets_total * 2.00)
            player.bullets = player.bullets + bullets_total
            store()
            break
        elif ValueError:
            print("\n[red]Please enter a number[/red]\n")
            continue
        store()


def parts():
    while True:
        print("\n[cyan italic]It's a good idea to have a few spare parts for\
 your wagon. Here are the totals:\
\nWagon wheel - [green]$10 each[/green]\
\nWagon axle - [green]$10 each[/green]\
\nWagon tongue - [green]$10 each[/green]\n")
        amount1 = input("How many wagon wheels do you want?: ")
        amount2 = input("How many wagon axles do you want?: ")
        amount3 = input("How many wagon tongues do you want?: ")
        wheels = float(amount1)
        axles = float(amount2)
        tongues = float(amount3)
        parts_total = (wheels + axles + tongues)
        if (parts_total) > player.money:
            print("[red]You can't spend that much on spare parts[/red]")
            continue
        if player.money <= 0:
            print("\n[red] You can't spend any more.[/red]")
            break
        elif player.money > 0:
            player.money = player.money - (parts_total * 10.00)
            player.parts = player.parts + parts_total
            store()
            break
        elif ValueError:
            print("[red]Please enter a number[/red]")
            continue
        store()


def matt_message():
    """Prints store message, creates store interface"""
    print(f"\nBefore leaving [red]Independence[/red] you should buy equipment \
and supplies. You have [green]$1600.00[/green] in cash, but you \
dont have to spend it \
all now.\n\n You can buy whatever you need at \
[red]Matt's General Store[/red]")
    print("\n[cyan italic] Hello, I'm Matt. So you're going to Oregon! I can\
 fix you up with what you need:\n\n\n - [blue]A team of oxen to pull your \
wagon\
\n - Clothing for both winter and summer[/blue]\n\n")
    key = input("Press Enter to continue")
    store()


def store():
    p = player.parts * 10.00
    b = player.bullets * 2.00
    c = player.clothes * 40.00
    f = player.food * 0.20
    o = player.oxen * 40.00
    console = Console()
# Store interface
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Goods")
    table.add_column("Cost", justify="right")
    table.add_row(
        "1. Oxen",
        f"[green]${player.oxen * 40.00}[/green]"
    )
    table.add_row(
        "2. Food",
        f"[green]${player.food * 0.20}[/green]",
    )
    table.add_row(
        "3. Clothing",
        f"[green]${player.clothes * 40.00}[/green]"
    )
    table.add_row(
        "4. Ammunition",
        f"[green]${player.bullets * 2.00}[/green]"
    )
    table.add_row(
        "5. Spare Parts",
        f"[green]${player.parts * 10.00}[/green]"
    )
    table.add_row(
        "\nTotal",
        f"\n[green]${o+f+c+b+p}[/green]"
    )
    console.print(table)

    while True:
        print("Which item would you like to buy?\n\n[cyan italic]\
Press spacebar to exit the store[/cyan italic]")
        selection = input("\n-->")
        if selection == "1":
            oxen()
            break
        elif selection == "2":
            food()
            break
        elif selection == "3":
            clothes()
            break
        elif selection == "4":
            bullets()
            break
        elif selection == "5":
            parts()
            break
        elif selection == "exit":
            return None
        elif selection == "leave":
            if player.oxen < 1:
                print("[cyan italic] Don't forget,\
 you'll need oxen to pull your wagon![/cyan italic]")
            elif player.oxen > 1:
                print("[cyan italic]Well then, you are ready to start.\
 Good luck! You have a long and difficult journey ahead of you...[/cyan italic]")
            journey()
            break
        else:
            print("\n[red]Invalid Selection[/red]\n")
            continue
