import time
from constants import (LOGO, INTRO_MESSAGE)
from question import Question

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


questions_prompt = [
    "1: What is regenerative farming?\n"
    "(A) A farming method that helps farmers decrease costs\n"
    "(B) new farming method seen on Doctor Who\n "
    "(C) A sustainable approach to farminng that locks carbon in the soil\n\n",
    "What color is strawberry?\n(a) purple\n (b) Green\n (c) Red\n\n"
    
    
    
    ]


questions =[
    Question(questions_prompt[0], "A"),
    Question(questions_prompt[1], "C")
    
    ]



def start_game():
    print(LOGO)
    time.sleep(1)
    user_name()
    time.sleep(1)
    print(INTRO_MESSAGE)
    time.sleep(1)
    # run_test(questions)
    time.sleep(1)

start_game()
