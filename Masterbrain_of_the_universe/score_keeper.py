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

# Function to get the top 5 high scores
def get_top_highscores(filename, top_n=5):
    highscores = load_highscores(filename)
    
    # Parse and sort highscores by total_questions_correct in descending order
    sorted_highscores = sorted(
        highscores.items(),
        key=lambda x: int(x[1].split('/')[0]),  # Extract total_questions_correct
        reverse=True
    )
    
    # Get the top N entries
    top_highscores = sorted_highscores[:top_n]
    
    # Print the top scores
    print(f"\nTop {top_n} High Scores:")
    for rank, (name, score) in enumerate(top_highscores, start=1):
        print(f"{rank}. {name} - {score}")
