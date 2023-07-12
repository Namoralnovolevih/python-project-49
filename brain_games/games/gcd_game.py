import random
import math


G_QUIESTION = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100


def question_and_answer():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{number} {number2}'
    result = math.gcd(number, number2)
    return question, str(result)
