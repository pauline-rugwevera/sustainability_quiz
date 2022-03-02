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
    "A A farming method that helps farmers decrease costs\n"
    "B new farming method seen on Doctor Who\n "
    "C A sustainable approach to farminng that locks carbon in the soil\n\n",
    
    "2: What color is strawberry?\n a purple\n b Green\n c Red\n\n"
    
    ]


questions = [
    Question(questions_prompt[0], "A", "oops\n"),
    Question(questions_prompt[1], "C", "cool\n")
    
    ]



def user_selection():
    """
    Function to accept user answer,validate it
    """
    option = input("Please choose an option:- (A/B/C)\n")
    accepted_choice = option.lower()
    if accepted_choice not in ['a', 'b', 'c']:
        print("Not a valid choice")
        return user_selection()

    return accepted_choice


# def run_test(questions):
#     """function
#     """
#     for question in questions:
#         print(question.prompt)
#         option = input(question.select)
#         accepted_choice = option.lower()

#         if accepted_choice not in ['a', 'b', 'c']:
#               print("Not a valid choice")
#               option = input(question.select)
#               time.sleep(1)
        



       

    
   

def run_test(questions):
    """
    function
    """
    for question in questions:

        #   answer = print(question.prompt)
        print(question.prompt)
        #   user_selection()
        user_selection()
      
        print(question.feedback)
        time.sleep(3)
        
        
    
    
        

        

      

            
          

# def run_test(questions):
#     """
#     function
#     """ 
#     for question in questions:
#         answer = question.answer
#         print(answer)   

      
      

    
        
 
       
        # if option == question.answer:
        #     print("ok")
       
        



def start_game():
    """
    function to
    """
    print(LOGO)
    time.sleep(1)
    user_name()
    time.sleep(1)
    print(INTRO_MESSAGE)
    time.sleep(3)
    run_test(questions)
 
    time.sleep(1)
    

start_game()
