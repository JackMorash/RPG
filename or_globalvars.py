import random
import time

from rich import print

from or_player import player


class GameGlobals:
    def __init__(self):
        self.dead = False
        self.GOAL_IN_MILES = 2040
        self.SOUTH_PASS_IN_MILES = 950
        self.amount_spent_on_animals = 0
        self.amount_spent_on_bullets = 0
        self.amount_spent_on_clothing = 0
        self.is_sufficient_clothing = False
        self.current_date = 0
        self.shooting_level = 5
        self.choice_of_eating = 1
        self.amount_spent_on_food = 0
        self.has_cleared_south_pass = False
        self.has_cleared_blue_montains = False
        self.fraction_of_2_weeks = 0
        self.is_injured = False
        self.is_blizzard = False
        self.total_mileage = 0
        self.amount_spent_on_miscellaneous = 0
        self.total_mileage_previous_turn = 0
        self.has_illness = False
        self.hostility_of_riders = False
        self.has_fort = False
        self.got_shot = False
        self.cold_weather = False
        self.raining = False
        self.weather = "Fine"
        self.health = "Healthy"

    def print_inventory(self):
        self.amount_spent_on_food = max(int(self.amount_spent_on_food), 0)
        self.amount_spent_on_bullets = max(
            int(self.amount_spent_on_bullets), 0)
        self.amount_spent_on_clothing = max(
            int(self.amount_spent_on_clothing), 0)
        self.amount_spent_on_miscellaneous = max(
            int(self.amount_spent_on_miscellaneous), 0)
        print("█"*79)
        print("[cyan]Food: [/cyan]", self.amount_spent_on_food)
        print("[cyan]Bullets: [/cyan]", self.amount_spent_on_bullets)
        print("[cyan]Clothing: [/cyan]", self.amount_spent_on_clothing)
        print("[cyan]Supplies: [/cyan]", self.amount_spent_on_miscellaneous)
        print("[green]Money : $[/green]", player.money)
        print("█"*79)
        input("-->")

    def cont():
        while True:
            option = input("Press Enter to Continue:")
            if option == "exit":
                return False
            else:
                break

    def increment_turn(self):
        self.current_date += 1

    def print_too_long(self):
        print("[red]You have been on the trail for too long...[/red]")
        print("[red]Your family dies in the \
    first blizzard of the winter[/red]")
        self.dead = True

    def no_turns_left(self, arr):
        return self.current_date >= len(arr)

    def input_yes_no(message):
        reply = input(message)
        return True if 'y' in reply else False

    def input_int(message):
        text_2_int = None
        while text_2_int == None:
            try:
                text_2_int = int(input(message))
            except:
                text_2_int = None
        return text_2_int

    def shooting():
        words = ["BANG", "BLAM", "POW", "WHAM"]
        word = random.choice(words)
        t0 = time.time()
        typed_word = input("{}".format(word))
        t1 = time.time()
        B1 = (t1-t0)-(vars.shooting_level)
        if typed_word != word:
            return 9
        return max(B1, 0)

    def illness(this_vars):
        RND = random.random()
        if 100*RND < 10+35*(this_vars.choice_of_eating-1):
            print("\n[red]MILD ILLNESS---MEDICINE USED[/red]\n")
            this_vars.total_mileage -= 5
            this_vars.amount_spent_on_miscellaneous -= 2
        elif 100*RND < 100-(40/4**(this_vars.choice_of_eating-1)):
            print("\n[red]BAD ILLNESS---MEDICINE USED[/red]\n")
            this_vars.total_mileage -= 5
            this_vars.amount_spent_on_miscellaneous -= 5
        else:
            print("\n[red]SERIOUS ILLNESS[/red]\n")
            print("\n[red]YOU MUST STOP FOR MEDICAL ATTENTION[/red]\n")
            this_vars.amount_spent_on_miscellaneous -= 10
            this_vars.has_illness = True

    def hp():
        if vars.is_injured == True:
            health = "Injured"
        elif vars.is_injured == False:
            health = "Healthy"


vars = GameGlobals()
