class Question:
    """
    creates a question class
    """
    def __init__(self, prompt, answer, feedback):
        self.prompt = prompt
        self.answer = answer
        self.feedback = feedback
        

class Menu:
    """
    creates pay and quit class
    """
    def __init__(self, prompt, choice):
        self.prompt = prompt
        self.choice = choice
