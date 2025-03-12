import pandas as pd
import os
def variable_initualisation():
    # Preform all global variables here
    global quiz_questions_database
    #
    # Begin variable initialisation
    quiz_questions_database = pd.read_csv('quiz_questions.csv') #reads the csv file

def syntax_error():
    print("Syntax Error: Please enter a valid input.")


def loading_screen():
    pass

def welcome_to_quiz():
    pass

def quiz_type_select():
    print("Choose your quiz topic:")
    categories = quiz_questions_database["category"].unique() # get unique catagories
    for i, category in enumerate(categories, 1):
        print(f"{i}) {category}")
    category_numbers = ", ".join(str(i) for i in range(1, len(categories) + 1))
    current_user_input = input(f"Choose your quiz topic ({category_numbers}): ")
    if current_user_input.isdigit() and 1 <= int(current_user_input) <= len(categories):
        quiz_category = categories[int(current_user_input) - 1]
        quiz_questions = quiz_questions_database[quiz_questions_database["category"] == quiz_category]
    else:
        syntax_error()
        quiz_type_select()

def main(): # Mainline for the program
    variable_initualisation()
    loading_screen()
    welcome_to_quiz()
    quiz_type_select()

main()

