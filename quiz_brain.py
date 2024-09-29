

class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        if self.question_number < len(self.question_list):
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            user_answer = input(f"Q.{self.question_number} : {current_question.text} (True/False): ").strip()
            self.check_answer(user_answer, current_question)
            return True
        else:
            print(f"Quiz completed!\n{self.score}/{len(self.question_list)}")
            return False

    def check_answer(self, user_answer, current_question):
        if user_answer.lower() == current_question.answer.lower():
            self.score += 1
            print("Correct!")

        else:
            print(f"Wrong! The correct answer is {current_question.answer}")
        print(f"Score remains : {self.score}/{len(self.question_list)}")
