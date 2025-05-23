import os
import time
from art import text2art

class UICleaner:

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def ascii_art(text):
        print(text2art(text))
