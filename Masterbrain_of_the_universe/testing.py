import pandas

quiz_questions_database = pandas.read_csv('quiz_questions.csv') # Reads the CSV file into a DataFrame

counter_1 = 1 # Gets all unique catagories and then prints them with formatting
categories = quiz_questions_database["category"].unique() 
for category in categories:
#    print(f"{counter_1}) {category}") 
    counter_1 += 1



print(quiz_questions_database["category_number"].unique().tolist()) # this prints the list of unqiue catagories