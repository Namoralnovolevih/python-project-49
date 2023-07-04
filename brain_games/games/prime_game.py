import random


GAME_QUIESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_specifics():
    number = random.randint(2, 200)
    question = number
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime is True:
        result = "yes"
        return question, result
    elif is_prime is False:
        result = "no"
        return question, result