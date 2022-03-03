import time  # Module required to add a pause as needed
from constants import (LOGO, INTRO_MESSAGE)
from question import Question
from question import Menu



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


menu_prompt = [
    "What will you like to do\n"
    "A: PLAY\n"
    "B: QUIT"
]
menus = [
    Menu(menu_prompt[0], "a")
]



def display_menu(menus):
    """
    function to display the menuS
    """
    for menu in menus:
        print(menu.prompt)
        if user_selection() == menu.choice:
            run_test(questions)
        else:
            print('ok')
            
       
     
    





questions_prompt = [
    "1: What is regenerative farming?\n\n"
    "A: A farming method that helps farmers decrease costs\n"
    "B: new farming method seen on Doctor Who\n"
    "C: A sustainable approach to farminng that locks carbon in the soil\n",
    "2: Why is it good to buy organic, regeneratively farmed products when you can?\n\n" 
    "A: Organic produces faster\n"
    "B: Organic is healthier for people, planet and help tackling climate change\n"
    "C: Because farmers get paid more for their products\n"
    ]


questions = [
    Question(questions_prompt[0], "a", 
    "Not too hard to start you off, regenerative "
    "farming is a sustainable approach to "
    "farming that focuses on soil regeneration, "
    "increasing biodiversity, locking-in carbon "
    "and strengthening the health and vitality of the soil.\n"),
    Question(questions_prompt[1], "b", 
    "Did you know? Organic, regeneratively farmed products "
    "are made in a way that puts the environment first "
    "by choosing products like this you can help make positive "
    "steps in the fight against climate change.\n")
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
    function display question and check if answer is correct to provide feedback
    """
    for question in questions:
        print(question.prompt)
        if user_selection() == question.answer:
            print("Weldone\n")
            time.sleep(1)
            print(question.feedback)
            time.sleep(2)

        else:
            print("Incorrect\n")
            time.sleep(1)
            print(question.feedback)
            time.sleep(2)






# def run_test(questions):

#     """
#     function display question and check if answer is correct to provide feedback
#     """
#     for question in questions:
#         print(question.prompt)
#         option = input("Please choose an option:- (A/B)\n").lower()
#         time.sleep(1)
#         if option == question.answer:
#             print('Weldone')
#         else:
#             print("A big no")

       
#         if option not in ['a', 'b', 'c']:
#             print('invalid_choice')
#             return run_test(questions)

      
     

    # return choice_lc
       
       
        # time.sleep(3)
        
        
def start_game():
    """
    function to
    # """
    # print(LOGO)
    # time.sleep(1)
    # user_name()
    # time.sleep(1)
    # print(INTRO_MESSAGE)
    # time.sleep(3)
    # display_menu(menus)
    run_test(questions)

    # time.sleep(1)


start_game()
