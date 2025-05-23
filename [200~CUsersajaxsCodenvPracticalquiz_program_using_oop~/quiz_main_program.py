import time
import quiz_functions
from prompt_functions import PromptValidator, FileRetriever
from miscellaneous_functions import UICleaner
from file_handling import PathHandler, FileHandler
from game_functions import ShowFileContents

class ProgramFunctions():

    @staticmethod
    def start_program():
        UICleaner.clear_screen()
        
        while True:
            UICleaner.ascii_art("Welcome!")
            print("""a. Create/Add QnA to a file
b. Start a quiz
c. Show contents of file
d. Delete a specific QnA in a file
e. Exit program\n""")
        
            ask = "What do you want to do? (a/b/c/d/e): "
            choices = ["a", "b", "c", "d", "e"]

            action = PromptValidator(ask, choices).get_input()

            if action == "a":
                obj_init = quiz_functions.QuizCreator()
                obj_init.create_quiz()
            
            elif action == "b":
                txt_file = FileRetriever().get_file_name()
                file_path = PathHandler(txt_file).get_file_path()

                try:
                    if not quiz_functions.QuizInitiator().start_quiz():
                        print("Exiting the program...")
                        time.sleep(3)
                        UICleaner.clear_screen()
                        return
                
                except FileNotFoundError:
                    FileHandler.file_empty_warning()
                    continue
                
            elif action == "c":
                txt_file = FileRetriever().get_file_name()
                file_path = PathHandler(txt_file).get_file_path()

                ShowFileContents(file_path).show_contents()

            elif action == "d":
                quiz_functions.QuizModifier().delete_qna()
                
            elif action == "e":
                break


if __name__ == "__main__":
    ProgramFunctions.start_program()