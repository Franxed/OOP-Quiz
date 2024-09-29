class QuizBrain:
    """
    The QuizBrain class manages the quiz logic, including asking questions,
    checking answers, and keeping track of the score.
    """

    def __init__(self, question_list):
        """
        Initializes the QuizBrain instance with a list of questions.

        Args:
            question_list (list): A list of Question objects.
        """
        self.question_number = 0  # Tracks the current question number
        self.question_list = question_list  # Stores the list of Question objects
        self.score = 0  # Initializes the user's score to zero

    def still_has_question(self):
        """
        Checks if there are more questions left in the quiz.

        Returns:
            bool: True if there are remaining questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Presents the next question to the user and processes the answer.

        Returns:
            bool: True if a question was asked, False if the quiz is completed.
        """
        if self.question_number < len(self.question_list):
            current_question = self.question_list[self.question_number]  # Retrieves the current Question object
            self.question_number += 1  # Moves to the next question number

            # Prompts the user for an answer to the current question
            user_answer = input(f"Q.{self.question_number} : {current_question.text} (True/False): ").strip()

            # Checks if the user's answer is correct
            self.check_answer(user_answer, current_question)
            return True  # Indicates that a question was asked and processed
        else:
            # If no more questions are left, print the final score
            print(f"Quiz completed!\n{self.score}/{len(self.question_list)}")
            return False  # Indicates that the quiz has ended

    def check_answer(self, user_answer, current_question):
        """
        Compares the user's answer to the correct answer and updates the score.

        Args:
            user_answer (str): The answer provided by the user.
            current_question (Question): The current Question object being answered.
        """
        # Converts both answers to lowercase to make the comparison case-insensitive
        if user_answer.lower() == current_question.answer.lower():
            self.score += 1  # Increments the score if the answer is correct
            print("Correct!")
        else:
            # Informs the user of the correct answer if their answer was wrong
            print(f"Wrong! The correct answer is {current_question.answer}")

        # Displays the current score after each question
        print(f"Score remains : {self.score}/{len(self.question_list)}")
