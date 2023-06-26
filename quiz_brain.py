class QuizBrain:
    def __init__(self, qlist):
        self.question_number = 0
        self.question_list = qlist
        self.score = 0

    def is_still_has_question(self):
        lens = len(self.question_list)
        qnos = self.question_number
        if lens == qnos:
            return True
        else:
            return False

    def answer_check(self,current,user):
        if current.lower()==user.lower():
            self.score+=1
            print("you got the correct answer")
            print(f"your current score {self.score}/{self.question_number}")
        else:
            print("Wrong Answer")
            print(f"Correct answers is : {current}")
            print(f"your current score {self.score}/{self.question_number}")
    def next_question(self):
        current_question = self.question_list[self.question_number].question
        current_answer = self.question_list[self.question_number].correct_answer
        self.question_number += 1
        user_answer = input(f"\nQ{self.question_number} :{current_question} : True/False :")
        self.answer_check(current_answer,user_answer)

    def print_report(self):
        print("\nYou have completed the Quiz")
        print(f"Your final score was :{self.score}/{self.question_number}")

