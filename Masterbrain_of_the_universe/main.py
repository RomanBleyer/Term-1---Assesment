import pandas
import os
import random
import time

from typewriter_with_skip import typewriter_input
from typewriter_with_skip import typewriter_with_skip

from background_functions import quiz_database_initialisation, syntax_error, clear_screen, fancy_clear_screen, title_typewriter, border_effect, title_screen_typewriter_text, title_screen_glitched, title_screen_very_glitched, title_screen_very_very_glitched
from colours import coloured_text_formats
from terminaltexteffects.effects import effect_vhstape


def welcome_to_quiz():
    show_title_screen = False

    while True:
        clear_screen()

        typewriter_with_skip(str(coloured_text_formats("This is best played in terminal fullscreen!\n").paragraph_colour()))

        typewriter_with_skip(str(coloured_text_formats("\nMade by Roman with love!").border()))

        typewriter_with_skip(str(coloured_text_formats("Would you like to see the title screen? (").paragraph_colour()), end="")
        time.sleep(0.25)
        typewriter_with_skip(str(coloured_text_formats("Y").correct_question_colour()), end="")
        typewriter_with_skip(str(coloured_text_formats("/").paragraph_colour()), end="")
        typewriter_with_skip(str(coloured_text_formats("N").inncorect_question_colour()), end="")
        typewriter_with_skip(str(coloured_text_formats(")").paragraph_colour()), end="")

        user_choice_one = typewriter_input(str(coloured_text_formats(": ").paragraph_colour()), end="").lower()
        if user_choice_one == "y":
            show_title_screen = True
            break
        elif user_choice_one == "n":
            show_title_screen = False
            break
        else:
            typewriter_with_skip(str(coloured_text_formats("\nYou need to enter a valid input (Y/N).").inncorect_question_colour()))
            time.sleep(1)

    if show_title_screen == True:
        fancy_clear_screen()

        title_effect = effect_vhstape.VHSTape(title_screen_typewriter_text)
        with title_effect.terminal_output() as terminal:
            clear_screen()
            title_typewriter(str(coloured_text_formats(f"\n \n \n{title_screen_typewriter_text}").option_colours()))
            time.sleep(1)
            clear_screen()
            print(str(coloured_text_formats(f"\n \n \n{title_screen_glitched}").option_colours()))
            time.sleep(0.1)
            clear_screen()
            print(str(coloured_text_formats(f" \n \n{title_screen_very_glitched}").option_colours()))
            time.sleep(1)
            clear_screen()
            print(str(coloured_text_formats(f" \n \n{title_screen_very_glitched}").option_colours()))
            time.sleep(0.1)
            clear_screen()
            print(str(coloured_text_formats(f"\n{title_screen_very_very_glitched}").option_colours()))
            time.sleep(1)
            clear_screen()
            print(str(coloured_text_formats(f"\n{title_screen_very_very_glitched}").option_colours()))
            time.sleep(0.1)
            clear_screen()
            for frame in title_effect:
                terminal.print(frame)
        time.sleep(0.5)
        fancy_clear_screen()
    else:
        fancy_clear_screen()


def quiz_type_select(selected_categories, quiz_database, total_questions_attempted, total_questions_correct):
    # Print the score if you have acually attempted questions
    if total_questions_attempted > 0:
        typewriter_with_skip(str(coloured_text_formats("Your score is: (").paragraph_colour()), end="")
        time.sleep(0.25)
        typewriter_with_skip(str(coloured_text_formats(total_questions_correct).correct_question_colour()), end="")
        typewriter_with_skip(str(coloured_text_formats("/").paragraph_colour()), end="")
        typewriter_with_skip(str(coloured_text_formats(total_questions_attempted).inncorect_question_colour()), end="")
        typewriter_with_skip(str(coloured_text_formats(")").paragraph_colour()), end="")

    category_list = quiz_database["category"].unique() # get all unqiue catagories

    available_categories = list(set(category_list) - set(selected_categories))  # Remove already selected categories

    if not available_categories:
        return False, None, selected_categories, total_questions_attempted, total_questions_correct


    while True:
        try:
            # Print available categories
            typewriter_with_skip(str(coloured_text_formats(f"{border_effect}\n").border().underline()))
            typewriter_with_skip("\nChoose your quiz topic:")
            counter = 1
            for index, category in enumerate(available_categories, start=counter):
                typewriter_with_skip(f"{index}) {category}")  # Print categories with nice formatting

            user_choice_two = typewriter_input("Enter the number of your chosen category: ").replace(" ", "")
            if user_choice_two.isdigit():  # Ensure the input is a valid number
                user_choice_two = int(user_choice_two)
                if 1 <= user_choice_two <= len(available_categories):
                    selected_category = available_categories[user_choice_two - 1]  # Get the selected category
                    filtered_questions = quiz_database[quiz_database["category"] == selected_category]  # Filter questions by category
                    selected_categories.append(selected_category)  # Add the selected category to the list
                    return True, filtered_questions, selected_categories, total_questions_attempted, total_questions_correct
                else:
                    syntax_error()
            else:
                syntax_error()
        except ValueError:
            syntax_error()


def begin_selected_questions(quiz_questions, total_questions_attempted, total_questions_correct):
    if len(quiz_questions) == 0:
        typewriter_with_skip(str(coloured_text_formats("No more questions available in this category.")))
        return quiz_questions, total_questions_attempted, total_questions_correct

    # Select a random question from the selected category
    random_question_index = random.randint(0, len(quiz_questions) - 1)
    selected_question = quiz_questions.iloc[random_question_index]

    # Split the options string into a list
    question_options = selected_question['options'].split(', ')

    # Print the question and options
    typewriter_with_skip(str(coloured_text_formats(f"{selected_question['question']}")))
    for option_index, option in enumerate(question_options, 1):
        typewriter_with_skip(str(coloured_text_formats(f"{option_index}) {option}")))

    user_answer = typewriter_input(str(coloured_text_formats("Enter your answer: "))).replace(" ", "")

    # Get the correct answer
    correct_answer = str(selected_question['answer']).strip()

    while True:  # Ensure the user inputs a valid answer
        if not user_answer.isdigit() or not (1 <= int(user_answer) <= len(question_options)):
            typewriter_with_skip(str(coloured_text_formats(f"Invalid input. Please enter a number between 1 and {len(question_options)}.")))
            user_answer = typewriter_input(str(coloured_text_formats("Enter your answer: "))).replace(" ", "")
            continue

        # Print whether the user's answer is correct or incorrect
        if user_answer.strip() == correct_answer:
            typewriter_with_skip(str(coloured_text_formats("Correct!").correct_question_colour()))
            total_questions_correct += 1
        else:
            typewriter_with_skip(str(coloured_text_formats(f"Incorrect! The correct answer was: {correct_answer}").inncorect_question_colour()))

        total_questions_attempted += 1

        # Remove the question from the DataFrame
        quiz_questions = quiz_questions.drop(quiz_questions.index[random_question_index]).reset_index(drop=True)

        return quiz_questions, total_questions_attempted, total_questions_correct


def finish_quiz():
    # Print a message when the quiz is completed
    typewriter_with_skip("You have completed all categories. Well done!")


def main():  # Mainline for the program
    try:
        quiz_database = quiz_database_initialisation()

        welcome_to_quiz()  # Displays the welcome screen

        selected_categories = []  # List to keep track of selected categories
        total_questions_attempted = 0
        total_questions_correct = 0

        while True:
            quiz_type_selected, quiz_questions, selected_categories, total_questions_attempted, total_questions_correct = quiz_type_select(
                selected_categories, quiz_database, total_questions_attempted, total_questions_correct
            )

            if not quiz_type_selected:  # Prompts the user to select a quiz type
                break

            while len(quiz_questions) > 0:  # Continue asking questions until there are no more questions left
                quiz_questions, total_questions_attempted, total_questions_correct = begin_selected_questions(
                    quiz_questions, total_questions_attempted, total_questions_correct
                )

        finish_quiz()  # Call finish_quiz after all categories are exhausted

    except Exception as error_message:
        typewriter_with_skip(f"An error occurred: {error_message}")


main()