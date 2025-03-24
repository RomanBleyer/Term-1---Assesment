import os
import sys
import time

# Vile mac compatabillity shenannagins
if os.name == 'nt':  # Windows
    import msvcrt
    def key_pressed():
        return msvcrt.kbhit()
else:  # Mac/Linux
    import select
    import termios
    import tty
    def key_pressed():
        dr, dw, de = select.select([sys.stdin], [], [], 0)
        return dr != []


def typewriter_with_skip(text, speed=0.05):
    """Typewriter effect with an option to skip when a key is pressed."""
    
    # Enable non-blocking key detection on Mac/Linux
    if os.name != 'nt':
        old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())

    try:
        for i, char in enumerate(text):
            if key_pressed():  # Skip effect if a key is pressed
                sys.stdout.write(text[i:])  # Print remaining text instantly
                sys.stdout.flush()
                break
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        print()
    finally:
        # Restore terminal settings on Mac/Linux
        if os.name != 'nt':
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

# Cross-platform keypress detection
if os.name == 'nt':  # Windows
    import msvcrt
    def key_pressed():
        return msvcrt.kbhit()
else:  # Mac/Linux
    import select
    import termios
    import tty
    def key_pressed():
        dr, _, _ = select.select([sys.stdin], [], [], 0)
        return dr != []

def typewriter_input(prompt, speed=0.05):
    """Displays the prompt with a typewriter effect, allowing user to skip."""
    
    # Enable non-blocking key detection for Mac/Linux
    if os.name != 'nt':
        old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())

    try:
        for i, char in enumerate(prompt):
            if key_pressed():  # Skip effect if a key is pressed
                sys.stdout.write(prompt[i:])  # Print the remaining text instantly
                sys.stdout.flush()
                break
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
    finally:
        # Restore terminal settings on Mac/Linux
        if os.name != 'nt':
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

    return input()  # Capture user input after the prompt