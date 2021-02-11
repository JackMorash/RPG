import random
import time


def shooting(shooting_level):
    words = ["BANG", "BLAM", "POW", "WHAM"]
    word = random.choice(words)
    t0 = time.time()
    typed_word = input("TYPE {}: ".format(word))
    t1 = time.time()
    B1 = (t1-t0)-(shooting_level-1)
    if typed_word != word:
        return 9
    return max(B1, 0)


def illness(this_vars):
    RND = random.random()
    if 100*RND < 10+35*(this_vars.choice_of_eating-1):
        print("[red]Mild illness...[/red][pink]Medicine Used[/pink]")
        this_vars.total_mileage -= 5
        this_vars.amount_spent_on_miscellaneous -= 2
    elif 100*RND < 100-(40/4**(this_vars.choice_of_eating-1)):
        print("[red]Bad Illnesss...[/red][pink]Medicine used[/pink]")
        this_vars.total_mileage -= 5
        this_vars.amount_spent_on_miscellaneous -= 5
    else:
        print("[red]Serious Illness[/red]")
        print("[red]You must stop for medical attention!")
        this_vars.amount_spent_on_miscellaneous -= 10
        this_vars.has_illness = True
