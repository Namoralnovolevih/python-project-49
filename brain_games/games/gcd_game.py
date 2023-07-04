import random
import math


GAME_QUIESTION = 'Find the greatest common divisor of given numbers.'


def game_specifics():
    number = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f'{number} {number2}'
    result = math.gcd(number, number2)
    return question, str(result)
