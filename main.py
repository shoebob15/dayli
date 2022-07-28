# shoe 
from time import sleep
from homescreen import *
from homescreen import home
import configparser
import sys
import os
# grab vars from ini

pathofentries = parser.get('settings', 'pathofentries')
pathofkeys = parser.get('settings', 'pathofkeys')
username = parser.get('settings', 'name')
firsttime = parser.get('mostlystaticvars', 'firsttime')
clear()

entriesdirectoryexists = os.path.isdir(pathofentries)
if entriesdirectoryexists:
    print("Entries directory found")
else:
    pathofentriesinput = input(
        "Entries directory not found. It may have been relocated, renamed, or deleted. It also may have been entered incorrectly. Would you like to (1) change the path to the entries directory, or (2) quit the program? ")
    if pathofentriesinput == '1':
        clear()
        while not entriesdirectoryexists:
            print(r"Please enter the new path to the entries directory. Add it like this: C:\Users\Owner\Desktop\Entries: ")
            newEntriesPath = input()

            parser.set('settings', 'pathofentries', newEntriesPath)
            entriesdirectoryexists = os.path.isdir(newEntriesPath)
            with open(configsetupfile, "w") as conf_file:
                parser.write(conf_file)
            entriesdirectoryexists = entriesdirectoryexists
            clear()
    if pathofentriesinput == '2':
        sys.exit()

if firsttime == 'yes':
    print("Hello, and welcome to Dayli!")
    input("Press Enter to continue...")
    clear()
    print("Dayli is a secure way to make virtual diary entries on the computer.")
    input("Press Enter to continue...")
    clear()
    print("You have the option to encrypt files, read files, and more!")
    input("Press Enter to continue...")
    clear()
    print(
        r"First we have to do some setup. Where would you like to have your keys for your encrypted files stored? (Add it as a full path like this: C:\Users\Owner\Desktop\EncryptKeys): ")
    firsttimekeypath = input()

    parser.set('settings', 'pathofkeys', firsttimekeypath)
    with open(configsetupfile, "w") as conf_file:
        parser.write(conf_file)

    print(
        r"Now let's set where you want your entries stored. (Add it as a full path like this: C:\Users\Owner\Desktop\Entries")
    firsttimeentrypath = input()

    parser.set('settings', 'pathofentries', firsttimeentrypath)
    with open(configsetupfile, "w") as conf_file:
        parser.write(conf_file)

    print(
        "Last but not least, would you like to add a username? This is completely optional, and is not required. Type in 1 if you do want to do a username, and type in 2 if you don't. ")
    nameofusermenu = input()
    if nameofusermenu == '1':
        print("What do you want your username to be? ")
        nameofuser = input()

        parser.set('settings', 'name', nameofuser)
        with open(configsetupfile, "w") as conf_file:
            parser.write(conf_file)

    elif nameofusermenu == '2':
        parser.set('mostlystaticvars', 'usesname', 'no')
        with open(configsetupfile, "w") as conf_file:
            parser.write(conf_file)

        print(
            "Ok, that's fine. And remember, you can change any of these settings in the settings menu of the home screen. Thanks for using Dayli!")
        sleep(2.5)

    else:
        print("Please select a valid option.")

    parser.set('mostlystaticvars', 'firsttime', 'no')
    with open(configsetupfile, "w") as conf_file:
        parser.write(conf_file)


clear()
print("\n\n\n")
print("      $$\                     $$\ $$\ ")
print("      $$ |                    $$ |\__|")
print(" $$$$$$$ | $$$$$$\  $$\   $$\ $$ |$$\ ")
print("$$  __$$ | \____$$\ $$ |  $$ |$$ |$$ |")
print("$$ /  $$ | $$$$$$$ |$$ |  $$ |$$ |$$ |")
print("$$ |  $$ |$$  __$$ |$$ |  $$ |$$ |$$ |")
print("\$$$$$$$ |\$$$$$$$ |\$$$$$$$ |$$ |$$ |")
print(" \_______| \_______| \____$$ |\__|\__|")
print("                    $$\   $$ |        ")
print("                    \$$$$$$  |        ")
print("                     \______/         ")

sleep(3)
clear()
home()
