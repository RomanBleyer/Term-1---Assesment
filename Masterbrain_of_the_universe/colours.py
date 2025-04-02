import random
# this is just lets main colour fonts and make it look PRETTY!!!!! 
class coloured_text_formats:
    def __init__(self, text):
        self.text = text
        self.styles = [] 

    def __str__(self):
        return f"{''.join(self.styles)}{self.text}\033[0m"

    def paragraph_colour(self):
        colors = [
            "\033[38;5;189m",  
            "\033[38;5;224m", 
            "\033[38;5;188m",
            "\033[38;5;152m", 
            "\033[38;5;231m"   
        ]
        weights = [1, 1, 1, 1, 10]  
        self.text = ''.join(f"{random.choices(colors, weights)[0]}{char}" for char in self.text) + "\033[0m"
        return self


    def inncorect_question_colour(self):
        self.styles.append("\033[38;5;197m")
        return self

    def syntax_error_colour(self):
        self.styles.append("\033[38;5;197m") 
        return self

    def correct_question_colour(self):
        self.styles.append("\033[38;5;78m")  
        return self

    def option_colours(self):
        colors = ["\033[38;5;117m", "\033[38;5;110m", "\033[38;5;146m"]
        self.text = ''.join(f"{random.choice(colors)}{char}" for char in self.text) + "\033[0m"
        return self

    def bold(self):
        self.styles.append("\033[1m")
        return self

    def underline(self):
        self.styles.append("\033[4m")
        return self

    def italic(self):
        self.styles.append("\033[3m")
        return self

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