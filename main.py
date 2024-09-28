from question_model import Question
from data import question_data


question_bank = []


for question in question_data:
    text = question['text']
    answer = question['answer']
    question_model = Question(text, answer)
    question_bank.append(question_model)
    print(question_model.answer)


