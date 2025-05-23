from file_handling import FileHandler
from miscellaneous_functions import UICleaner
from prompt_functions import ContinueOrExit, PromptValidator

class AnswerValidator:
    '''This is a code for validate_answer()'''
    
    def __init__(self, answer, correct_answer):
        self.answer = answer
        self.correct_answer = correct_answer

    def valid_ans(self):
        self.correct_answer = self.correct_answer.split()[0]

        if self.answer == self.correct_answer:
            return 1, self.correct_answer
        else:
            return 0, self.correct_answer

class ScoreKeeper:
    '''This is a code for score_keeper()'''

    def __init__(self, qna_list, score, point, answer):
        self.qna_list = qna_list
        self.score = score
        self.point = point
        self.answer = answer
    
    def score_counter(self):
        if self.point == 1:
            self.score += self.point
            self.answer = f"Correct! It was {self.answer}"
        else:
            self.answer = f"Incorrect! It was {self.answer}"

        self.qna_list.append(self.answer)

        return self.qna_list, self.score

class ShowFileContents:
    '''This is a code for show_contents()'''

    def __init__(self, file_path):
        self.file_path = file_path

    def show_contents(self):
        txt_file = FileHandler(self.file_path)

        if txt_file.file_empty_warning():
            return
        
        while True:
            UICleaner.clear_screen()

            try:
                with open(self.file_path, "r") as file_qna:
                    content = file_qna.read()
                    print(content)

                    action = ContinueOrExit()
                    action = action.continue_or_exit()

                    if action or action == "":
                        UICleaner.clear_screen()
                        return
            
            except FileNotFoundError:
                FileHandler.file_not_exists_warning()
                return

class DisplayQnA:

    def __init__(self, qna):
        UICleaner.clear_screen()
        self.qna = qna

    def display_questions(self):
        question_str = self.qna[1] + "\n"

        for i in range(4):
            letter = chr(ord("a") + i)
            question_str += f"{letter}. {self.qna[i+2]}\n"

        return question_str

class DisplayAnswers():
    
    def __init__(self, qna_list):
        self.qna_list = qna_list
    
    def display_ans(self):
        prompt_check = "Do you want to see the answers? (y/n): "
        valid_response = ["y", "n"]

        response = PromptValidator(prompt_check, valid_response).get_input()

        if response == "y":
            UICleaner.clear_screen()
            UICleaner.ascii_art("Answers\n")

            for number, qna in enumerate(self.qna_list):
                questions = DisplayQnA(qna).display_questions()
                display = f"{number+1}. {questions}{qna[7]}\n"
                print(display)    
                input("Press any key to continue...\n")
            return

        elif response == "n":
            return

if __name__ == "__main__":
    # This will store the objects
    scores = ScoreKeeper([], 23, 1, "a")

    scores.score_counter()

    # This will sote the behavoir of the objects
    print(scores.score_counter())