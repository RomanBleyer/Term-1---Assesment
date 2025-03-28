import os
import sys
import time

# Cross-platform keypress detection
if os.name == 'nt':  # Windows
    import msvcrt
    def key_pressed():
        if msvcrt.kbhit():
            key = msvcrt.getch()
            return key == b' '  # Check if the pressed key is the spacebar
        return False
else:  # Mac/Linux
    import select
    import termios
    import tty
    def key_pressed():
        dr, _, _ = select.select([sys.stdin], [], [], 0)
        if dr:
            key = sys.stdin.read(1)
            return key == ' '  # Check if the pressed key is the spacebar
        return False


def typewriter_with_skip(text, speed=0.05):
    """Displays text with a typewriter effect, allowing skipping with the spacebar."""
    # Enable non-blocking key detection on Mac/Linux
    if os.name != 'nt':
        old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())

    try:
        for i, char in enumerate(text):
            if key_pressed():  # Skip effect if the spacebar is pressed
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


def typewriter_input(prompt, speed=0.05):
    """Displays the prompt with a typewriter effect, allowing skipping with the spacebar."""
    # Enable non-blocking key detection for Mac/Linux
    if os.name != 'nt':
        old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())

    try:
        for i, char in enumerate(prompt):
            if key_pressed():  # Skip effect if the spacebar is pressed
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