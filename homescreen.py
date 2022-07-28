# sho
# Function File Imports
from time import sleep
# Module Imports
from colorama import init, Fore, Style
from configparser import ConfigParser
import os
from cryptography.fernet import Fernet
init()  # initialize colorama
clear = lambda: os.system('cls')  # define clear

configsetupfile = 'config.ini'  # conf file
parser = ConfigParser()  # define configparser object
parser.read(configsetupfile)  # read file
pathofentries = parser.get('settings', 'pathofentries')
pathofkeys = parser.get('settings', 'pathofkeys')


def home():
    # small menu functions (usually just printing stuff out to program)
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
        print("2. Review previous 10 entries")
        print("3. Unencrypt a previous entry")
        print("4. What is Dayli?")
        print("5. Settings")
        print("\n0. Quit")
        choice = input(" >>  ")
        if choice == "1":
            clear()
            menu1()
        elif choice == "2":
            clear()
            menu2()
        elif choice == "3":
            clear()
            menu3()
        elif choice == "4":
            clear()
            menu4()
        elif choice == "5":
            clear()
            menu5()
        return

    # Menu 1
    def menu1():
        entry()
        return

    # TODO: Make menu 2 and menu 3 operational

    # Menu 2
    def menu2():
        print(" Uhhhh, sorry. This file is MISSING (OH NOES!)")
        sleep(3)
        main_menu()

    def menu3():
        unencrypt()
        return

    def menu4():
        menu_what_is_dayli()
        return

    def menu5():
        clear()
        settings()
        return

    # BIG FUNCTIONS
    def entry():
        filename = input(
            "What would you like to call this entry? No special characters, like /, \, ', etc. (Subject, "
            "date (Using periods), etc): "
        )
        filename += ".txt"
        makeentry = os.path.join(
            pathofentries, filename
        )

        writeentry = open(makeentry, "w")

        clear()
        entry.entrybodyglob = input(
            "Welcome to the entry maker! Write what you want, then hit enter when you are finished: "
        )

        clear()

        writeentry.write(str(entry.entrybodyglob))
        encryptquestion = input("Would you like to encrypt this file? ")
        encryptquestion.lower()

        # Encryption stuff
        if encryptquestion == "yes":
            key = Fernet.generate_key()
            encryptpath = os.path.join(
                pathofkeys, filename
            )
            encryptpath += ".key"

            with open(encryptpath, "wb") as filekey:
                filekey.write(key)

            # opening the key
            with open(encryptpath, "rb") as filekey:
                key = filekey.read()

            # using the generated key
            fernet = Fernet(key)

            # opening the original file to encrypt
            with open(makeentry, "rb") as file:
                original = file.read()

            # encrypting the file
            encrypted = fernet.encrypt(original)

            # opening the file in write mode and
            # writing the encrypted data
            with open(makeentry, "wb") as encrypted_file:
                encrypted_file.write(encrypted)
            print("Encrypted! Also, entry added!")
        elif encryptquestion == "no":
            print("Ok, not encrypting. Entry added!")
        else:
            print("Please enter a valid option...")

        sleep(2.5)
        clear()
        return

    def unencrypt():
        print(
            "Listing all files in entry directory (TIP: If there is a lot of files, go into file explorer and type in your file from there.")
        for listfiles in os.listdir(pathofentries):
            if listfiles.endswith(".txt"):
                # Prints only text file present in My Folder
                print(listfiles)
        input("Press enter")
        home()

    def settings():
        settingselector = input("Welcome to settings! Please input an option number for the thing you want to change.")
        print("1. Change path of entries")
        print("2. Change path of encryption keys")
        print("3. Change name or add name")
        if settingselector == "1":
            print("Do something")
        elif settingselector == "2":
            print("Do something")
        elif settingselector == "3":
            print("Do something")
        elif settingselector == "4":
            print("Do something")
        else:
            print("Please enter again.")
            settings()


    main_menu()
