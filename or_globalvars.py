from rich import print


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
        self.cash_total = -1
        self.has_fort = False

    def print_inventory(self):
        self.amount_spent_on_food = max(int(self.amount_spent_on_food), 0)
        self.amount_spent_on_bullets = max(
            int(self.amount_spent_on_bullets), 0)
        self.amount_spent_on_clothing = max(
            int(self.amount_spent_on_clothing), 0)
        self.amount_spent_on_miscellaneous = max(
            int(self.amount_spent_on_miscellaneous), 0)
        print("="*53)
        print("[cyan]Food: [/cyan]", self.amount_spent_on_food)
        print("[cyan]Bullets: [/cyan]", self.amount_spent_on_bullets)
        print("[cyan]Clothing: [/cyan]", self.amount_spent_on_clothing)
        print("[cyan]Supplies: [/cyan]", self.amount_spent_on_miscellaneous)
        print("[green]Money : $[/green]", self.cash_total)
        print("="*53)

    def increment_turn(self):
        self.current_date += 1

    def print_too_long(self):
        print("[red]You have been on the trail for too long...[/red]")
        print("[red]Your family dies in the \
first blizzard of the winter[/red]")
        self.dead = True

    def no_turns_left(self, arr):
        return self.current_date >= len(arr)


vars = GameGlobals()
