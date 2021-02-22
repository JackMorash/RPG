import or_events
import or_map


def walking_trail():
    print("March 1, 1848  --  Independence, Missuori")
    print("""
===============================================================================
    Weather:
    Health:
    Pace:
    Rations:
===============================================================================
You May:
    
    1. Continue on Trail
    2. Check supplies
    3. Check map
    """)
    option = input("What is your choice? ")
    if option == "1":
        or_events.events()
    elif option == "2":
        print()
    elif option == "3":
        or_map.map()
