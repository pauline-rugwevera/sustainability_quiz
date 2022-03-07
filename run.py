"""
 # Module required to add a pause as needed
"""
import time  # Module required to add a pause as needed
from datetime import datetime
from tabulate import tabulate
import gspread
from google.oauth2.service_account import Credentials
from constants import (LOGO, INTRO_MESSAGE)
from question import Question
from question import Menu

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('sustainability')

scores = SHEET.worksheet('scores')
data = scores.get_all_values()

now = datetime.now()
# dd/mm/YY H:M
dt_string = now.strftime("%d/%m/%Y %H:%M")


# def user_name():
#     """
#     Function to accept and validate user name
#     """
#     name_entry = input("Please enter your name: -(Minimum 3 characters)\n")
#     if len(name_entry) < 3:
#         print("Enter at least 3 letters")
#         return user_name()
#     elif name_entry.isdigit():
#         print("Only letters allowed!")
#         return user_name()
#     else:
#         print(f"\nWelcome to the Sustainability Quiz {name_entry}\n")




name_entry = input("Please enter your name: -(Minimum 3 characters)\n")

if len(name_entry) < 3:

    print("Enter at least 3 letters")
    name_entry = input("Please enter your name: -(Minimum 3 characters)\n")
    
elif name_entry.isdigit():

    print("Only letters allowed!")
    name_entry = input("Please enter your name: -(Minimum 3 characters)\n")
       
else:
    print(f"\nWelcome to the Sustainability Quiz {name_entry}\n")
    

# menu_prompt = [
#     "What will you like to do\n"
#     "A: PLAY\n"
#     "B: QUIT"
# ]
# menus = [
#     Menu(menu_prompt[0], "a")
# ]


# def display_menu(menus):
#     """
#     function to display the menuS
#     """
#     for menu in menus:
#         print(menu.prompt)
#         if user_selection() == menu.choice:
#             # run_test(questions)
#             print("Good to have you on board\n\n")
#             time.sleep(2)
#         else:
#             print('ok')










def display_menu():
    """
    function to display menu to choose from beginning of quiz
    """
    print("what do you want to do?\n\n")
    menu = (input("A: Play Quiz\nB: Show Top Ten scores\n\
D: Quit\n").lower())

    if menu == "a":
        print("Starting the quiz....\n")
        time.sleep(1)
        run_test(questions)
    if menu == "b":
        print("Processing the scoreboard")
        time.sleep(2)
        # print(tabulate(data, headers='firstrow', showindex='always'))
        print(tabulate(data[0:11], headers='firstrow',
        tablefmt='fancy_grid'))



        

        

questions_prompt = [
    "1: What is regenerative farming?\n\n"
    "A: A farming method that helps farmers decrease costs\n"
    "B: new farming method seen on Doctor Who\n"
    "C: A sustainable approach to farminng that locks carbon in the soil\n",
    "2: Why is it good to buy organic, regeneratively farmed products when you"
    "can?\n\n"
    "A: Organic produces faster\n"
    "B: Organic is healthier for people, planet and help tackling climate "
    "change\n"
    "C: Because farmers get paid more for their products\n"
    ]
questions = [
    Question(questions_prompt[0],
             "a",
             "Not too hard to start you off, regenerative"
             "farming is a sustainable approach to "
             "farming that focuses on soil regeneration, "
             "increasing biodiversity, locking-in carbon "
             "and strengthening the health and vitality of the soil.\n"),
    Question(questions_prompt[1],
             "b",
             "Did you know? Organic, regeneratively farmed products "
             "are made in a way that puts the environment first "
             "by choosing products like this you can help make positive "
             "steps in the fight against climate change.\n"),


]


def user_selection():
    """
    function to accet user choice of answers
    """
    option = input("Please choose an option:- (A/B/C)\n")
    choice_lc = option.lower()
    if choice_lc not in ['a', 'b', 'c']:
        print('invalid_choice')
        return user_selection()

    return choice_lc


def run_test(questions):

    """
    function display question and check if answer is correct to provide
    feedback
    """
    score = 0
    for question in questions:
        print(question.prompt)
        if user_selection() == question.answer:
            score += 1
            print("Weldone\n")
            time.sleep(1)
            print(question.feedback)
            time.sleep(2)

        else:
            print("Incorrect\n")
            time.sleep(1)
            print(question.feedback)
            time.sleep(2)
        
    print("You got", score, "out of 10")
    time.sleep(1)
    print("Now updating the score board")
    scores = SHEET.worksheet('scores')
    scores.append_row(values=[name_entry, score, dt_string])
    scores.sort((2, 'des'), (4, 'asc'),)





def start_game():
    """
    function to
    # """
    # print(LOGO)
    # time.sleep(1)
  
    # time.sleep(1)
    # print(INTRO_MESSAGE)
    # time.sleep(3)
    display_menu()
    # run_test(questions)


start_game()
