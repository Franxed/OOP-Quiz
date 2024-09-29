from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []


for question in question_data:
    text = question['text']
    answer = question['answer']
    question_model = Question(text, answer)
    question_bank.append(question_model)

quiz_brain = QuizBrain(question_bank)

quiz_brain.next_question()

