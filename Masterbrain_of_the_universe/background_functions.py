'''THIS FILE HAS A BUNCH OF RANDOM FUNCTIONS THAT CLUTTER UP SPACE IN THE MAIN PROGRAMM'''

from typewriter_with_skip import typewriter_with_skip
import os, pandas, time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') 


def fancy_clear_screen():
    typewriter_with_skip("\n" * 15)
    os.system('cls' if os.name == 'nt' else 'clear') 

def quiz_database_initialisation():
    return pandas.read_csv('quiz_questions.csv')  # Return the loaded quiz questions database

def syntax_error():
    # Print an error message for invalid input
    typewriter_with_skip("syntax nuh ah")
    time.sleep(1)
    clear_screen()

