import pandas as pd

# Load the CSV file
df = pd.read_csv('quiz_questions.csv', encoding='utf-8')

# Drop empty columns
df = df.dropna(how='all', axis=1)

# Save the cleaned CSV
df.to_csv('cleaned_quiz_questions.csv', index=False)