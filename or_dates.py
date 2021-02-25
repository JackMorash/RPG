from rich import print
from rich.console import Console

from or_globalvars import vars

console = Console()
# Possible starting dates

# Weekday names array
weekdays = ["SATURDAY", "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY",
            "THURSDAY", "FRIDAY"]


def get_date():
    """Determines which turn it is, creates a date based off turn #

    Args:
        turn_number (Month, Day): Sets possible dates
    """
    return f"{vars.dates[0]}, {vars.current_date}"


def print_weekday(amount):
    """Function for determining day of the week"""
    return weekdays[amount % 7]


def print_final_date(D3):
    """Determines final date based off origin"""
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
