'''THIS FILE HAS A BUNCH OF RANDOM FUNCTIONS THAT CLUTTER UP SPACE IN THE MAIN PROGRAMM'''

from typewriter_with_skip import typewriter_with_skip
import os, pandas, time, random
from colours import coloured_text_formats
title_screen_typewriter_text = " /##      /##                       /##                         /##                          /##                            /###### \n| ###    /###                      | ##                        | ##                         |__/                           /##__  ##\n| ####  /####  /######   /####### /######    /######   /###### | #######   /######  /######  /## /#######         /###### | ##  \__/\n| ## ##/## ## |____  ## /##_____/|_  ##_/   /##__  ## /##__  ##| ##__  ## /##__  ##|____  ##| ##| ##__  ##       /##__  ##| ####    \n| ##  ###| ##  /#######|  ######   | ##    | ########| ##  \__/| ##  \ ##| ##  \__/ /#######| ##| ##  \ ##      | ##  \ ##| ##_/    \n| ##\  # | ## /##__  ## \____  ##  | ## /##| ##_____/| ##      | ##  | ##| ##      /##__  ##| ##| ##  | ##      | ##  | ##| ##      \n| ## \/  | ##|  ####### /#######/  |  ####/|  #######| ##      | #######/| ##     |  #######| ##| ##  | ##      |  ######/| ##      \n|__/     |__/ \_______/|_______/    \___/   \_______/|__/      |_______/ |__/      \_______/|__/|__/  |__/       \______/ |__/      \n \n \n \n \n   /##     /##                       /##   /##           /##                                                                        \n  | ##    | ##                      | ##  | ##          |__/                                                                        \n /######  | #######   /######       | ##  | ## /#######  /## /##    /## /######   /######   /#######  /######                       \n|_  ##_/  | ##__  ## /##__  ##      | ##  | ##| ##__  ##| ##|  ##  /##//##__  ## /##__  ## /##_____/ /##__  ##                      \n  | ##    | ##  \ ##| ########      | ##  | ##| ##  \ ##| ## \  ##/##/| ########| ##  \__/|  ###### | ########                      \n  | ## /##| ##  | ##| ##_____/      | ##  | ##| ##  | ##| ##  \  ###/ | ##_____/| ##       \____  ##| ##_____/                      \n  |  ####/| ##  | ##|  #######      |  ######/| ##  | ##| ##   \  #/  |  #######| ##       /#######/|  #######                      \n   \___/  |__/  |__/ \_______/       \______/ |__/  |__/|__/    \_/    \_______/|__/      |_______/  \_______/                      "

border_effect = "                                                                                                                                                                     \n"

def title_typewriter(text, delay=0.05):  # Adjust delay as needed
    lines = text.split("\n")
    for line in lines:
        print(line, flush=True)  # Print each line and flush immediately
        time.sleep(delay)

def add_glitch_effect(text, glitch_chance=0.1):
    """Randomly introduces static noise into the text."""
    glitch_chars = ["#", "*", "%", "&", "@", "$"]
    glitched_text = ""
    for char in text:
        if char not in [" ", "\n"] and random.random() < glitch_chance:
            glitched_text += random.choice(glitch_chars)
        else:
            glitched_text += char
    return glitched_text

title_screen_glitched = add_glitch_effect(title_screen_typewriter_text, glitch_chance=0.08)
title_screen_very_glitched = add_glitch_effect(title_screen_typewriter_text, glitch_chance=0.2)
title_screen_very_very_glitched = add_glitch_effect(title_screen_typewriter_text, glitch_chance=0.6)
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

def slow_fancy_clear_screen():
    for i in range(0,30):
        print(" ")
        time.sleep(0.05)
    clear_screen()
