
import random
import time

from typewriter_with_skip import typewriter_input, typewriter_with_skip

from background_functions import quiz_database_initialisation, syntax_error, fancy_clear_screen, clear_screen

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from terminaltexteffects.effects import effect_beams # terminal fancy title screen
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from colours import coloured_text_formats
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def welcome_to_quiz():
    clear_screen()
    time.sleep(0.5)
    typewriter_with_skip(coloured_text_formats("You can skip typewriter sequences by pressing space, it will not be counted on your answer\n").green().apply())
    name = typewriter_input(coloured_text_formats("What is your name? ").blue().apply()).replace(" ", "")
    typewriter_with_skip(coloured_text_formats(f"Welcome to the quiz, {name}!").yellow().bold().apply())  # Greets the user
    time.sleep(0.5)
    effect = effect_beams.Beams("        :::   :::       :::      :::::::: ::::::::::: :::::::::: :::::::::  :::::::::  :::::::::      :::     ::::::::::: ::::    :::    \n      :+:+: :+:+:    :+: :+:   :+:    :+:    :+:     :+:        :+:    :+: :+:    :+: :+:    :+:   :+: :+:       :+:     :+:+:   :+:     \n    +:+ +:+:+ +:+  +:+   +:+  +:+           +:+     +:+        +:+    +:+ +:+    +:+ +:+    +:+  +:+   +:+      +:+     :+:+:+  +:+      \n   +#+  +:+  +#+ +#++:++#++: +#++:++#++    +#+     +#++:++#   +#++:++#:  +#++:++#+  +#++:++#:  +#++:++#++:     +#+     +#+ +:+ +#+       \n  +#+       +#+ +#+     +#+        +#+    +#+     +#+        +#+    +#+ +#+    +#+ +#+    +#+ +#+     +#+     +#+     +#+  +#+#+#        \n #+#       #+# #+#     #+# #+#    #+#    #+#     #+#        #+#    #+# #+#    #+# #+#    #+# #+#     #+#     #+#     #+#   #+#+#         \n###       ### ###     ###  ########     ###     ########## ###    ### #########  ###    ### ###     ### ########### ###    ####          \n      ::::::::  ::::::::::      ::::::::::: :::    ::: ::::::::::                                                                        \n    :+:    :+: :+:                 :+:     :+:    :+: :+:                                                                                \n   +:+    +:+ +:+                 +:+     +:+    +:+ +:+                                                                                 \n  +#+    +:+ :#::+::#            +#+     +#++:++#++ +#++:++#                                                                             \n +#+    +#+ +#+                 +#+     +#+    +#+ +#+                                                                                   \n#+#    #+# #+#                 #+#     #+#    #+# #+#                                                                                    \n########  ###                 ###     ###    ### ##########                                                                              \n     :::    ::: ::::    ::: ::::::::::: :::     ::: :::::::::: :::::::::   ::::::::  ::::::::::                                          \n    :+:    :+: :+:+:   :+:     :+:     :+:     :+: :+:        :+:    :+: :+:    :+: :+:                                                  \n   +:+    +:+ :+:+:+  +:+     +:+     +:+     +:+ +:+        +:+    +:+ +:+        +:+                                                   \n  +#+    +:+ +#+ +:+ +#+     +#+     +#+     +:+ +#++:++#   +#++:++#:  +#++:++#++ +#++:++#                                               \n +#+    +#+ +#+  +#+#+#     +#+      +#+   +#+  +#+        +#+    +#+        +#+ +#+                                                     \n#+#    #+# #+#   #+#+#     #+#       #+#+#+#   #+#        #+#    #+# #+#    #+# #+#                                                      \n########  ###    #### ###########     ###     ########## ###    ###  ########  ##########                                                ")
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)
    time.sleep(100)
    fancy_clear_screen()


def quiz_type_select(selected_categories, quiz_questions_database, total_questions_attempted, total_questions_correct):
    # Print the score if the variables are not zero
    if total_questions_attempted > 0:
        typewriter_with_skip(coloured_text_formats(f"Your score is {total_questions_correct}/{total_questions_attempted}").cyan().apply())

    counter = 1
    categories = quiz_questions_database["category"].unique()

    available_categories = list(set(categories) - set(selected_categories))  # Remove already selected categories

    if not available_categories:
        return False, None, selected_categories, total_questions_attempted, total_questions_correct

    while True:
        try:
            # Print available categories
            typewriter_with_skip(coloured_text_formats("Choose your quiz topic:").bold().apply())
            for i, category in enumerate(available_categories, start=counter):
                typewriter_with_skip(coloured_text_formats(f"{i}) {category}").green().apply())  # Print categories with nice formatting

            current_user_input = typewriter_input(coloured_text_formats("Enter the number of your chosen category: ").blue().apply()).replace(" ", "")  # Remove spaces from input
            if current_user_input.isdigit():  # Ensure the input is a valid number
                current_user_input = int(current_user_input)  # Convert to integer
                if 1 <= current_user_input <= len(available_categories):
                    quiz_category = available_categories[current_user_input - 1]  # Get the selected category
                    quiz_questions = quiz_questions_database[quiz_questions_database["category"] == quiz_category]  # Filter questions by category
                    selected_categories.append(quiz_category)  # Add the selected category to the list
                    return True, quiz_questions, selected_categories, total_questions_attempted, total_questions_correct
                else:
                    syntax_error()
            else:
                syntax_error()
        except ValueError:
            syntax_error()


def begin_selected_questions(quiz_questions, total_questions_attempted, total_questions_correct):
    if len(quiz_questions) == 0:
        # Print a message when no questions are left in the category
        typewriter_with_skip(coloured_text_formats("No more questions available in this category.").red().apply())
        return quiz_questions, total_questions_attempted, total_questions_correct

    # Select a random question from the selected category
    random_index = random.randint(0, len(quiz_questions) - 1)
    first_question = quiz_questions.iloc[random_index]

    # Split the options string into a list
    question_options = first_question['options'].split(', ')

    # Print the question and options
    typewriter_with_skip(coloured_text_formats(f"{first_question['question']}").bold().apply())
    for i, option in enumerate(question_options, 1):
        typewriter_with_skip(coloured_text_formats(f"{i}) {option}").yellow().apply())

    current_user_input = typewriter_input(coloured_text_formats("Enter your answer: ").blue().apply()).replace(" ", "")

    # Get the correct answer
    current_correct_answer = str(first_question['answer']).strip()

    while True:  # Ensure the user inputs a valid answer
        if not current_user_input.isdigit() or not (1 <= int(current_user_input) <= len(question_options)):
            typewriter_with_skip(coloured_text_formats(f"Invalid input. Please enter a number between 1 and {len(question_options)}.").red().apply())

            # Reprint the question and options if input is invalid
            typewriter_with_skip(coloured_text_formats(f"{first_question['question']}").bold().apply())
            for i, option in enumerate(question_options, 1):
                typewriter_with_skip(coloured_text_formats(f"{i}) {option}").yellow().apply())

            current_user_input = typewriter_input(coloured_text_formats("Enter your answer: ").blue().apply())
        else:
            break

    # Print whether the user's answer is correct or incorrect
    if current_user_input.strip() == current_correct_answer:
        typewriter_with_skip(coloured_text_formats("Correct!").green().bold().apply())
        total_questions_correct += 1
    else:
        typewriter_with_skip(coloured_text_formats(f"Incorrect! The correct answer was: {current_correct_answer}").red().apply())

    total_questions_attempted += 1

    # Remove the question from the DataFrame
    quiz_questions = quiz_questions.drop(quiz_questions.index[random_index]).reset_index(drop=True)

    return quiz_questions, total_questions_attempted, total_questions_correct


def finish_quiz():
    # Print a message when the quiz is completed
    typewriter_with_skip(coloured_text_formats("You have completed all categories. Well done!").green().bold().apply())


def main():  # Mainline for the program
    try:
        quiz_questions_database = quiz_database_initialisation()

        welcome_to_quiz()  # Displays the welcome screen

        selected_categories = []  # List to keep track of selected categories
        total_questions_attempted = 0
        total_questions_correct = 0

        while True:
            quiz_type_selected, quiz_questions, selected_categories, total_questions_attempted, total_questions_correct = quiz_type_select(
                selected_categories, quiz_questions_database, total_questions_attempted, total_questions_correct
            )

            if not quiz_type_selected:  # Prompts the user to select a quiz type
                break

            while len(quiz_questions) > 0:  # Continue asking questions until there are no more questions left
                quiz_questions, total_questions_attempted, total_questions_correct = begin_selected_questions(
                    quiz_questions, total_questions_attempted, total_questions_correct
                )

        finish_quiz()  # Call finish_quiz after all categories are exhausted

    except Exception as error_location:
        typewriter_with_skip(coloured_text_formats(f"An error occurred: {error_location}").red().apply())
        main()


main()  # Commence