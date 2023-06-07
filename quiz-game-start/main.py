from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
# question_bank = [Question(ques_dict['text'],ques_dict['answer']) for ques_dict in question_data]

question_bank = []
for ques_dict in question_data:
    question_text = ques_dict['text']
    question_answer = ques_dict['answer']
    question = Question(question_text, question_answer)
    question_bank.append(question)
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print(f"You have completed the challenge.\nYour final score is {quiz.score}/{quiz.question_number}.")
