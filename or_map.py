from queue import SimpleQueue

from pynput import keyboard
from rich import print
from rich.console import Console

console = Console()


class Map:
    """Class for displaying the Map"""

    def __init__(self):
        """Initial variables"""
        # Determines which message displays
        map_message = ""
        # Determines which location the player selects
        self.position = 0
        # Empty space when displaying certain prints
        self.spacer = " " * 47
        # Array for map locations, (looks terrible in the IDE)
        self.map = [
            [
                f"\n{self.spacer}╔═════════════════════════╗\n{self.spacer}║\
[bold italic cyan] Map of the\
 Oregon Trail [/bold italic cyan]║\n{self.spacer}╚═════════════════════════╝"
            ],
            ["[blue bold]OREGON[/blue bold]"],
            ["[blue bold]CITY[/blue bold]", "  FORT WALLA WALLA"],
            [" ★", " " * 10, "☐", "\n", " " * 10, "◼"],
            [" " * 6, "THE DALLES", "\n", " " * 14, "◼"],
            [" " * 14, "BLUE", " " * 2, "FORT BOISE"],
            [" " * 12, "MOUNTAINS", " ", "☐"],
            ["\n\n", " " * 30, "FORT HALL"],
            [" " * 34, "☐", " " * 17, "INDEPENDENCE ROCK"],
            [" " * 40, "SODA SPRINGS", " " * 3, "◼"],
            [" " * 40, "◼", " " * 7, "◼"],
            [" " * 50, "SOUTH PASS", " " * 4, "☐", " " * 4, "CHIMNEY ROCK"],
            [" " * 63, "FORT LARAMIE", " " * 4, "◼"],
            [
                " " * 43,
                "☐",
                " " * 37,
                "☐\n",
                " " * 42,
                "FORT BRIDGER",
                " " * 19,
                "FORT KEARNEY",
            ],
            [" " * 101, "[bold red]START[/bold red]"],
            [" " * 103, "★"],
            [" " * 98, "INDEPENDENCE"],
        ]

    def print(self, selected):
        """Function determines which location is selected, prints array"""
        flat_map = []
        for y in self.map:
            for x in y:
                flat_map.append(x)
            flat_map.append("\n")

        # Determines message for which location player selects
        if selected == 0:
            flat_map[77] = "[bold green][INDEPENDENCE][/bold green]"
            self.map_message = "[i cyan]Independence was founded by pioneers who\n\
migrated from Independence, Missouri.\nIt is where your party starts[/i cyan]"
        elif selected == 1:
            flat_map[68] = "[bold green][FORT KEARNEY][/bold green]"
            self.map_message = "[i cyan]Fort Kearney is the first fort on the way\n\
to Oregon City. It's been stocked with\neverything a traveller would need to\n\
make the periless journey to Oregon City[/i cyan]"
        elif selected == 2:
            flat_map[54] = "[bold green][CHIMNEY ROCK][/bold green]"
            self.map_message = "[i cyan]Located some one-hundred miles west \
of\nFort Laramie, Chimney Rock was one of the\nmost picturesque landmarks\
along the Oregon\nTrail. It signaled the end of the prairies \nas the\
trail became more steep and rugged\nheading west towards the Rocky\n\
Mountains.[/i cyan]"
        elif selected == 3:
            flat_map[57] = "[bold green][FORT LARAMIE][/bold green]"
            self.map_message = "[i cyan]The second major for along the trail,\
it \nwas intended to be used during the war of \n1812, \
but the war never made it to its walls[/i cyan]"
        elif selected == 4:
            flat_map[37] = "[bold green][INDEPENDENCE ROCK][/bold green]"
            self.map_message = "[i cyan]Independence Rock is a large granite\n\
rock, approximately 130 feet (40 m) high,\n1,900 feet (580 m) long.\n\
Many that have walked the trail\nhave carved their names into the rock[/i cyan]"
        elif selected == 5:
            flat_map[50] = "[bold green][SOUTH PASS][/bold green]"
            self.map_message = "[i cyan]South pass divides into two seperate \
paths, \nGreen River Crossing to the west,\n\
and Fort Bridger to the south[/i cyan]"
        elif selected == 6:
            flat_map[66] = "[bold green][FORT BRIDGER][/bold green]"
            self.map_message = "[i cyan]Fort Bridger is a small fort to the \n\
south of south pass. Isolated from\nthe rest of the Oregon Trail, \
\nit doesn't see many new supplies shipped in...[/i cyan]"
        elif selected == 7:
            flat_map[40] = "[bold green][SODA SPRINGS][/bold green]"
            self.map_message = "[i cyan]Soda Springs is a small spring with a\
beautiful\nview of the Blue Mountains. Indians and travelers\nalike travel\
to the springs for fresh water[/i cyan]"
        elif selected == 8:
            flat_map[32] = "[bold green][FORT HALL][/bold green]"
            self.map_message = "[i cyan]Fort Hall is a large fort containing\
\nan excess supply of US military armaments[/i cyan]"
        elif selected == 9:
            flat_map[23] = "[bold green][FORT BOISE][/bold green]"
            self.map_message = "[i cyan]Fort Boise is a smaller fort west \
of Fort Hall,\ngenerally used for excess stock from Fort Boise[/i cyan]"
        elif selected == 10:
            flat_map[21] = "[bold green][BLUE[/bold green]"
            flat_map[26] = "[bold green]MOUNTAINS][/bold green]"
            self.map_message = "[i cyan]A beautiful Mountain range, names for\
\nthe distinct blue hue that is produced around \nthe mountains[/i cyan]"
        elif selected == 11:
            flat_map[15] = "[bold green][THE DALLES][/bold green]"
            self.map_message = "[i cyan]A small river pass to \
Fort Walla Walla, used\nbefore the trail existed, it is now occupied by\n\
a toll collector[/i cyan]"
        elif selected == 12:
            flat_map[5] = "[bold green][FORT WALLA WALLA][/bold green]"
            self.map_message = "[i cyan]The last fort \
before Oregon City[/i cyan]"
        elif selected == 13:
            flat_map[2] = "[bold green][OREGON[/bold green]"
            flat_map[4] = "[bold green]CITY][/bold green]"
            flat_map[9] = " ★"
            self.map_message = "[i cyan]Your final destination[/i cyan]"
        console.clear()
        print(" ".join(flat_map))
        # Prints map key, displays selected location's description
        print(
            f"""
    ╔═══════════════════════╗
    ║                       ║
    ║      ☐ FORTS          ║
    ║      ◼ LANDMARKS      ║
    ║      ★ HOME           ║
    ║                       ║
    ╚═══════════════════════╝    
{self.map_message}"""
        )


map = Map()
queue = SimpleQueue()


def on_press(key):
    """Function handling menu navigation"""
    queue.put(key)


def print_map():
    """Loops the keyboard listener to determine which key the player pushes"""
    # Starts listening to keyboard inputs
    listener = keyboard.Listener(on_press=on_press, suppress=True)
    listener.start()
    # Variable for which option is selected
    global selected
    selected = 0
    # Loop for checking which key is pressed, updates menu when player presses
    # key
    while True:
        map.print(selected)
        key = queue.get()
        if key == keyboard.Key.right and selected > 0:
            selected -= 1
        elif key == keyboard.Key.left and selected < 13:
            selected += 1
        elif key == keyboard.Key.esc:
            listener.stop()
            break
