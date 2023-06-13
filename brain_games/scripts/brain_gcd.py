#!/usr/bin/env/python

import random
import prompt
import math


def main():
    print("Welcom to the brain games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\nFind the greatest common divisor of given numbers.')
    index = 0
    windscore = 3
    while index < windscore:
        index += 1
        number = random.randint(1, 100)
        number2 = random.randint(1, 100)
        print("Question:", number, number2)
        answer = prompt.string('Your answer: ')
        result = math.gcd(number, number2)
        if int(answer) == result:
            print("Corret!")
        if int(answer) != result:
            return print(f"{answer} is wrong answer ;(. Correct answer was {result}.\nLet's try again, {name}!")
    return print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
