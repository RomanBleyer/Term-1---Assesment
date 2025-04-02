import random, time
from typewriter_with_skip import typewriter_input, typewriter_with_skip

from background_functions import quiz_database_initialisation, clear_screen, fancy_clear_screen, title_typewriter, slow_fancy_clear_screen, border_effect, title_screen_typewriter_text, title_screen_glitched, title_screen_very_glitched, title_screen_very_very_glitched
# backround functions is to clean up main file
from colours import coloured_text_formats
from terminaltexteffects.effects import effect_vhstape
from score_keeper import update_highscore, filename

def welcome_to_quiz(): # nothing technical in this func, look to background_functions for cool BTS stuff relating to title stuff
    show_title_screen = False
    clear_screen()
    typewriter_with_skip(str(coloured_text_formats("Typewriter sections can be skipped by pressing space, it will not be counted on your answer\nThis is best played in terminal fullscreen!\n").paragraph_colour()))
    typewriter_with_skip(str(coloured_text_formats("\nMade by Roman with love!\n").border()))

    player_name = typewriter_input(str(coloured_text_formats("What is you name:").paragraph_colour()), end="") or ""
    
    while True:
        typewriter_with_skip(str(coloured_text_formats("\nWould you like to see the title screen? (").paragraph_colour()), end="")
        typewriter_with_skip(str(coloured_text_formats("Y").correct_question_colour()), end="")
        typewriter_with_skip(str(coloured_text_formats("/").paragraph_colour()), end="")
        typewriter_with_skip(str(coloured_text_formats("N").inncorect_question_colour()), end="")
        typewriter_with_skip(str(coloured_text_formats(")").paragraph_colour()), end="")
        user_show_title_screen_selection = typewriter_input(str(coloured_text_formats(": ").paragraph_colour()), end="") or ""
        user_show_title_screen_selection = user_show_title_screen_selection.replace(" ", "").lower() # remove case sensitivity and space so typewriter skip works

        if user_show_title_screen_selection == "y":
            show_title_screen = True
            break
        elif user_show_title_screen_selection == "n":
            show_title_screen = False
            break
        else:
            typewriter_with_skip(str(coloured_text_formats("\nYou need to enter a valid input (Y/N).").inncorect_question_colour()))
            time.sleep(1)
            fancy_clear_screen()

    if show_title_screen == True:
        fancy_clear_screen()

        title_effect = effect_vhstape.VHSTape(title_screen_typewriter_text)
        with title_effect.terminal_output() as terminal:
            clear_screen()
            title_typewriter(str(coloured_text_formats(f"\n \n \n{title_screen_typewriter_text}").option_colours()))
            time.sleep(0.1)
            clear_screen()
            print(str(coloured_text_formats(f"\n \n{title_screen_glitched}").option_colours()))
            time.sleep(0.1)
            clear_screen()
            print(str(coloured_text_formats(f" \n \n \n \n{title_screen_typewriter_text}").option_colours()))
            time.sleep(0.1)
            clear_screen()
            print(str(coloured_text_formats(f" \n \n{title_screen_very_glitched}").option_colours()))
            time.sleep(0.1)
            clear_screen()
            print(str(coloured_text_formats(f"\n{title_screen_very_very_glitched}").option_colours()))
            time.sleep(0.1)
            clear_screen()
            print(str(coloured_text_formats(f"\n \n{title_screen_very_glitched}").option_colours()))
            time.sleep(0.1)
            clear_screen()
            for frame in title_effect:
                terminal.print(frame)
        time.sleep(0.5)
        fancy_clear_screen()
    else:
        pass
    return player_name


def quiz_type_select(selected_categories, quiz_database, total_questions_attempted, total_questions_correct): # For selecting what catagory you will pick
    
    # Some quick variable init
    category_list = quiz_database["category"].unique()
    available_categories = list(set(category_list) - set(selected_categories))

    if len(available_categories) == 0: # if something somewhere fails and it tries to make you select nothing
        fancy_clear_screen()
        quiz_finished()
        return False, None, selected_categories, total_questions_attempted, total_questions_correct

    if total_questions_attempted > 0:
        fancy_clear_screen()
        print("\n \n \n \n")
        title_typewriter(str(coloured_text_formats(f"{border_effect}\n").border().underline()))
        typewriter_with_skip(str(coloured_text_formats("Your score is: (").paragraph_colour()), end="")
        time.sleep(0.25)
        if total_questions_attempted <= total_questions_correct / 2:
            typewriter_with_skip(str(coloured_text_formats(total_questions_correct).inncorect_question_colour()), end="")
        else:
            typewriter_with_skip(str(coloured_text_formats(total_questions_correct).correct_question_colour()), end="")
        
        typewriter_with_skip(str(coloured_text_formats("/").paragraph_colour()), end="")
        typewriter_with_skip(str(coloured_text_formats(total_questions_attempted).option_colours()), end="")
        typewriter_with_skip(str(coloured_text_formats(")").paragraph_colour()), end="")
        print("\n \n")
        user_wants_to_stop_seeing_score = typewriter_input(str(coloured_text_formats("press enter to continue: ").paragraph_colour())).replace(" ", "") # remove space so typewriter skip acually works
        # variable is not used because it is just an input check, allowing you to stay looking at your score
        pass

    if not available_categories:
        return False, None, selected_categories, total_questions_attempted, total_questions_correct 

    while True:
        try:
            fancy_clear_screen()
            print("\n \n \n \n")
            title_typewriter(str(coloured_text_formats(f"{border_effect}\n").border().underline()))

            typewriter_with_skip(str(coloured_text_formats("\nHere is the list of currently avaible topics:").paragraph_colour()))
            time.sleep(0.5)
            counter = 1
            for index, category in enumerate(available_categories, start=counter):
                typewriter_with_skip(str(coloured_text_formats(f"{index}) {category}").option_colours().bold()))
                time.sleep(0.5)

            user_catagory_selection = typewriter_input(str(coloured_text_formats("\nEnter the number of your chosen category: ").option_colours())) or ""
            user_catagory_selection = user_catagory_selection.replace(" ", "")

            if user_catagory_selection.isdigit():
                user_catagory_selection = int(user_catagory_selection)
                if 1 <= user_catagory_selection <= len(available_categories):
                    selected_category = available_categories[user_catagory_selection - 1]
                    filtered_questions = quiz_database[quiz_database["category"] == selected_category]
                    selected_categories.append(selected_category)
                    return True, filtered_questions, selected_categories, total_questions_attempted, total_questions_correct  # Ensure 5 values are returned
                # mother of all input validations
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


def begin_selected_questions(quiz_questions, total_questions_attempted, total_questions_correct): # plays questions from selected catagory, no code outsourcing
    if len(quiz_questions) == 0: # if something somehow breaks and it tries to give you a catagory with no questions 
        clear_screen()
        quiz_finished()
        return quiz_questions, total_questions_attempted, total_questions_correct

    # sorting the questions into variables for use
    random_question_index = random.randint(0, len(quiz_questions) - 1)
    selected_question = quiz_questions.iloc[random_question_index]
    question_options = selected_question['options'].split(', ')

    while True: # this loop is for input validation, the function repeats and resets the variables
        try:
            fancy_clear_screen() 
            print("\n \n \n \n")
            title_typewriter(str(coloured_text_formats(f"{border_effect}\n").border().underline())) # adds border fomat

            typewriter_with_skip(str(coloured_text_formats(f"\n{selected_question['question']}\n").paragraph_colour().bold()))
            for option_index, option in enumerate(question_options, 1):
                typewriter_with_skip(str(coloured_text_formats(f"{option_index}) {option}").option_colours())) # prints questions fomatted and numbered

            user_question_selection = typewriter_input(str(coloured_text_formats("\nEnter your answer: ").option_colours().bold())) or ""
            user_question_selection = user_question_selection.replace(" ", "") # removes spaces from input answer so you can use the typewriter skip function

            correct_answer = str(selected_question['answer']).strip()

            if not user_question_selection.isdigit() or not (1 <= int(user_question_selection) <= len(question_options)): # a slightly more effecient input validation system
                typewriter_with_skip(str(coloured_text_formats(f"\nInvalid input. Please enter a number between 1 and {len(question_options)}.").inncorect_question_colour()))
                time.sleep(1) 
                continue
            
            # this part updates score and tells you if you where right or not
            if user_question_selection.strip() == correct_answer:
                typewriter_with_skip(str(coloured_text_formats("\nCorrect!").correct_question_colour()))
                time.sleep(1)
                total_questions_correct += 1
            else:
                typewriter_with_skip(str(coloured_text_formats("\nIncorrect").inncorect_question_colour()))
                #(f"\nIncorrect. The correct answer was: {correct_answer}").inncorect_question_colour())) could do this but that would make the quiz quite easy to solve on repeat
                time.sleep(1)

            total_questions_attempted += 1
            quiz_questions = quiz_questions.drop(quiz_questions.index[random_question_index]).reset_index(drop=True)
            break

        except ValueError:
            typewriter_with_skip(str(coloured_text_formats(f"\nSomething strange happened. Please enter a number between 1 and {len(question_options)}.").inncorect_question_colour()))
            time.sleep(1)

    return quiz_questions, total_questions_attempted, total_questions_correct


def quiz_finished(total_questions_attempted, total_questions_correct, player_name):
    slow_fancy_clear_screen()
    print("\n \n \n \n")
    title_typewriter(str(coloured_text_formats(f"{border_effect}\n").border().underline())) # adds border fomat
    typewriter_with_skip(str(coloured_text_formats("\n \n \nCongradulations on finishing the quiz!").paragraph_colour()))

    typewriter_with_skip(str(coloured_text_formats("Your score is: (").paragraph_colour()), end="")
    time.sleep(0.25)
    if total_questions_attempted <= total_questions_correct / 2:
        typewriter_with_skip(str(coloured_text_formats(total_questions_correct).inncorect_question_colour()), end="")
    else:
        typewriter_with_skip(str(coloured_text_formats(total_questions_correct).correct_question_colour()), end="")
    
    typewriter_with_skip(str(coloured_text_formats("/").paragraph_colour()), end="")
    typewriter_with_skip(str(coloured_text_formats(total_questions_attempted).option_colours()), end="")
    typewriter_with_skip(str(coloured_text_formats(")").paragraph_colour()), end="")
    print("\n \n")
    typewriter_with_skip(str(coloured_text_formats("Saving your score right now.").paragraph_colour()))
    update_highscore(filename, player_name, total_questions_correct, total_questions_attempted)

    user_wants_to_restart_quiz = typewriter_input(str(coloured_text_formats("If you want to restart this quiz, press any button or just simply close it!").paragraph_colour())).replace(" ", "") # remove space so typewriter skip acually works
    #just adds a input buffer so you can remain on score screen forever
    main()

def main():
    try:
        quiz_database = quiz_database_initialisation()

        if quiz_database is None or quiz_database.empty: # redundency to stop unexpected things
            raise ValueError("Quiz database failed to load or is empty.")

        welcome_to_quiz()

        # score and catagories
        selected_categories = []
        total_questions_attempted = 0
        total_questions_correct = 0

        # Main loop for selecting quiz types and answering questions
        while True:
            # update and reset variables
            quiz_type_selected, quiz_questions, selected_categories, total_questions_attempted, total_questions_correct = quiz_type_select(
                selected_categories, quiz_database, total_questions_attempted, total_questions_correct
            )

            # Exit the loop if no quiz type is selected (e.g., no categories left)
            if not quiz_type_selected:
                break

            # Loop through the questions in the selected category
            while len(quiz_questions) > 0:
                # update and reset variables
                quiz_questions, total_questions_attempted, total_questions_correct = begin_selected_questions(
                    quiz_questions, total_questions_attempted, total_questions_correct
                )
            
        quiz_finished()

    # Handle specific errors related to missing keys in the quiz data
    except KeyError as e:
        typewriter_with_skip(f"Error: Missing expected key in quiz data - {e}")
    # Handle value-related errors (e.g., invalid input or empty database)
    except ValueError as e:
        typewriter_with_skip(f"Value Error: {e}")
    # Handle any other unexpected errors
    except Exception as e:
        typewriter_with_skip(f"An unexpected error occurred: {e}")


# Start the program
main()