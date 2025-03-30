def print_colored_escape_codes():
    for i in range(256):
        color_code = f"\033[38;5;{i}m"  # ANSI escape code for color
        reset_code = "\033[0m"
        escape_repr = f"{color_code}\\033[38;5;{i}m{reset_code}"  # Escape sequence in color

        print(escape_repr)  # Print the escape sequence in its corresponding color
        print()  # Extra newline for spacing

print_colored_escape_codes()
