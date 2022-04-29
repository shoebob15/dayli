# shoe
# Function File Imports
from functions import *

# Module Imports
import sys
import os
from colorama import init, Fore, Back, Style

init()  # initialize colorama


def home():
    # main def const
    menu_actions = {}

    # small menu functions
    def menu_what_is_dayli():
        print("Dayli is a private, secure way to write down daily diary entires on your computer.")
        input("Press Enter to continue...")
        clear()
        print("You have the option to encrypt your files, which will keep your most private entries away from prying "
              "eyes.")
        input("Press Enter to continue...")
        clear()
        print("But Dayli's main goal is to just create a minimalistic and welcoming enviroment to write diary entries"
              "in")
        input("Press Enter to continue...")
        clear()
        print(Fore.BLACK + Style.BRIGHT + "Thank you for using Dayli!")
        print(Style.RESET_ALL)
        input("Press Enter to continue...")
        clear()
        main_menu()

    # Main menu
    def main_menu():
        clear()

        print("\n")
        print("Welcome to Dayli!\n")
        print("Please choose an option -->")
        print("1. Make an entry")
        print("2. Review previous entries")
        print("3. Unencrypt a previous entry")
        print("4. What is Dayli?")
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

    def menu4():
        menu_what_is_dayli()

    # Back to main menu
    def back():
        menu_actions['main_menu']()

    # Exit program
    def exit_menu():
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
        '4': menu4,
        '9': back,
        '0': exit_menu
    }

    # =======================
    #      MAIN PROGRAM
    # =======================

    main_menu()
