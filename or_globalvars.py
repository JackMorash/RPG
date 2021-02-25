import random
import time

from rich import print

from or_player import player


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
        self.is_sufficient_clothing = False
        self.current_date = 0
        self.shooting_level = 5
        self.choice_of_eating = 1
        self.amount_spent_on_food = player.food
        self.has_cleared_south_pass = False
        self.has_cleared_blue_montains = False
        self.fraction_of_2_weeks = 0
        self.is_injured = False
        self.is_blizzard = False
        self.total_mileage = 0
        self.amount_spent_on_miscellaneous = player.parts
        self.total_mileage_previous_turn = 0
        self.has_illness = False
        self.hostility_of_riders = False
        self.has_fort = False
        self.got_shot = False
        self.cold_weather = False
        self.raining = False
        self.weather = "Fine"
        self.health = "Healthy"

    dates = ["MARCH",
             "APRIL",
             "MAY",
             "JUNE",
             "JULY",
             "AUGUST",
             "SEPTEMBER",
             "OCTOBER",
             "NOVEMBER",
             "DECEMBER"]

    def print_inventory(self):
        """Function for printing the inventory"""
        # Determines what how much of each item is in the inventory
        self.amount_spent_on_food = max(int(self.amount_spent_on_food), 0)
        self.amount_spent_on_bullets = max(
            int(self.amount_spent_on_bullets), 0)
        self.amount_spent_on_clothing = max(
            int(self.amount_spent_on_clothing), 0)
        self.amount_spent_on_miscellaneous = max(
            int(self.amount_spent_on_miscellaneous), 0)
        # Prints inventory
        print("█"*79)
        print("[cyan]Food: [/cyan]", self.amount_spent_on_food)
        print("[cyan]Bullets: [/cyan]", self.amount_spent_on_bullets)
        print("[cyan]Clothing: [/cyan]", self.amount_spent_on_clothing)
        print("[cyan]Supplies: [/cyan]", self.amount_spent_on_miscellaneous)
        print("[green]Money : $[/green]", player.money)
        print("█"*79)
        input("-->")

    def cont():
        """Function for "Press enter to continue" """
        while True:
            option = input("Press Enter to Continue:")
            if option == "exit":
                return False
            else:
                break

    def increment_turn(self):
        """Function for adding to the turn value"""
        self.current_date += 1

    def print_too_long(self):
        """Function for when the player has been on the trail too long"""
        print("[red]You have been on the trail for too long...[/red]")
        print("[red]Your family dies in the \
    first blizzard of the winter[/red]")
        self.dead = True

    def no_turns_left(self, arr):
        """Function for determining if the player has any turns left"""
        return self.current_date >= len(arr)

    def input_yes_no(self, message):
        """Function for a yes/no message"""
        reply = input(message)
        return True if 'y' in reply else False

    def input_int(self, message):
        """Function for inputing only integers (unused so far)"""
        self.text_2_int = None
        while self.text_2_int == None:
            try:
                self.text_2_int = int(input(message))
            except:
                self.text_2_int = None
        return self.text_2_int

    def shooting(self, shooting_level):
        """Function for determining if the player wins a gun battle"""

        words = ["\nBANG\n", "\nBLAM\n", "\nPOW\n", "\nWHAM\n"]
        word = random.choice(words)
        t0 = time.time()
        typed_word = input("{}".format(word))
        t1 = time.time()
        B1 = (t1-t0)-(self.shooting_level)
        if typed_word != word:
            return 9
        return max(B1, 0)

    def illness(self):
        """Function for determining which illness the player recieves"""
        RND = random.random()
        if 100*RND < 10+35*(self.choice_of_eating-1):
            print("\n[red]MILD ILLNESS---MEDICINE USED[/red]\n")
            self.total_mileage -= 5
            self.amount_spent_on_miscellaneous -= 2
        elif 100*RND < 100-(40/4**(self.choice_of_eating-1)):
            print("\n[red]BAD ILLNESS---MEDICINE USED[/red]\n")
            self.total_mileage -= 5
            self.amount_spent_on_miscellaneous -= 5
        else:
            print("\n[red]SERIOUS ILLNESS[/red]\n")
            print("\n[red]YOU MUST STOP FOR MEDICAL ATTENTION[/red]\n")
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
            print("""
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
            """)
            return False


def health():
    if vars.is_injured == True:
        health = "Injured"
    elif vars.is_injured == False:
        health = "Good"


vars = GameGlobals()
