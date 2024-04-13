from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for qa in question_data:
    q = qa['text']
    a = qa['answer']

    question = Question(q,a)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.final_report()