from rich import print
from rich.console import Console

from or_store import matt_message

console = Console()
# Possible starting dates
dates = ["MARCH 29",
         "APRIL 12 ",
         "APRIL 26 ",
         "MAY 10 ",
         "MAY 24 ",
         "JUNE 7 ",
         "JUNE 21 ",
         "JULY 5 ",
         "JULY 19 ",
         "AUGUST 2 ",
         "AUGUST 16 ",
         "AUGUST 31 ",
         "SEPTEMBER 13 ",
         "SEPTEMBER 27 ",
         "OCTOBER 11 ",
         "OCTOBER 25 ",
         "NOVEMBER 8 ",
         "NOVEMBER 22 ",
         "DECEMBER 6 ",
         "DECEMBER 20 "]


def choose_date():
    """Displays storyline message, selects date for departure"""
    print("\nIt is 1848, your jumping off place for Oregon is \
[red]Independence, Missouri[/red]. You must decide which month to \
leave [red]Independence[/red]")
    print("\n [green]1. March[green/]\n [green]2. April[/green]\n [green]\
3. May[/green]\n [green]4. June[/green]\n [green]5. July[/green]")
# Options for month of departure
    while True:
        month = input("\n-->")
        if month == "1":
            console.clear()
            matt_message()
            break
        elif month == "2":
            del dates[1]
            console.clear()
            matt_message()
            break
        elif month == "3":
            del dates[1:3]
            console.clear()
            matt_message()
            break
        elif month == "4":
            del dates[1:5]
            console.clear()
            matt_message()
            break
        elif month == "5":
            del dates[1:7]
            console.clear()
            matt_message()
            break
        elif month == "exit":
            console.clear()
            return None
        elif ValueError:
            print("\n[red]Invalid Selection, please enter a number[/red]")
        else:
            print("\n[red]Invalid Selection, please enter a number[/red]")
        continue
    console.clear()


# Weekday names
weekdays = ["SATURDAY", "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY",
            "THURSDAY", "FRIDAY"]


def print_date(turn_number):
    """Determines which turn it is, creates a date based off turn #

    Args:
        turn_number (Month, Day): Sets possible dates
    """
    print("=" * 53)
    print("{} {} 1847".format(weekdays[0], dates[turn_number]))
    print("=" * 53)


def print_weekday(amount):
    return weekdays[amount % 7]


def print_final_date(D3):
    """Determines final date based off origin

    Args:
        D3 ([type]): [description]

    Returns:
        [type]: [description]
    """
    # mar 29 -> dec 20 1847 = 266 days
    weekday = print_weekday(D3)
    # dec 1 = 246 days
    if D3 > 246:
        return "{} DECEMBER {} 1847".format(weekday, D3 - 246)
    elif D3 > 216:
        return "{} NOVEMBER {} 1847".format(weekday, D3 - 216)
    elif D3 > 185:
        return "{} OCTOBER {} 1847".format(weekday, D3 - 185)
    elif D3 > 155:
        return "{} SEPTEMBER {} 1847".format(weekday, D3 - 155)
    elif D3 > 125:
        return "{} AUGUST {} 1847".format(weekday, D3 - 124)
    else:
        return "{} JULY {} 1847".format(weekday, D3 - 93)
