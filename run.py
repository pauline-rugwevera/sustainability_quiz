import time
from constants import (LOGO, INTRO_MESSAGE)

def user_name():
    """
    Function to accept and validate user name
    """
    name_entry = input("Please enter your name: -(Minimum 3 characters)\n")
    
    if len(name_entry) < 3:
        print("Enter at least 3 letters")
        return user_name()
    else:
        print(f"\nWelcome to the Sustainability Quiz {name_entry}\n")


def start_game():
    print(LOGO)
    time.sleep(1)
    user_name()
    time.sleep(1)
    print(INTRO_MESSAGE)

start_game()
