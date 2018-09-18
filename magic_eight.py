import random

def get_question():
	question = input("What is your question?")
        return str(question)

def check_question(question):
    question_str = str(question)
    if question_str[-1] != "?":
        print("I'm sorry, I can only answer questions!")
        return False
    else:
        return True

question = 0

while question != "quit":
    question = get_question()

    
