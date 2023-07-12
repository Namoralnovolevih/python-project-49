import random


GAME_QUIESTION = "What is the result of the expression?"
MIN_NUMBER = 1
MAX_NUMBER = 100


def question_and_answer():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    question = f'{number} {operation} {number2}'
    result = eval(str(number) + operation + str(number2))
    return question, str(result)
