
class PromptValidator:
    '''This is a class for prompt_validation()'''

    def __init__(self, prompt, valid_response=None):
        self.prompt = prompt
        self.valid_response = valid_response

    def get_input(self, new_prompt=None):

        if new_prompt:
            prompt = new_prompt
        else:
            prompt = self.prompt

        while True:

            response = input(prompt).strip().lower()

            if not response: 
                print("Your input is invalid!")
                continue

            if self.valid_response:
                if response in self.valid_response:
                    return response
                
                warning = f"Input is invalid! Enter only {'/'.join(self.valid_response)}!"
                print(warning)

            else:
                return response
            
class QuestionEntry(PromptValidator):
    '''THis is a class for prompt_question()'''

    def __init__(self):
        super().__init__(prompt=None)

    def get_question(self):
        question = self.get_input("Enter a question entry: ")
        return question

class ChoicesEntry(PromptValidator):
    '''This is a class for prompt_choices()'''

    def __init__(self):
        super().__init__(prompt=None)

    def get_choices(self):
        choices_list = []
        for i in range(4):
            letter = chr(ord("a") + i)
            choice = self.get_input(f"Enter an answer for {letter}: ")
            choices_list.append(choice)

        choices_list = " | ".join(choices_list)
        
        return choices_list

class CorrAnsEntry(PromptValidator):
    ''' This is a class for prompt_correct_answer()'''
    prompt_letter = "Enter the letter of the correct answer: "
    letter_choices = ["a", "b", "c", "d"]

    def __init__(self):
        super().__init__(self.prompt_letter, self.letter_choices)
    
    def get_correct_answer(self):
        correct_ans = self.get_input()
        return correct_ans

class ContinueOrExit(PromptValidator):
    '''This is a class for continue_or_exit()'''
    
    prompt_check = "Do you want to continue? (y/n): "
    valid_response = ["y", "n"]

    def __init__(self):
        super().__init__(self.prompt_check, self.valid_response)

    def continue_or_exit(self):
        response = self.get_input()
        return response
    
class FileRetriever(PromptValidator):

    def __init__(self):
        ask = "Enter the file name: "
        super().__init__(prompt=ask)

    def get_file_name(self):
        return self.get_input() 

if __name__ == "__main__":
    # This will store all of the objects

    question_validator = QuestionEntry("Enter a question entry: ")
    choices_validator = ChoicesEntry()
    correct_answer_validator = CorrAnsEntry("Enter the letter of the correct answer: ", ["a", "b", "c", "d"])


    decision = ContinueOrExit()
    print(decision.continue_or_exit())

    # This will store the behavior of the object
    question = question_validator.get_question()
    print(question)

    choices = choices_validator.get_choices()
    print(choices)

    correct_answer = correct_answer_validator.get_correct_answer()
    print(correct_answer)