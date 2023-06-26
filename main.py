from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for qus in question_data:
    question=qus["question"]
    answer=qus["correct_answer"]
    new_question=Question(q_text=question,q_answer=answer)
    question_bank.append(new_question)

quizs= QuizBrain(question_bank)
while quizs.is_still_has_question()!=True:
    quizs.next_question()
quizs.print_report()
