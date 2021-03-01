import random
import time

from rich import print
from rich.console import Console

console = Console()


class Character:
    def __init__(self):
        self.money = 1600.00


class Player(Character):
    def __init__(self):
        """Function for creating player-based variables"""
        super().__init__()
        self.name = ""
        self.job = ""
        self.members = []
        self.cold = False
        self.alive = True
        self.repair = False
        self.miles = 0


player = Player()


class GameGlobals:
    """Sets global game variables"""

    def __init__(self):
        # Flag for player death
        self.dead = False
        # Flag for amount of miles to reach Oregon City
        self.GOAL_IN_MILES = 2040
        # Flag for if player reached miles to south pass
        self.SOUTH_PASS_IN_MILES = 950
        # Flag for amount of animals player has
        self.amount_spent_on_animals = 0
        # Flag for amount of bullets player has
        self.amount_spent_on_bullets = 0
        # Flag for amount of clothes player has
        self.amount_spent_on_clothing = 0
        # Flag for amount of cash player has
        self.cash_total = player.money
        # Flag for amount of misc. items player has
        self.amount_spent_on_miscellaneous = 0
        # Flag for amount of food player has
        self.amount_spent_on_food = 0
        # Flag for how many miles player has traveled
        self.total_mileage = player.miles
        # Flag for if player has enough clothing to survive
        self.is_sufficient_clothing = False
        # Flag for determining current date
        self.current_date = 1
        # Flag for choice of food rationing
        self.choice_of_eating = 1
        # Flag for if player clears south pass
        self.has_cleared_south_pass = False
        # Flag for if player clears blue montains
        self.has_cleared_blue_montains = False
        # Flag for if player has been injured
        self.is_injured = False
        # Flag for if the player has been shot
        self.got_shot = False
        # Flag for if player is in a blizzard
        self.is_blizzard = False
        # Flag for determining how many miles the player took in the last turn
        self.total_mileage_previous_turn = 0
        # Flag for the distance to the next landmark call
        self.distance_to_landmark = 0
        # Flag for if player has an illness
        self.has_illness = False
        # Flag for cold weather
        self.cold_weather = False
        # Flag for raining
        self.raining = False
        # Flag for determining the string for the type of weather selected
        self.weather = "Fine"
        # Flag for determining the string for the player health
        self.health = "Healthy"
        # Flag for determining the string for the food quality type
        self.food_quality = "Filling"
        # Flag for determining the string for player landmark
        self.location = "Independence, Missouri"
        # Flag for determining if player has chosen chimney rock to travel to
        self.chimney_rock = False
        # Flag for determining if player has chosen green river to travel to
        self.green_river_crossing = False
        # Flag for determining if player has chosen fort bridger to travel to
        self.fort_bridger = False
        # Flag for determining if player has chosen fort walla walla to travel
        # to
        self.fort_walla_walla = False
        # Flag for determining if player has chosen the dalles to travel to
        self.the_dalles = False
        # Flag for determining if the player has passed kansas river
        self.kansas_river_passed = False
        # Flag for determining if the player has passed big blue river
        self.big_blue_river_passed = False
        # Flag for determining if the player has passed fort kearney
        self.fort_kearney_passed = False
        # Flag for determining if the player has passed fort laramie
        self.fort_laramie_passed = False
        # Flag for determining if the player has passed chimney rock
        self.chimney_rock_passed = False
        # Flag for determining if the player has passed independence rock
        self.independence_rock_passed = False
        # Flag for determining if the player has passed south pass
        self.south_pass_passed = False
        # Flag for determining if the player has passed snake river
        self.snake_river_passed = False
        # Flag for determining if the player has passed fort bridger
        self.fort_bridger_passed = False
        # Flag for determining if the player has passed green river
        self.green_river_passed = False
        # Flag for determining if the player has passed soda springs
        self.soda_springs_passed = False
        # Flag for determining if the player has passed fort hall
        self.fort_hall_passed = False
        # Flag for determining if the player has passed fort boise
        self.fort_boise_passed = False
        # Flag for determining if the player has passed grande ronde valley
        self.grande_ronde_valley_passed = False
        # Flag for determining if the player has passed blue mountains
        self.blue_mountains_passed = False
        # Flag for determining if the player has passed fort walla walla
        self.fort_walla_walla_passed = False
        # Flag for determining if the player has passed the dalles
        self.the_dalles_passed = False
        # Flag for determining if the player has reached a landmark
        self.reached_landmark = True
        # Flag determines if the player is running the trail loop
        self.playing = False
        # Flag determines what the "talk to people" option message displays
        self.message = ""

    # List of months
    dates = [
        "MARCH",
        "APRIL",
        "MAY",
        "JUNE",
        "JULY",
        "AUGUST",
        "SEPTEMBER",
        "OCTOBER",
        "NOVEMBER",
        "DECEMBER",
    ]
    # List of locations
    locations = [
        "Kansas River",
        "Big Blue River",
        "Fort Kearney",
        "Chimney Rock",
        "Fort Laramie",
        "Independence Rock",
        "South Pass",
        "Fort Bridger",
        "Green River",
        "Soda Springs",
        "Fort Hall",
        "Snake River",
        "Fort Boise",
        "Grande Ronde Valley",
        "Blue Mountains",
        "Fort Walla Walla",
        "The Dalles",
    ]

    def print_inventory(self):
        """Function for printing the inventory"""
        # Determines what how much of each item is in the inventory
        console.clear()
        # Prints inventory
        print("█" * 79)
        print("")
        print("[cyan]Food: [/cyan]", int(self.amount_spent_on_food / 0.20))
        print(
            "[cyan]Bullets: [/cyan]", int(self.amount_spent_on_bullets / 2.00)
        )
        print(
            "[cyan]Clothing: [/cyan]",
            int(self.amount_spent_on_clothing / 10.00),
        )
        print(
            "[cyan]Supplies: [/cyan]",
            int(self.amount_spent_on_miscellaneous / 10.00),
        )
        print("[green]Money : $[/green]", player.money)
        print("")
        print("█" * 79)
        input("\nPress Enter to Continue...")

    def cont(self):
        """Function for "Press enter to continue" """
        option = input("Press Enter to Continue:")
        if option == "exit":
            return False

    def increment_turn(self):
        """Function for adding to the turn value"""
        self.current_date += 1

    def print_too_long(self):
        """Function for when the player has been on the trail too long"""
        print("[red]You have been on the trail for too long...[/red]")
        print(
            "[red]Your family dies in the \
    first blizzard of the winter[/red]"
        )
        self.dead = True

    def no_turns_left(self, arr):
        """Function for determining if the player has any turns left"""
        return self.current_date >= len(arr)

    def input_yes_no(self, message):
        """Function for a yes/no message"""
        reply = input(message)
        return True if "y" in reply else False

    def input_int(self, message):
        """Function for inputing only integers (unused so far)"""
        self.text_2_int = None
        while self.text_2_int == None:
            try:
                self.text_2_int = int(input(message))
            except ValueError:
                self.text_2_int = None
        return self.text_2_int

    def shooting(self):
        """Function for determining if the player wins a gun battle"""
        # List of words to select randomly
        words = [
            "BANG",
            "BLAM",
            "POW",
            "WHAM",
        ]
        # Takes random word from words list
        word = random.choice(words)
        # Takes the time from when the function began to after you typed
        # the word
        t0 = time.time()
        typed_word = input(f"\nType: {word}\n")
        t1 = time.time()
        B1 = int(t1 - t0)
        # Determines if you typed the word correctly
        if typed_word.lower() != word.lower():
            return 9
        return B1

    def illness(self):
        """Function for determining which illness the player recieves"""
        RND = random.random()
        if 100 * RND < 10 + 35 * (self.choice_of_eating - 1):
            print("\n[red]Mild Illness---Medicine Used[/red]\n")
            self.total_mileage -= 5
            self.amount_spent_on_miscellaneous -= 2
        elif 100 * RND < 100 - (40 / 4 ** (self.choice_of_eating - 1)):
            print("\n[red]Bad Illness---Medicine Used[/red]\n")
            self.total_mileage -= 5
            self.amount_spent_on_miscellaneous -= 5
        else:
            print("\n[red]Serious Illness[/red]\n")
            print("\n[red]!YOU MUST SEEK FOR MEDICAL ATTENTION![/red]\n")
            self.amount_spent_on_miscellaneous -= 10
            self.has_illness = True

    def hp(self):
        """Function for general player health"""
        if self.is_injured == True:
            vars.health = "Injured"
        elif self.is_injured == False:
            vars.health = "Healthy"

    def death(self):
        """Function for if the player is killed"""
        if self.dead == True:
            console.clear()
            # Displays a skull
            print(
                f"""[red]
                       uuuuuuuuuuuuuuuuuuuuu.
                   .u$$$$$$$$$$$$$$$$$$$$$$$$$$W.
                 u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Wu.
               $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i
              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
         `    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
           .i$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i
           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$W
          .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$W
         .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i
         #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
         W$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$u       #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$~
$#      `"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$i        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$         $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$.        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
 $$      $iW$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$!
 $$i      $$$$$$$#"" `""'%$$$$$$$$$$$$$$$$$%""''''#$$$$$$$$$$$$$$$W
 #$$W    `$$$#"            "       !$$$$$`           `"#$$$$$$$$$$#
  $$$     ``                 ! !iuW$$$$$                 #$$$$$$$#
  #$$    $u                  $   $$$$$$$                  $$$$$$$~
   "#    #$$i.               #   $$$$$$$.                 `$$$$$$
          $$$$$i.                ""'#$$$$i.               .$$$$#
          $$$$$$$$!         .   `    $$$$$$$$$i           $$$$$
          `$$$$$  $iWW   .uW`        #$$$$$$$$$W.       .$$$$$$#
            "#$$$$$$$$$$$$#`          $$$$$$$$$$$iWiuuuW$$$$$$$$W
               !#""    ""             `$$$$$$$##$$$$$$$$$$$$$$$$
          i$$$$    .                   !$$$$$$ .$$$$$$$$$$$$$$$#
         $$$$$$$$$$`                    $$$$$$$$$Wi$$$$$$#"#$$`
         #$$$$$$$$$W.                   $$$$$$$$$$$#   ``
          `$$$$##$$$$!       i$u.  $. .i$$$$$$$$$#""
             "     `#W       $$$$$$$$$$$$$$$$$$$`      u$#
                            W$$$$$$$$$$$$$$$$$$      $$$$W
                            $$`!$$$##$$$$``$$$$      $$$$!
                           i$" $$$$  $$#"`  ""'     W$$$$
                                                   W$$$$!
                      uW$$  uu  uu.  $$$  $$$Wu#   $$$$$$
                     ~$$$$iu$$iu$$$uW$$! $$$$$$i .W$$$$$$
             ..  !   "#$$$$$$$$$$##$$$$$$$$$$$$$$$$$$$$#"
             $$W  $     "#$$$$$$$iW$$$$$$$$$$$$$$$$$$$$$W
             $#`   `       ""#$$$$$$$$$$$$$$$$$$$$$$$$$$$
                              !$$$$$$$$$$$$$$$$$$$$$#`
                              $$$$$$$$$$$$$$$$$$$$$$!
                            $$$$$$$$$$$$$$$$$$$$$$$`
                             $$$$$$$$$$$$$$$$$$$$"
            [/red]"""
            )
        quit()


def health():
    """Function for determining what string the player health displays"""
    if vars.is_injured == True:
        vars.health = "Injured"
    elif vars.got_shot == True:
        vars.health = "Critical"
    else:
        vars.health = "Good"


class RandomSelection:
    """Class for determining a random member to give a disease to"""

    def __init__(self):
        """Variables for the class"""
        # Flag for which member's name is selected
        self.random_member = ""
        # Flag for which place in the list the afflicted member is in
        self.selected_member = 0
        # Flag for which disease is selected
        self.disease = ""
        # Flag for if a member is sick
        self.member_is_sick = False

    def rndmem(self):
        """Function chooses a random member from the player.mebmers list"""
        i = random.choice(range(len(player.members)))
        self.random_member = player.members[i]
        self.selected_member = i

    def random_disease(self):
        """Function for determining which event occurs"""
        self.disease = random.choice(self.diseases)

    def dead_member(self):
        """Function for which member to kill"""
        if self.selected_member == 0:
            del player.members[0]
        elif self.selected_member == 1:
            del player.members[1]
        elif self.selected_member == 2:
            del player.members[2]
        elif self.selected_member == 3:
            del player.members[3]

    # List of disease names
    diseases = [
        "typhoid",
        "cholera",
        "measles",
        "dysentery",
        "fever",
    ]


vars2 = RandomSelection()
vars = GameGlobals()
