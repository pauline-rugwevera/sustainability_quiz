import time  # Module required to add a pause as needed
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
    "A A farming method that helps farmers decrease costs\n"
    "B new farming method seen on Doctor Who\n "
    "C A sustainable approach to farminng that locks carbon in the soil\n\n",
    "2: What color is strawberry?\n a purple\n b Green\n c Red\n\n"
    ]


questions = [
    Question(questions_prompt[0], "a", "oops\n"),
    Question(questions_prompt[1], "c", "cool\n")
    ]


def user_selection():
    """
    functin
    """
    option = input("Please choose an option:- (A/B)\n")
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
        else:
            print("Incorrect\n")






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
       
    

   

        

     
        

 
    
    
        
    
    
    
        

    

       
        
       

        # print(question.feedback)
        # time.sleep(3)
        
        
def start_game():
    """
    function to
    """
    # print(LOGO)
    # time.sleep(1)
    # user_name()
    # time.sleep(1)
    # print(INTRO_MESSAGE)
    # time.sleep(3)
    run_test(questions)
    
    time.sleep(1)


start_game()
