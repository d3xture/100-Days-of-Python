class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        current_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        choice = input(f"Q.{self.question_number}: {current_question} (True/False)?: ").capitalize()

        if choice == current_answer:
            self.score += 1
            print("You got it right!")
            print(f"Your answer was: {current_answer} ")
            print(f"Your current score is {self.score}/{self.question_number}.")
        elif choice not in current_answer:
            print("Wrong Answer")
            print(f"Your answer was: {current_answer}")
            print(f"Your current score is {self.score}/{self.question_number}.")
        else:
            print("Wrong choice!")



