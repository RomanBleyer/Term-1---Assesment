import pandas
import os
import random

def variable_initualisation():
    # Preform all global variables here
    global quiz_questions_database
    #
    # Begin variable initialisation
    quiz_questions_database = pandas.read_csv('quiz_questions.csv') #reads the csv file

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') # clears the screen

def fancy_clear_screen():
    print("\n" * 100) # clears the screen
    os.system('cls' if os.name == 'nt' else 'clear') # clears the screen

def syntax_error():
    print("Syntax Error: Please enter a valid input.")
    clear_screen()

def loading_screen():
    pass

def welcome_to_quiz():
    pass

def quiz_type_select():
    global quiz_questions
    #
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

def begin_selected_questions():
    first_question = quiz_questions.iloc[random.randint(0, len(quiz_questions) - 1)]
    print(f"Question: {first_question['question']} | Options: {first_question['options']}")
    current_user_input = input("Enter your answer: ")
    current_correct_answer = first_question['answer']
    if current_user_input.strip().lower() == current_correct_answer.strip().lower():
        print("Correct!")
    else:
        print(f"Incorrect! The correct answer was: {current_correct_answer}")

def main(): # Mainline for the program
    variable_initualisation()
    loading_screen()
    welcome_to_quiz()
    quiz_type_select()
    begin_selected_questions()

main()

