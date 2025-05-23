import os
import time
from miscellaneous_functions import UICleaner

class PathHandler:
    '''This is a code for create_dir(), get_file(), and rename_file()'''
    def __init__(self, file_name):
        self.file_name = file_name

    @staticmethod
    def create_dir():
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        subdir_name = "questionnaire_inventory"

        dir_path = os.path.join(parent_dir, subdir_name)
        os.makedirs(dir_path, exist_ok=True)
        
        return dir_path
    
    def rename_file(self):
        file_name = self.file_name.strip().lower()
        file_name = file_name.replace(" ", "_")
        return file_name

    def get_file_path(self):
        file_path = self.rename_file()
        dir = PathHandler.create_dir()

        full_path = os.path.join(dir, file_path)
        
        if not full_path.endswith(".txt"):
            file_path = f"{full_path}.txt"

        return file_path
    
class FileHandler:

    def __init__(self, file_path):
        self.file_path = file_path

    @staticmethod
    def file_not_exists_warning():
        UICleaner.clear_screen()
        UICleaner.ascii_art("File does not exist.")
        time.sleep(3)
        UICleaner.clear_screen()    

    def file_empty_warning(self):
        try:   
            with open(self.file_path, "r") as file:
                content = file.read()

            if content.strip() == "":
                UICleaner.clear_screen()
                UICleaner.ascii_art("File is empty")
                time.sleep(3)
                UICleaner.clear_screen()
                return True

        except FileNotFoundError:
            FileHandler.file_not_exists_warning()
            return True

if __name__ == "__main__":

    file_name = PathHandler()
    file_path = file_name.get_file_path()

    check = FileHandler(file_path)
    check.file_empty_warning()
