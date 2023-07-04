import random


GAME_QUIESTION = "What is the result of the expression?"


def game_specifics():
    number = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    question = f'{number} {operation} {number2}'
    result = eval(str(number) + operation + str(number2))
    return question, str(result)