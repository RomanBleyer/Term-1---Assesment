import pandas
import os
import random
import time

from typewriter_with_skip import typewriter_input
from typewriter_with_skip import typewriter_with_skip

from background_functions import quiz_database_initialisation, clear_screen, fancy_clear_screen, title_typewriter, slow_fancy_clear_screen, border_effect, title_screen_typewriter_text, title_screen_glitched, title_screen_very_glitched, title_screen_very_very_glitched
from colours import coloured_text_formats
from terminaltexteffects.effects import effect_vhstape


def welcome_to_quiz():
    show_title_screen = False

    while True:
        clear_screen()

        typewriter_with_skip(str(coloured_text_formats("Typewriter sections can be skipped by pressing space, it will not be counted on your answer").paragraph_colour()))
        typewriter_with_skip(str(coloured_text_formats("This is best played in terminal fullscreen!\n").paragraph_colour()))

        typewriter_with_skip(str(coloured_text_formats("\nMade by Roman with love!\n").border()))
        typewriter_with_skip(str(coloured_text_formats("Would you like to see the title screen? (").paragraph_colour()), end="")
        time.sleep(0.25)
        typewriter_with_skip(str(coloured_text_formats("Y").correct_question_colour()), end="")
        typewriter_with_skip(str(coloured_text_formats("/").paragraph_colour()), end="")
        typewriter_with_skip(str(coloured_text_formats("N").inncorect_question_colour()), end="")
        typewriter_with_skip(str(coloured_text_formats(")").paragraph_colour()), end="")

        user_choice_one = typewriter_input(str(coloured_text_formats(": ").paragraph_colour()), end="") or ""
        user_choice_one = user_choice_one.replace(" ", "").lower()
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
            time.sleep(0.15)
            clear_screen()
            print(str(coloured_text_formats(f"\n \n{title_screen_glitched}").option_colours()))
            time.sleep(0.15)
            clear_screen()
            print(str(coloured_text_formats(f" \n \n \n \n{title_screen_typewriter_text}").option_colours()))
            time.sleep(0.15)
            clear_screen()
            print(str(coloured_text_formats(f" \n \n{title_screen_very_glitched}").option_colours()))
            time.sleep(0.15)
            clear_screen()
            print(str(coloured_text_formats(f"\n{title_screen_very_very_glitched}").option_colours()))
            time.sleep(0.15)
            clear_screen()
            print(str(coloured_text_formats(f"\n \n{title_screen_very_glitched}").option_colours()))
            time.sleep(0.15)
            clear_screen()
            for frame in title_effect:
                terminal.print(frame)
        time.sleep(0.5)
        fancy_clear_screen()
    else:
        pass


def quiz_type_select(selected_categories, quiz_database, total_questions_attempted, total_questions_correct):
    category_list = quiz_database["category"].unique()  # Get all unique categories
    available_categories = list(set(category_list) - set(selected_categories))  # Remove already selected categories

    if len(available_categories) == 0:
        typewriter_with_skip(str(coloured_text_formats("Somehow your in the catagory selection menu when it doesnt have any aviable catagories, just gonna send you to finish quiz").inncorect_question_colour()))
        time.sleep(1.5)
        clear_screen()
        finish_quiz()
        return selected_categories, quiz_database, total_questions_attempted, total_questions_correct

    # Print the score if you have actually attempted questions
    if total_questions_attempted > 0:
        fancy_clear_screen()
        print("\n \n \n \n")
        title_typewriter(str(coloured_text_formats(f"{border_effect}\n").border().underline()))
        typewriter_with_skip(str(coloured_text_formats("Your score is: (").paragraph_colour()), end="")
        time.sleep(0.25)
        typewriter_with_skip(str(coloured_text_formats(total_questions_correct).correct_question_colour()), end="")
        typewriter_with_skip(str(coloured_text_formats("/").paragraph_colour()), end="")
        typewriter_with_skip(str(coloured_text_formats(total_questions_attempted).inncorect_question_colour()), end="")
        typewriter_with_skip(str(coloured_text_formats(")").paragraph_colour()), end="")
        print("\n \n")
        user_input = typewriter_input(str(coloured_text_formats("press enter to continue: ").paragraph_colour())).replace(" ", "")
        pass

    if not available_categories:  # If there are no categories, return all variables
        return False, None, selected_categories, total_questions_attempted, total_questions_correct

    while True:
        try:
            fancy_clear_screen()
            print("\n \n \n \n")
            title_typewriter(str(coloured_text_formats(f"{border_effect}\n").border().underline()))

            typewriter_with_skip(str(coloured_text_formats("\nChoose your quiz topic:").paragraph_colour())).replace(" ", "")
            time.sleep(0.5)
            counter = 1
            for index, category in enumerate(available_categories, start=counter):
                typewriter_with_skip(str(coloured_text_formats(f"{index}) {category}").option_colours().bold()))  # Print categories with nice formatting
                time.sleep(0.5)
            user_choice_two = typewriter_input(str(coloured_text_formats("\nEnter the number of your chosen category: ").option_colours())) or ""
            user_choice_two = user_choice_two.replace(" ", "")
            if user_choice_two.isdigit():  # Ensure the input is a valid number
                user_choice_two = int(user_choice_two)
                if 1 <= user_choice_two <= len(available_categories):
                    selected_category = available_categories[user_choice_two - 1]  # Get the selected category
                    filtered_questions = quiz_database[quiz_database["category"] == selected_category]  # Filter questions by category
                    selected_categories.append(selected_category)  # Add the selected category to the list
                    return True, filtered_questions, selected_categories, total_questions_attempted, total_questions_correct
                else:
                    if available_categories != 1:
                        typewriter_with_skip(str(coloured_text_formats(f"\nInvalid input. Please enter a valid number between 1 and {len(available_categories)}.").syntax_error_colour().bold()))
                    else:
                        typewriter_with_skip(str(coloured_text_formats("\nPlease enter the number 1.").syntax_error_colour().bold()))
                    time.sleep(1.5)
                    clear_screen()
            else:
                if available_categories != 1:
                    typewriter_with_skip(str(coloured_text_formats(f"\nInvalid input. Please enter a valid number between 1 and {len(available_categories)}.").syntax_error_colour().bold()))
                else:
                    typewriter_with_skip(str(coloured_text_formats("\nPlease enter the number 1.").syntax_error_colour().bold()))
                time.sleep(1.5)
                clear_screen()
        except ValueError:
            if available_categories != 1:
                typewriter_with_skip(str(coloured_text_formats(f"\nA strange unrecorded error occured, in your input. Please enter a valid number between 1 and {len(available_categories)}.").syntax_error_colour().bold()))
            else:
                typewriter_with_skip(str(coloured_text_formats("\nSomething broke, please enter the number 1.").syntax_error_colour().bold()))
            time.sleep(1.5)
            clear_screen()


def begin_selected_questions(quiz_questions, total_questions_attempted, total_questions_correct):
    if len(quiz_questions) == 0:
        # boots them to finish quiz if they have finished all questions
        clear_screen()
        finish_quiz()
        return quiz_questions, total_questions_attempted, total_questions_correct

    random_question_index = random.randint(0, len(quiz_questions) - 1)  # Select a random question from the selected category
    selected_question = quiz_questions.iloc[random_question_index]
    question_options = selected_question['options'].split(', ')  # Split the options string into a list

    while True:  # Keep asking the same question until valid input is provided
        try:
            fancy_clear_screen()
            print("\n \n \n \n")
            title_typewriter(str(coloured_text_formats(f"{border_effect}\n").border().underline()))
            typewriter_with_skip(str(coloured_text_formats(f"\n{selected_question['question']}\n").paragraph_colour().bold()))
            for option_index, option in enumerate(question_options, 1):
                typewriter_with_skip(str(coloured_text_formats(f"{option_index}) {option}").option_colours()))

            user_answer = typewriter_input(str(coloured_text_formats("\nEnter your answer: ").option_colours().bold())) or ""
            user_answer = user_answer.replace(" ", "")

            # Get the correct answer
            correct_answer = str(selected_question['answer']).strip()

            if not user_answer.isdigit() or not (1 <= int(user_answer) <= len(question_options)):
                typewriter_with_skip(str(coloured_text_formats(f"\nInvalid input. Please enter a number between 1 and {len(question_options)}.").inncorect_question_colour()))
                time.sleep(1)
                continue  # Replay the same question

            # Check if the answer is correct
            if user_answer.strip() == correct_answer:
                typewriter_with_skip(str(coloured_text_formats("\nCorrect!").correct_question_colour()))
                time.sleep(1)
                total_questions_correct += 1
            else:
                typewriter_with_skip(str(coloured_text_formats(f"\nIncorrect. The correct answer was: {correct_answer}").inncorect_question_colour()))
                time.sleep(1)

            # Update the total questions attempted and remove the question from the DataFrame
            total_questions_attempted += 1
            quiz_questions = quiz_questions.drop(quiz_questions.index[random_question_index]).reset_index(drop=True)
            break  # Exit the loop after valid input and processing the question

        except ValueError:
            typewriter_with_skip(str(coloured_text_formats(f"\nSomething strange happened. Please enter a number between 1 and {len(question_options)}.").inncorect_question_colour()))
            time.sleep(1)

    return quiz_questions, total_questions_attempted, total_questions_correct


def finish_quiz():
    # Print a message when the quiz is completed
    typewriter_with_skip("\n \n \nThis is a placeholder, score summmerisation is gonna be here.")


def main():  
    try:
        quiz_database = quiz_database_initialisation()

        if quiz_database is None or quiz_database.empty:
            raise ValueError("Quiz database failed to load or is empty.")

        welcome_to_quiz()

        selected_categories = []
        total_questions_attempted = 0
        total_questions_correct = 0

        while True:
            quiz_type_selected, quiz_questions, selected_categories, total_questions_attempted, total_questions_correct = quiz_type_select(
                selected_categories, quiz_database, total_questions_attempted, total_questions_correct
            )

            if not quiz_type_selected:
                break

            while len(quiz_questions) > 0:
                quiz_questions, total_questions_attempted, total_questions_correct = begin_selected_questions(
                    quiz_questions, total_questions_attempted, total_questions_correct
                )

        finish_quiz()

    except KeyError as e:
        typewriter_with_skip(f"Error: Missing expected key in quiz data - {e}")
    except ValueError as e:
        typewriter_with_skip(f"Value Error: {e}")
    except Exception as e:
        typewriter_with_skip(f"An unexpected error occurred: {e}")



main()