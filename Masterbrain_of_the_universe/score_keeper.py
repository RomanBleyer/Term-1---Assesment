import os

filename = 'highscores.txt'  # File name set to 'highscores.txt'

# Function to load existing high scores
def load_highscores(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            highscores = {}
            for line in file:
                name, score = line.strip().split(' : ')
                highscores[name] = score
            return highscores
    return {}

# Function to save high scores to a file
def save_highscores(filename, highscores):
    with open(filename, 'w') as file:
        for name, score in highscores.items():
            file.write(f"{name} : {score}\n")

# Function to calculate and save the score
def update_highscore(filename, player_name, total_questions_correct, total_questions_attempted):
    score = f"{total_questions_correct}/{total_questions_attempted}"
    highscores = load_highscores(filename)
    
    # Update or add new score
    highscores[player_name] = score
    save_highscores(filename, highscores)
