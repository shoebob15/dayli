# shoe
# Function File Imports
from functions import *

# Module Imports
import sys, os

def home():
    # Main definition - constants
    menu_actions  = {}  

    # =======================
    #     MENUS FUNCTIONS
    # =======================

    # Main menu
    def main_menu():
        os.system('cls')

        print("Welcome to Dayli!\n")
        print("Please choose a valid option ->")
        print("1. Make an entry")
        print("2. Review previous entries")
        print("3. Unencrypt a previous entry")
        print("\n0. Quit")
        choice = input(" >>  ")
        exec_menu(choice)

        return


    def exec_menu(choice):
        os.system('cls')
        ch = choice.lower()
        if ch == '':
            menu_actions['main_menu']()
        else:
            try:
                menu_actions[ch]()
            except KeyError:
                print("StOp tRyInG tO bReAk My PrOgRaM!!1! D:\n")
                menu_actions['main_menu']()
        return

    # Menu 1
    def menu1():
        entry()
        return

    # TODO: Make menu 2 and menu 3 operational

    # Menu 2
    def menu2():
        print("Sorry, still in development! Release TBD")
        time.sleep(3)
        main_menu()

    def menu3():
        print("Sorry, still in development! Release TBD")
        time.sleep(3)
        main_menu()
        choice = input(" >>  ")
        exec_menu(choice)
        return

    # Back to main menu
    def back():
        menu_actions['main_menu']()

    # Exit program
    def exit():
        sys.exit()

    # =======================
    #    MENUS DEFINITIONS
    # =======================

    # Menu definition
    menu_actions = {
        'main_menu': main_menu,
        '1': menu1,
        '2': menu2,
        '3': menu3,
        '9': back,
        '0': exit
    }

    # =======================
    #      MAIN PROGRAM
    # =======================

    main_menu()

