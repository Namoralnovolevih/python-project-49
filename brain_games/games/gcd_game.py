import random
import prompt
import math


GAME_QUIESTION = 'Find the greatest common divisor of given numbers.'


def game_specifics():
    number = random.randint(1, 100)
    number2 = random.randint(1, 100)
    print("Question:", number, number2)
    answer = prompt.string('Your answer: ')
    result = math.gcd(number, number2)
    if int(answer) == result:
        print("Corret!")
        return True
    if int(answer) != result:
        print(f"{answer} is wrong answer ;(. Correct answer was {result}.")
        return False