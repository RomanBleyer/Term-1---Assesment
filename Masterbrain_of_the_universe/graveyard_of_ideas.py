'''
import json
import random
import time

with open('quiz_questions.json', 'r') as file:
    questions = json.load(file)


def welcome():
    pass # add title screen and credits here
def main():
    welcome()
    quiz()  
def quiz():
    asked_questions = set()
    correct_answers = 0
    
    while len(asked_questions) < len(questions):
        que
    else:stion = random.choice(questions)
        if question['question'] not in asked_questions:
            asked_questions.add(question['question'])
            print(f"Question: {question['question']}")
            for i, option in enumerate(question['options']):
                print(f"{i + 1}. {option}")
            answer = input("Your answer (enter the number): ")
            if question['options'][int(answer) - 1] == question['answer']:
                correct_answers += 1
                print("Correct!")
            else:
                print(f"Wrong! The correct answer was: {question['answer']}")
            print()
        print("No more questions available.")

main()'
'''


'''
# Main function to start the quiz
def main():
    welcome()
    quiz()
    print_all_questions_and_answers()

# Function to conduct the quiz

def quiz():
    asked_questions = set()
    correct_answers = 0
    
    while len(asked_questions) < len(questions):
        question = random.choice(questions)
        if question['question'] not in asked_questions:
            asked_questions.add(question['question'])
            print(f"Question: {question['question']}")
            for i, option in enumerate(question['options']):
                print(f"{i + 1}. {option}")
            answer = input("Your answer (enter the number): ")
            if question['options'][int(answer) - 1] == question['answer']:
                correct_answers += 1
                print("Correct!")
            else:
                print(f"Wrong! The correct answer was: {question['answer']}")
            print()
    else:
        print("No more questions available.")

# Start the quiz
main()
'''

import csv

# Function to load questions from a CSV file
def load_questions_from_csv(filepath):
    questions = []
    with open(filepath, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            question = {
                'category': row['category'],
                'question': row['question'],
                'options': row['options'].split('|'),
                'answer': row['answer']
            }
            questions.append(question)
    return questions

# Load questions from the CSV file
questions = load_questions_from_csv('quiz_questions.csv')

# Function to print all questions and answers
def print_all_questions_and_answers():
    for question in questions:
        print(f"Question: {question['question']}, Answer: {question['answer']}")

# Function to print questions by category
def print_questions_by_category(category):
    for question in questions:
        if question['category'] == category:
            print(f"Question: {question['question']}, Answer: {question['answer']}")

# Function to print only questions
def print_only_questions():
    for question in questions:
        print(f"Question: {question['question']}")

# Function to print only answers
def print_only_answers():
    for question in questions:
        print(f"Answer: {question['answer']}")

# Function to print questions and options
def print_questions_and_options():
    for question in questions:
        print(f"Question: {question['question']}")
        options = question['options']
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")

# Function to print questions and answers by category
def print_questions_and_answers_by_category(category):
    for question in questions:
        if question['category'] == category:
            print(f"Question: {question['question']}, Answer: {question['answer']}")


