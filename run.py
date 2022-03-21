"""
 # Module required to add a pause as needed
"""
import time
from datetime import datetime
from tabulate import tabulate
import random
import gspread
from google.oauth2.service_account import Credentials
from constants import (LOGO, INTRO_MESSAGE, GAMEOVER)


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
dt_string = now.strftime("%d/%m/%Y %H:%M")


class Question:
    """
    creates a question class
    """
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions_prompt = [
    " What is regenerative farming?\n\n"
    "A: A farming method that helps farmers decrease costs\n"
    "B: new farming method seen on Doctor Who\n"
    "C: A sustainable approach to farminng that locks carbon in the soil\n",
    " Why is it good to buy organic, regeneratively farmed products when you"
    "can?\n\n"
    "A: Organic produces faster\n"
    "B: Organic is healthier for people, planet and help tackling climate "
    "change\n"
    "C: Because farmers get paid more for their products\n",
    " Which of the following is not a renewable energy source\n\n"
    "A: Wind\n"
    "B: Solar\n"
    "C: Coal\n",
    " What is biodiversity?\n\n"
    "A: A type of insects\n"
    "B: A measurement of different life forms in a particular place\n"
    "C: A type of plant species\n",
    " When travelling to school which mode the of transport "
    "of transport is best for environment?\n\n"
    "A: Car\n"
    "B: Bike\n"
    "C: Train\n",
    " What happens to waste that is not recycled?\n\n"
    "A: Landfill\n"
    "B: Throw into the sea\n"
    "C: Burn\n",
    " About 71% of the Earth is covered with water. How much of "
    "it is fresh water?\n\n"
    "A: 23%\n"
    "B: 2.5%\n"
    "C: 50%\n",
    " How many UN Sustainable development goals are there?\n\n"
    "A: 2\n"
    "B: 20\n"
    "C: 17\n",
    " Which animal produces the wool we use to make clothes?\n\n"
    "A: sheep\n"
    "B: chimpanzee\n"
    "C: cow\n",
    " How many blades does a wind turbine usually have?\n\n"
    "A: 1\n"
    "B: 2\n"
    "C: 3\n",
    " Which of these energy sources is a fossil fuel?\n\n"
    "A: Solar\n"
    "B: Gas Turbine \n"
    "C: Wind\n",
    " What is the number one ranked solution for fighting climate change?\n\n"
    "A: Manage refrigerants\n"
    "B: Waste less water\n"
    "C: Restore tropical forests\n",
    " What does the governments climate change watchdog recommend as a "
    "green substitute for air conditioning?\n\n"
    "A: Opening windows to help create a through draughtn \n"
    "B: Installing special blinds on glass and steel structures\n"
    "C: Allowing ivy to grow\n",
    " Which nation became the first to ban all metal mining,"
    "in an attempt to protect its freshwater supply?\n\n"
    "A: El Salvador\n"
    "B: Angola\n"
    "C: Brazil\n",
    " Which country generates the largest amount of solar power in the world?,"
    "\n\n"
    "A: Germany\n"
    "B: China\n"
    "C: Canada\n",
    " What does sustainability mean?\n\n"
    "A: using only fossil fuels\n"
    "B: using only non-renewable resources\n"
    "C: Avoiding the depletion of natural resources in order to maintain "
    "ecological balance.\n",
    " What is NOT a sustainable practice?\n\n"
    "A: buying\n"
    "B: recycling\n"
    "C: reusing.\n",
    " Which of the following increases demand that pushes the "
    "environment to its limit?\n\n"
    "A: farming\n"
    "B: population growth\n"
    "C: fossil fuels.\n",
    " Water resources are uniformly distributed around the world.\n\n"
    "A: True\n"
    "B: False\n"
    "C: Sometimes.\n",
    " Most energy used by humans comes from:\n\n"
    "A: China\n"
    "B: Brazil\n"
    "C: Sun\n",
    " What is one of the areas of the ocean called "
    "where marine debris (garbage) has combined due to ocean currents?\n\n"
    "A: The Great Pacific Garbage Patch\n"
    "B: The Great Pacific Pristine Pool\n"
    "C: The Great Pacific Dump Truck\n",
    "Organic waste, like fruits and vegetables, is considered\n\n"
    "A: nonbiodegradable\n"
    "B: Healthy\n"
    "C: biodegradable\n",
    " What is the definition of climate?\n\n"
    "A: The condition of the air around the Earth\n"
    "B: The pattern of weather over time\n"
    "C: The rainforest\n",
    " What are some possible solutions to climate change\n\n"
    "A: Use less energy\n"
    "B: Plant trees and other plants\n"
    "C: All of the above\n",
    " How many pieces of litter are estimated to enter the sea on "
    "a daily basis?\n\n"
    "A: 8 million\n"
    "B: 2 million\n"
    "C: 1million\n",
    " Which type of farming is sustainable\n\n"
    "A: Plantations\n"
    "B: shifting cultivation\n"
    "C: cattle ranching\n",
    " Eco-toirism should lead to\n"
    "A: Environmental tourism\n"
    "B: Sustainability\n"
    "C: Sustainable tourism\n",
    " Scientists are looking for new ways of generating hydrogen "
    "from most renewable energy\n"
    "A: solar energy\n"
    "B: sunlight\n"
    "C: coal\n",



]


questions = [
    Question(questions_prompt[0], "a"),
    Question(questions_prompt[1], "b"),
    Question(questions_prompt[2], "c"),
    Question(questions_prompt[3], "b"),
    Question(questions_prompt[4], "b"),
    Question(questions_prompt[5], "a"),
    Question(questions_prompt[6], "b"),
    Question(questions_prompt[7], "c"),
    Question(questions_prompt[8], "a"),
    Question(questions_prompt[9], "c"),
    Question(questions_prompt[10], "b"),
    Question(questions_prompt[11], "c"),
    Question(questions_prompt[12], "c"),
    Question(questions_prompt[13], "a"),
    Question(questions_prompt[14], "b"),
    Question(questions_prompt[15], "c"),
    Question(questions_prompt[16], "a"),
    Question(questions_prompt[17], "b"),
    Question(questions_prompt[18], "b"),
    Question(questions_prompt[19], "c"),
    Question(questions_prompt[20], "a"),
    Question(questions_prompt[21], "c"),
    Question(questions_prompt[22], "b"),
    Question(questions_prompt[23], "c"),
    Question(questions_prompt[24], "a"),
    Question(questions_prompt[25], "b"),
    Question(questions_prompt[26], "b"),

]


def user_selection():
    """
    function to accept user choice of answers
    """
    option = input("Please choose an option:- (A/B/C)\n")
    choice = option.lower()
    if choice not in ['a', 'b', 'c']:
        print('invalid_choice\n\n')
        return user_selection()

    return choice


def run_test(questions):

    """
    function to get user name, display question and check if
    answer is correct to provide
    feedback
    """
    while True:
        name = input(" Please enter your name below:\n")
        if name.isalpha():
            break
        print("Please enter characters A-Z only\n")
    print(f"\n Welcome to the Sustainability Quiz {name}\n\n")
    time.sleep(2)
    new_list = random.sample(questions, 10)
    score = 0
    for sample in new_list:

        print(sample.prompt)

        if user_selection() == sample.answer:
            score += 1
            print("Weldone\n\n")
            time.sleep(2)

        else:
            print("Incorrect\n\n")
            time.sleep(2)

    print("Thank you for completing the quiz " + name + "\n\n")
    print("You got", score, "out of 10\n\n")
    time.sleep(2)
    print("Now updating the score board...................................\n")
    time.sleep(2)
    scores = SHEET.worksheet('scores')
    scores.append_row(values=[name, score, dt_string])
    scores.sort((2, 'des'), (4, 'asc'),)
    time.sleep(1)
    print(GAMEOVER)
    time.sleep(1)
    print("Press P to replay the quiz\n")
    print("Press S to view the scoreboard\n")
    print("Click the RUN PROGRAM button to Quit the quiz\n")
    time.sleep(2)
    gameover_menu()


def quiz_instructions():
    """
    Function to display quiz instructions to the user
    """
    print("But first house keeping!\n\n")
    time.sleep(2)
    print(INTRO_MESSAGE)
    time.sleep(4)
    print("1. All questions are based on sustainability & climate change")
    print("2. All 10 questions are multiple choice based")
    print("3. Choose either a,b or c for correct answer")
    print("4. You will be told if your answer is correct or incorrect")
    print("5. Score increase is based on correct answers only")
    print("6. You will see your score at the end when you complete the quiz")
    print("7. Score is added to the scoreboard at the end of quiz\n\n")

    time.sleep(4)
    print("Now lets roll..........................................\n\n")


def second_menu():
    """
    Function that gives users ability to navigate around the quiz
    """
    press_key = input().lower()
    if press_key == "p":
        time.sleep(2)
        print("Good to have you onboard. Now starting the quiz\n\n")
        time.sleep(2)
        quiz_instructions()
        run_test(questions)

    if press_key == "q":
        time.sleep(2)
        print("Goodbye, hope to see you soon\n\n")
        time.sleep(2)
        start_game()

    else:
        print("Invalid choice")
        time.sleep(1)
        print("Press either P, Q or S!\n")
        second_menu()


def gameover_menu():
    """
    function to display menu to choose when the quiz game is over
    """

    press_key = input().lower()
    if press_key == "p":
        time.sleep(2)
        print("Good to have you onboard. Now starting the quiz\n\n")
        time.sleep(2)
        quiz_instructions()
        run_test(questions)
    if press_key == "s":
        time.sleep(2)
        print("Just a moment to process the scoreboard.....")
        data = scores.get_all_values()
        print(tabulate(data[0:11], headers='firstrow', tablefmt='fancy_grid'))
        # print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))
        time.sleep(4)
        print("Press P to proceed to Quiz\n")
        print("Press Q to quit")
        second_menu()
    else:
        print("Invalid input!")
        time.sleep(1)
        print("Press either P, S or Click the Run Program button")
        gameover_menu()


def display_menu():
    """
    function to display menu to choose from beginning of quiz
    """
    print("What do you want to do?\n\n")
    menu = (input("A: Play Quiz\nB: Show Top Ten scores\n").lower())

    if menu == "a":
        time.sleep(1)
        quiz_instructions()
        run_test(questions)
    if menu == "b":
        print("Just a moment to process the scoreboard.....")
        time.sleep(2)
        print(tabulate(data[0:11], headers='firstrow', tablefmt='fancy_grid'))
        time.sleep(4)
        print("Press P to proceed to Quiz\n")
        print("Press Q to quit")
        second_menu()
    if menu not in ['a', 'b']:
        print('Invalid_choice! Choose either A or B\n\n')
        return display_menu()


def start_game():
    """
    function to
    """

    print(LOGO)
    time.sleep(2)

    display_menu()


start_game()
