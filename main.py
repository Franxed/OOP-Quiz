# main.py

# Import the necessary classes from other modules
from question_model import Question  # Imports the Question class from question_model.py
from data import question_data        # Imports the list of question dictionaries from data.py
from quiz_brain import QuizBrain      # Imports the QuizBrain class from quiz_brain.py

# Initialize an empty list to store Question objects
question_bank = []

# Loop through each question dictionary in question_data
for question in question_data:
    text = question['text']      # Extracts the question text
    answer = question['answer']  # Extracts the correct answer
    question_model = Question(text, answer)  # Creates a Question object with the text and answer
    question_bank.append(question_model)      # Adds the Question object to the question_bank list

# Create an instance of QuizBrain, passing in the list of Question objects
quiz_brain = QuizBrain(question_bank)

# Loop through all the questions in the quiz
while quiz_brain.still_has_question():
    quiz_brain.next_question()  # Asks the next question to the user
