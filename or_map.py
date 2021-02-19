from rich import print
from rich.console import Console

console = Console()


def map():
    """Array for locations in the game"""
    console.clear()
    store = [["[blue bold]OREGON \n CITY[/blue bold]", "   FORT WALLA WALLA"],
             ["  ★", " "*10, "☐", "\n", " "*10, "◼"],
             [" "*6, "THE DALLES", "\n", " "*14, "◼"],
             [" "*14, "BLUE", " "*2, "FORT BOISE"],
             [" "*12, "MOUNTAINS", " ", "☐"],
             ["\n\n", " "*30, "FORT HALL"],
             [" "*34, "☐",  " "*17, "INDEPENDENCE ROCK"],
             [" "*40, "SODA SPRINGS", " "*3, "◼"],
             [" "*40, "◼", " "*7, "◼"],
             [" "*50, "SOUTH PASS", " "*4, "☐", " "*4, "CHIMNEY ROCK"],
             [" "*63, "LARAMIE", " "*4, "◼"],
             [" "*85, "☐\n", " "*76, "FORT KEARNEY"],
             [" "*101, "[bold red]START[/bold red]"],
             [" "*103, "★"],
             [" "*98, "INDEPENDENCE"],
             ]

# prints the map
    spacer = " "*40
    print(f"\n{spacer}[u italic cyan]Map of the Oregon Trail[/u italic cyan]")
    for i in store:
        for j in i:
            print(j, end=" ")
        print()
    print("""

* * * * * * * * * * * * *
*                       *
*      ☐ FORTS          *
*      ◼ LANDMARKS      *
*      _ YOUR ROUTE     *
*      ★ HOME           *
*                       *
* * * * * * * * * * * * *

    """)
