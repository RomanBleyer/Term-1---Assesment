import pandas
import os
import random
import time


def variable_initualisation():
    # Perform all global variables here
    global quiz_questions_database
    #
    # Begin variable initialisation
    quiz_questions_database = pandas.read_csv('quiz_questions.csv') # Reads the CSV file into a DataFrame

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') 

def fancy_clear_screen():
    print("\n" * 100)
    os.system('cls' if os.name == 'nt' else 'clear') 

def syntax_error():
    print("Your a fool fong stop trying to break my stuff... Or you just cant spell properly") # Prints a syntax error message
    time.sleep(1)
    clear_screen() # Clears the screen

def loading_screen():
    pass # Placeholder for loading screen functionality

def welcome_to_quiz():
    pass # Placeholder for welcome screen functionality

def quiz_type_select(selected_categories):

    counter = 1
    categories = quiz_questions_database["category"].unique()

    available_categories = list(set(categories) - set(selected_categories)) # remove unselected catagories
    
    if not available_categories:
        return False

    global quiz_questions
    while True:
        try: 
            print("Choose your quiz topic:")
            for i, category in enumerate(available_categories, start=counter):
                print(f"{i}) {category}")  # Prints categories with nice formatting      
            current_user_input = int(input("Enter the number of your chosen category: ")) # Prompts the user to choose a category
            if 1 <= current_user_input <= len(available_categories):
                quiz_category = available_categories[current_user_input - 1] # Gets the selected category
                quiz_questions = quiz_questions_database[quiz_questions_database["category"] == quiz_category] # Filters questions by category
                selected_categories.append(quiz_category) # Add the selected category to the list
                break
            else:
                syntax_error()
        except ValueError:
            syntax_error()
    return True

def begin_selected_questions():
    global quiz_questions
    if len(quiz_questions) == 0:
        print("No more questions available in this category.")
        return

    # Select a random question from the selected category
    random_index = random.randint(0, len(quiz_questions) - 1)
    first_question = quiz_questions.iloc[random_index]
    
    # Split the options string into a list
    question_options = first_question['options'].split(', ')
    
    print(f"{first_question['question']}") # This prints a question
    for i, option in enumerate(question_options, 1):
        print(f"{i}) {option}")    
    current_user_input = input("Enter your answer: ")


    # Get the correct answer
    current_correct_answer = str(first_question['answer']) # Convert the correct answer to a string
    
    while True: # Makes sure the user inputs a valid answer
        if not current_user_input.isdigit() or not (1 <= int(current_user_input) <= len(question_options)):
            print(f"Invalid input. Please enter a number between 1 and {len(question_options)}.")
        
            print(f"{first_question['question']}") # if you a big poo poo head and get it wrong reprints the question
            for i, option in enumerate(question_options, 1):
                print(f"{i}) {option}")
            current_user_input = input("Enter your answer: ")

        else:
            break

    # check to see if their answer is correct after checking that it is valid
    if question_options[int(current_user_input) - 1].strip().lower() == current_correct_answer.strip().lower():
        print("Correct!")
    else:
        print(f"Incorrect! The correct answer was: {current_correct_answer}")
    
    # question from the DataFrame
    quiz_questions = quiz_questions.drop(quiz_questions.index[random_index]).reset_index(drop=True)

def finish_quiz():
    print("You have completed all categories. Well done!")


def main(): # Mainline for the program
    try:
        variable_initualisation() # Initializes variables
        loading_screen() # Displays the loading screen
        welcome_to_quiz() # Displays the welcome screen
        selected_categories = [] # List to keep track of selected categories
        while True:
            if not quiz_type_select(selected_categories): # Prompts the user to select a quiz type
                break
            while len(quiz_questions) > 0: # Continue asking questions until there are no more questions left
                begin_selected_questions() # Begins the quiz with the selected questions
        finish_quiz() # Call finish_quiz after all categories are exhausted
    except Exception as error_location: # telling the game to catch errors and programm should restart accordingly
        print(f"An error occurred: {error_location}")
        main()

main() # Commence