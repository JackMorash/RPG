import random
import time

from rich import print
from rich.console import Console

console = Console()


class Character:
    def __init__(self):
        self.money = 1600
        self.bullets = 999
        self.water = 0
        self.oxen = 999
        self.parts = 999
        self.medicine = 999
        self.clothes = 999
        self.food = 9999


class Player(Character):
    def __init__(self):
        """Function for creating player-based variables"""
        super().__init__()
        self.name = ""
        self.job = ""
        self.members = ["Player 1", "Player 2", "Player 3", "Player 4"]
        self.cold = False
        self.alive = True
        self.repair = False
        self.miles = 0


player = Player()


class GameGlobals:
    """Sets global game variables"""

    def __init__(self):
        self.dead = False
        self.GOAL_IN_MILES = 2040
        self.SOUTH_PASS_IN_MILES = 950
        self.amount_spent_on_animals = player.oxen
        self.amount_spent_on_bullets = player.bullets
        self.amount_spent_on_clothing = player.clothes
        self.cash_total = player.money
        self.amount_spent_on_miscellaneous = player.parts
        self.amount_spent_on_food = player.food
        self.total_mileage = player.miles
        self.is_sufficient_clothing = False
        self.current_date = 1
        self.shooting_level = 5
        self.choice_of_eating = 0
        self.has_cleared_south_pass = False
        self.has_cleared_blue_montains = False
        self.fraction_of_2_weeks = 0
        self.is_injured = False
        self.is_blizzard = False
        self.total_mileage_previous_turn = 0
        self.distance_to_landmark = 0
        self.has_illness = False
        self.hostility_of_riders = False
        self.has_fort = False
        self.got_shot = False
        self.cold_weather = False
        self.raining = False
        self.weather = "Fine"
        self.health = "Healthy"
        self.food_quality = "Filling"
        self.location = "Independence, Missouri"
        self.chimney_rock = False
        self.green_river_crossing = False
        self.fort_bridger = False
        self.fort_walla_walla = False
        self.the_dalles = False
        self.kansas_river_passed = False
        self.big_blue_river_passed = False
        self.fort_kearney_passed = False
        self.fort_laramie_passed = False
        self.chimney_rock_passed = False
        self.independence_rock_passed = False
        self.south_pass_passed = False
        self.snake_river_passed = False
        self.fort_bridger_passed = False
        self.green_river_passed = False
        self.soda_springs_passed = False
        self.fort_hall_passed = False
        self.fort_boise_passed = False
        self.grande_ronde_valley_passed = False
        self.blue_mountains_passed = False
        self.fort_walla_walla_passed = False
        self.the_dalles_passed = False
        self.member = False
        self.reached_landmark = True
        self.playing = False

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

    def landmark_message(self):
        if self.location == "Kansas River":
            console.clear()
            print(
                """[cyan]A Ferry Operator tells you:\n "Don't try to ford any river\ndeeper than the wagon bed --\nabout two and a half feet" 



"""
            )

    def print_inventory(self):
        """Function for printing the inventory"""
        # Determines what how much of each item is in the inventory
        self.amount_spent_on_food = max(int(self.amount_spent_on_food), 0)
        self.amount_spent_on_bullets = max(
            int(self.amount_spent_on_bullets), 0
        )
        self.amount_spent_on_clothing = max(
            int(self.amount_spent_on_clothing), 0
        )
        self.amount_spent_on_miscellaneous = max(
            int(self.amount_spent_on_miscellaneous), 0
        )
        # Prints inventory
        print("█" * 79)
        print("[cyan]Food: [/cyan]", self.amount_spent_on_food)
        print("[cyan]Bullets: [/cyan]", self.amount_spent_on_bullets)
        print("[cyan]Clothing: [/cyan]", self.amount_spent_on_clothing)
        print("[cyan]Supplies: [/cyan]", self.amount_spent_on_miscellaneous)
        print("[green]Money : $[/green]", player.money)
        print("█" * 79)
        input("-->")

    def cont(self):
        """Function for "Press enter to continue" """
        option = input("Press Enter to Continue:")
        if option == "exit":
            return False
        elif ValueError():
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
            except:
                self.text_2_int = None
        return self.text_2_int

    def shooting(self):
        """Function for determining if the player wins a gun battle"""

        words = [
            "\nType: BANG\n",
            "\nType: BLAM\n",
            "\nType: POW\n",
            "\nType: WHAM\n",
        ]
        word = random.choice(words)
        t0 = time.time()
        typed_word = input(word)
        t1 = time.time()
        B1 = int(t1 - t0) - (self.shooting_level)
        if typed_word != word:
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
            health = "Injured"
        elif self.is_injured == False:
            health = "Healthy"

    def death(self):
        if self.dead == True:
            print(
                f"""[white]
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
            [/white]"""
            )
        return False


def health():
    if vars.is_injured == True:
        health = "Injured"
    elif vars.got_shot == True:
        health = "Critical"
    else:
        health = "Good"


class Random_Selection:
    def __init__(self):
        self.random_member = ""
        self.selected_member = 0
        self.disease = ""
        self.member_is_sick = False

    def rndmem(self):
        x = random.randint(0, 3)
        if x == 0:
            self.random_member = player.members[0]
            self.selected_member = 0
        elif x == 1:
            self.random_member = player.members[1]
            self.selected_member = 1
        elif x == 2:
            self.random_member = player.members[2]
            self.selected_member = 2
        elif x == 3:
            self.random_member = player.members[3]
            self.selected_member = 3

    def random_disease(self):
        """Function for determining which event occurs"""
        self.disease = random.choice(self.diseases)

    def dead_member(self):
        if self.selected_member == 0:
            del player.members[0]
        elif self.selected_member == 1:
            del player.members[1]
        elif self.selected_member == 2:
            del player.members[2]
        elif self.selected_member == 3:
            del player.members[3]

    diseases = [
        "typhoid",
        "cholera",
        "measles",
        "dysentery",
        "fever",
    ]


vars2 = Random_Selection()
vars = GameGlobals()
