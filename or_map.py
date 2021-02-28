from queue import SimpleQueue

from pynput import keyboard
from rich import print
from rich.console import Console

console = Console()


class Map:
    def __init__(self):
        self.position = 0
        self.spacer = " " * 47
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
            [" " * 85, "☐\n", " " * 76, "FORT KEARNEY"],
            [" " * 101, "[bold red]START[/bold red]"],
            [" " * 103, "★"],
            [" " * 98, "INDEPENDENCE"],
        ]

    def print(self, selected):
        flat_map = []
        for y in self.map:
            for x in y:
                flat_map.append(x)
            flat_map.append("\n")

        if selected == 0:
            flat_map[73] = "[bold green][INDEPENDENCE][/bold green]"
        elif selected == 1:
            flat_map[64] = "[bold green][FORT KEARNEY][/bold green]"
        elif selected == 2:
            flat_map[54] = "[bold green][CHIMNEY ROCK][/bold green]"
        elif selected == 3:
            flat_map[57] = "[bold green][FORT LARAMIE][/bold green]"
        elif selected == 4:
            flat_map[37] = "[bold green][INDEPENDENCE ROCK][/bold green]"
        elif selected == 5:
            flat_map[50] = "[bold green][SOUTH PASS][/bold green]"
        elif selected == 6:
            flat_map[40] = "[bold green][SODA SPRINGS][/bold green]"
        elif selected == 7:
            flat_map[32] = "[bold green][FORT HALL][/bold green]"
        elif selected == 8:
            flat_map[23] = "[bold green][FORT BOISE][/bold green]"
        elif selected == 9:
            flat_map[21] = "[bold green][BLUE[/bold green]"
            flat_map[26] = "[bold green]MOUNTAINS][/bold green]"
        elif selected == 10:
            flat_map[15] = "[bold green][THE DALLES][/bold green]"
        elif selected == 11:
            flat_map[5] = "[bold green][FORT WALLA WALLA][/bold green]"
        elif selected == 12:
            flat_map[2] = "[bold green][OREGON[/bold green]"
            flat_map[4] = "[bold green]CITY][/bold green]"
            flat_map[9] = " ★"
        console.clear()
        print(" ".join(flat_map))
        print(
            """
    ╔═══════════════════════╗
    ║                       ║
    ║      ☐ FORTS          ║
    ║      ◼ LANDMARKS      ║
    ║      _ YOUR ROUTE     ║
    ║      ★ HOME           ║
    ║                       ║
    ╚═══════════════════════╝
        """
        )


map = Map()
queue = SimpleQueue()


def on_press(key):
    """Function handling menu navigation"""
    queue.put(key)


def print_map():
    listener = keyboard.Listener(on_press=on_press, suppress=True)
    listener.start()
    selected = 0
    while True:
        map.print(selected)
        key = queue.get()
        if key == keyboard.Key.right and selected > 0:
            selected -= 1
        elif key == keyboard.Key.left and selected < 12:
            selected += 1
        elif key == keyboard.Key.esc:
            listener.stop()
            break
