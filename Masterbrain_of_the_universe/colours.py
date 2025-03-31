import random

class coloured_text_formats:
    def __init__(self, text):
        self.text = text
        self.styles = []  # Store ANSI codes for styles

    def __str__(self):
        # Automatically apply styles and return the formatted text
        return f"{''.join(self.styles)}{self.text}\033[0m"

    # Apply paragraph colors with weighted randomness
    def paragraph_colour(self):
        colors = [
            "\033[38;5;189m",  # Light purple
            "\033[38;5;224m",  # Light yellow
            "\033[38;5;188m",  # Light green
            "\033[38;5;152m",  # Light cyan
            "\033[38;5;231m"   # White (more common)
        ]
        weights = [1, 1, 1, 1, 10]  # White is more common
        self.text = ''.join(f"{random.choices(colors, weights)[0]}{char}" for char in self.text) + "\033[0m"
        return self

    # Apply incorrect question color
    def inncorect_question_colour(self):
        self.styles.append("\033[38;5;197m")  # Bright pink
        return self

    # Apply syntax error color
    def syntax_error_colour(self):
        self.styles.append("\033[38;5;197m")  # Bright pink
        return self

    # Apply correct question color
    def correct_question_colour(self):
        self.styles.append("\033[38;5;78m")  # Bright green
        return self

    # Apply random option colors
    def option_colours(self):
        colors = ["\033[38;5;117m", "\033[38;5;110m", "\033[38;5;146m"]  # Option colors
        self.text = ''.join(f"{random.choice(colors)}{char}" for char in self.text) + "\033[0m"
        return self

    # Apply bold style
    def bold(self):
        self.styles.append("\033[1m")
        return self

    # Apply underline style
    def underline(self):
        self.styles.append("\033[4m")
        return self

    # Apply italic style
    def italic(self):
        self.styles.append("\033[3m")
        return self

    # Apply border effect with cycling colors
    def border(self):
        colors = [
            "\033[38;5;5m", "\033[38;5;13m", "\033[38;5;17m", "\033[38;5;18m", "\033[38;5;19m",
            "\033[38;5;25m", "\033[38;5;26m", "\033[38;5;31m", "\033[38;5;53m", "\033[38;5;54m",
            "\033[38;5;55m", "\033[38;5;56m", "\033[38;5;57m", "\033[38;5;61m", "\033[38;5;62m",
            "\033[38;5;75m", "\033[38;5;89m", "\033[38;5;90m", "\033[38;5;91m", "\033[38;5;92m",
            "\033[38;5;93m", "\033[38;5;97m", "\033[38;5;98m", "\033[38;5;99m", "\033[38;5;104m",
            "\033[38;5;105m", "\033[38;5;110m", "\033[38;5;111m", "\033[38;5;125m", "\033[38;5;126m",
            "\033[38;5;127m", "\033[38;5;128m", "\033[38;5;129m", "\033[38;5;133m", "\033[38;5;134m",
            "\033[38;5;135m", "\033[38;5;140m", "\033[38;5;141m", "\033[38;5;162m", "\033[38;5;163m",
            "\033[38;5;164m", "\033[38;5;165m", "\033[38;5;169m", "\033[38;5;170m", "\033[38;5;171m",
        ]
        self.text = ''.join(f"{colors[i % len(colors)]}{char}" for i, char in enumerate(self.text)) + "\033[0m"
        return self


# Example usage
print("border effect below")
print(coloured_text_formats("\n").border().underline())
print(coloured_text_formats("This is paragraph text colouring\n").paragraph_colour())
print(coloured_text_formats("Options colour series\n").option_colours())
print(coloured_text_formats("You got this answer wrong!").inncorect_question_colour())
print(coloured_text_formats("You got this answer right!\n").correct_question_colour())
print(coloured_text_formats("This was formatted incorrectly!").syntax_error_colour().bold())




