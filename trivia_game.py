# Trivia Game
# list of questions
# store answers
# randomly pick a question
# ask from user a question
# see if they are correct
# keep track the score
# tell a user the final score

questions = {
    "What is the output of print(2 + 3 * 4)?": 14,
    "How do you create a list in Python?": "[]",
    "What keyword is used to define a function in Python?": "def",
    "What is the output of len('Python')?": 6,
    "How do you import the math module?": "import math",
    "What is the difference between '==' and 'is' in Python?": "'==' checks value equality, 'is' checks object identity",
    "How do you write a comment in Python?": "#",
    "What is the output of type(3.14)?": "float",
    "How do you get the first element of a list lst = [10, 20, 30]?": "lst[0]",
    "What will print('Hello' * 3) output?": "HelloHelloHello"
}

import random

def trivia_game():

    question_list = list(questions.keys())
    total_questions = 3
    score = 0

    selected_questions = random.sample(question_list, total_questions)
    
    for index, question in enumerate(selected_questions, start=1):
        print(f'Question {index}: {question}')
        
        user_answer = input("Your answer: ").lower().strip()

        correct_answer = questions[question]

        if user_answer == str(correct_answer).lower():
            print("Correct!")
            score+=1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}")

    print(f"Gamer over! You got {round(score/total_questions*100), 2}% out of 100%")    



if __name__ == '__main__':

    trivia_game()