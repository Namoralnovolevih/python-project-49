import random


G_QUIESTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def сhecking_for_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def question_and_answer():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = number
    if сhecking_for_even(number) is True:
        result = "yes"
        return question, result
    else:
        result = "no"
        return question, result
