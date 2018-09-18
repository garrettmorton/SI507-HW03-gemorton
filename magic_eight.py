import random

def get_question():
	question = input("What is your question?")
    question_str = str(question)
    return(question_str)

def check_question(question):
    question_str = str(question)
    if question_str[-1] != "?":
        print("I'm sorry, I can only answer questions!")
        return False
    else:
        return True

answer_list = ["It is certain", "It is decidedly so.", "Without a doubt.", "Yes - definitely.",
"You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
"Reply hazy, try again","Ask again later.", "Better not tell you now.", "Cannot predict now.",
"Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no", "Outlook not so good.", "Very doubtful" ]

answer = answer_list[random.randrange(20)]
print(answer)

question = 0

while question != "quit":
    question = get_question()

