from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank= []
for questions in question_data:
	question_text = questions["text"]
	
	question_answer = questions["answer"]
	new_question = Question(text=question_text , answer = question_answer)
	
	question_bank.append(new_question)
quiz = QuizBrain(question_bank)
while quiz.still_question():
	quiz.next_question()
	print("\n")
print("You have completed the quiz")
print(f"Your Final score is {quiz.current_score}/{quiz.question_number}")