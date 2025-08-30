# Quiz Game
# list of questions
# store answers
# randomly pick a question
# ask from user a question
# see if they are correct
# keep track the score
# tell a user the final score

questions = {
    "What is the output of print(2 + 3 * 4)?": {
        "A": 20,
        "B": 14,
        "C": 24,
        "answer": "B"
    },
    "How do you create a list in Python?": {
        "A": "{}",
        "B": "()",
        "C": "[]",
        "answer": "C"
    },
    "What keyword is used to define a function in Python?": {
        "A": "func",
        "B": "def",
        "C": "function",
        "answer": "B"
    },
    "What is the output of len('Python')?": {
        "A": 5,
        "B": 6,
        "C": 7,
        "answer": "B"
    },
    "How do you import the math module?": {
        "A": "import mathematics",
        "B": "import math",
        "C": "include math",
        "answer": "B"
    },
    "What is the difference between '==' and 'is' in Python?": {
        "A": "'==' checks identity, 'is' checks equality",
        "B": "Both are the same",
        "C": "'==' checks value equality, 'is' checks object identity",
        "answer": "C"
    },
    "How do you write a comment in Python?": {
        "A": "//",
        "B": "/* */",
        "C": "#",
        "answer": "C"
    },
    "What is the output of type(3.14)?": {
        "A": "float",
        "B": "int",
        "C": "str",
        "answer": "A"
    },
    "How do you get the first element of a list lst = [10, 20, 30]?": {
        "A": "lst[1]",
        "B": "lst[0]",
        "C": "lst[-1]",
        "answer": "B"
    },
    "What will print('Hello' * 3) output?": {
        "A": "Hello3",
        "B": "Hello Hello Hello",
        "C": "HelloHelloHello",
        "answer": "C"
    }
}

import random


def quiz_game():
    questions_list = list(questions.keys())
    total_questions = 3
    score = 0

    selected_questions = random.sample(questions_list, total_questions)

    for index, question in enumerate(selected_questions,start=1):
        print(f'{index}. {question}')
        print(f' A) {questions[question]['A']}')
        print(f' B) {questions[question]['B']}')
        print(f' C) {questions[question]['C']}')

        user_answer = input("What is your answer: ").strip()
        correct_answer = questions[question]['answer']

        if user_answer == correct_answer:
            print('Correct!')
            score+=1
        else:
            print(f"Incorrect. Correct choice is {correct_answer}")
    
    print(f"Game over! You got {round(score/total_questions*100, 0)}% out of 100%")



if __name__ == '__main__':

    quiz_game()