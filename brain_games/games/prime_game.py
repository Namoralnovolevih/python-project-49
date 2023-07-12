import random


G_QUIESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 2
MAX_NUMBER = 100


def prime_number_check(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def question_and_answer():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = number
    if prime_number_check(number) is True:
        result = "yes"
        return question, result
    else:
        result = "no"
        return question, result
