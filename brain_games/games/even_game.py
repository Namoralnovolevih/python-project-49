import random


GAME_QUIESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_specifics():
    number = random.randint(1, 100)
    question = number
    if number % 2 == 0:
        result = "yes"
        return question, result
    elif number % 2 != 0:
        result = "no"
        return question, result
