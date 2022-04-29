# shoe
# import stuff
import os
import time
from cryptography.fernet import Fernet
from pynput import keyboard

dict1 = {}

# Lambada functions
clear = lambda: os.system("cls")


# reg functions
def entry():
    # Keystroke listener junk

    current = set()

    def on_press(key):
        pass

    def on_release(key):
        pass

    # End of keystroke listener junk

    filename = input(
        "What would you like to call this entry? No special characters, like /, \, ', etc. (Subject, "
        "date (Using periods), etc): "
    )
    filename += ".txt"
    makeentry = os.path.join(
        r"C:\Users\Owner\PycharmProjects\dailydiary\entries", filename
    )

    writeentry = open(makeentry, "w")

    clear()
    entry.entrybodyglob = input(
        "Welcome to the entry maker! Write what you want, then hit enter when you are finished: "
    )

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

    clear()

    writeentry.write(str(entry.entrybodyglob))
    encryptquestion = input("Would you like to encrypt this file? ")

    # Encryption stuff
    if encryptquestion == "Yes" or "yes":
        key = Fernet.generate_key()
        encryptpath = os.path.join(
            r"C:\Users\Owner\PycharmProjects\dailydiary\encryptKeys", filename
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
    elif encryptquestion == "No" or "no":
        print("Ok, not encrypting. Entry added!")
    else:
        print("Please enter a valid option...")

    time.sleep(2.5)
    return
