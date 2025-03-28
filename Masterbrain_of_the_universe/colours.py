class coloured_text_formats:
    def __init__(self, text):
        self.text = text
        self.styles = []  # Store ANSI codes for multiple styles

    def green(self):
        self.styles.append("\033[92m")  # Green text
        return self

    def red(self):
        self.styles.append("\033[91m")  # Red text
        return self

    def yellow(self):
        self.styles.append("\033[93m")  # Yellow text
        return self

    def blue(self):
        self.styles.append("\033[94m")  # Blue text
        return self

    def bold(self):
        self.styles.append("\033[1m")  # Bold text
        return self

    def underline(self):
        self.styles.append("\033[4m")  # Underlined text
        return self

    def italic(self):
        self.styles.append("\033[3m")  # Italic text
        return self

    def apply(self):
        # Combine all styles and apply them to the text
        return f"{''.join(self.styles)}{self.text}\033[0m"

#print(coloured_text_formats("This is green and bold text").green().bold().apply())
#print(coloured_text_formats("This is red, italic, and underlined text").red().italic().underline().apply())
#print(coloured_text_formats("This is blue text with underline").blue().underline().apply())