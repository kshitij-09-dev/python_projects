#pip install pyautogui {for graphics}

import random
import pyautogui
import string

#chars = "abcdefghijklmnopqrstuvwxyz0123456789"
chars = string.printable
chars_list = list(chars)

password = pyautogui.password("Enter password")

guess_password = ""

while (guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))

    print("<=============" + str(guess_password) + "===============>")

    if(guess_password == list(password)):
        print("Password Cracked! password was = " + "".join(guess_password))
        break
