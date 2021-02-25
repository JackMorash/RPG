import time

from rich import print
from rich.console import Console

console = Console()


class Player:
    def __init__(self):
        """Function for creating player-based variables"""
        self.name = ""
        self.job = ""
        self.money = 1600
        self.bullets = 999
        self.water = 0
        self.oxen = 999
        self.parts = 999
        self.medicine = 0
        self.clothes = 999
        self.food = 999
        self.cholera = False
        self.typhoid = False
        self.measles = False
        self.cold = False
        self.alive = True
        self.repair = False
        self.miles = 500


player = Player()
