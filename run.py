"""
 # Module required to add a pause as needed
"""
import time  # Module required to add a pause as needed
from datetime import datetime
from tabulate import tabulate
import gspread
from google.oauth2.service_account import Credentials
from constants import (LOGO, INTRO_MESSAGE, GAMEOVER)
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






# print(INTRO_MESSAGE)
# time.sleep(1)


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





def user_name():
    """
    Function to accept and validate user name
    """
    name_entry = input("Please enter your name: -(Minimum 3 characters)\n")
    if len(name_entry) < 3:
        print("Enter at least 3 letters")
        return user_name()
    elif name_entry.isdigit():
        print("Only letters allowed!")
        return user_name()
    else:
        print(f"\nWelcome to the Sustainability Quiz {name_entry}\n")


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
    name_entry = input("Please enter your name: -(Minimum 3 characters)\n")
    score = 0

    if len(name_entry) < 3:
        print("Enter at least 3 letters")
        name_entry = input("Please enter your name: -(Minimum 3 characters)\n")
    
    if name_entry.isdigit():
        print("Only letters allowed!")
        name_entry = input("Please enter your name: -(Minimum 3 characters)\n")
    
    else:
        print(f"\nWelcome to the Sustainability Quiz {name_entry}\n")  
        time.sleep(2)
    
    for question in questions:
        print(question.prompt)
        if user_selection() == question.answer:
            score += 1
            print("Weldone\n\n")
            time.sleep(1)
            print(question.feedback)
            time.sleep(2)

        else:
            print("Incorrect\n\n")
            time.sleep(1)
            print(question.feedback)
            time.sleep(2)
        
    print("Thank you for completing the quiz " + name_entry + "\n\n")
    print("You got", score, "out of 10\n\n")
    time.sleep(2)
    print("Now updating the score board...................\n")
    time.sleep(3)
    scores = SHEET.worksheet('scores')
    scores.append_row(values=[name_entry, score, dt_string])
    scores.sort((2, 'des'), (4, 'asc'),)
    print(GAMEOVER)
    time.sleep(5)
    start_game()


def quiz_instructions():
    """
    Function to display quiz instructions to the user
    """
    print("But first house keeping!\n\n")
    time.sleep(2)
    print(INTRO_MESSAGE)
    time.sleep(4)
    print("1. All questions are based on sustainability")
    print("2. All questions are multiple choice based")
    print("3. Choose either a,b or c for correct answer")
    print("4. You will be told if your answer is correct or incorrect")
    print("5. Score increase is based on correct answers only")
    print("6. You will see your score at the end when you complete the quiz")
    print("7. Score is added to the scoreboard at the end of quiz\n\n")

    time.sleep(4)
    print("Now lets roll..........\n\n")


def display_menu():
    """
    function to display menu to choose from beginning of quiz
    """
    print("what do you want to do?\n\n")
    menu = (input("A: Play Quiz\nB: Show Top Ten scores\n\
C: Quit\n").lower())

    if menu == "a":
        time.sleep(3)
        quiz_instructions()
        run_test(questions)
         
    if menu == "b":
        print("Just a moment to process the scoreboard.....")
        time.sleep(2)
        # print(tabulate(data, headers='firstrow', showindex='always'))
        print(tabulate(data[0:11], headers='firstrow',
        tablefmt='fancy_grid'))
        time.sleep(4)
        display_menu()
  
    if menu == "c":
        print("Goodbye Hope to see you soon.........\n")
        time.sleep(2)
        start_game()
    
    if menu not in ['a', 'b', 'c']:
        print('invalid_choice')
        return display_menu()








def start_game():
    """
    function to
    """

    print(LOGO)
    time.sleep(2)
    
    display_menu()


start_game()



# def run_test(questions):

#     """
#     function display question and check if answer is correct to provide
#     feedback
#     """
#     name_entry = input("Please enter your name: -(Minimum 3 characters)\n")

#     if len(name_entry) < 3:
#          print("Enter at least 3 letters")
#     name_entry = input("Please enter your name: -(Minimum 3 characters)\n")
    
#     if name_entry.isdigit():
#         print("Only letters allowed!")
#     name_entry = input("Please enter your name: -(Minimum 3 characters)\n")
    
#     else:
#         print(f"\nWelcome to the Sustainability Quiz {name_entry}\n")