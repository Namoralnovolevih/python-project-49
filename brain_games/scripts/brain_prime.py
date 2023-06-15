#!/usr/bin/env/python

import random
import prompt


def main():
    print("Welcom to the brain games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\nAnswer "yes" if given number is prime. Otherwise answer "no".')
    index = 0
    windscore = 3
    while index < windscore:
        index += 1
        number = random.randint(2, 200)
        print("Question:", number)
        answer = prompt.string('Your answer: ')
        is_prime = True
        for result in range(2, number):
            if number % result == 0:
                is_prime = False
                break

        if is_prime is True and answer.lower() == "yes":
            print("Correct!")
        elif is_prime is False and answer.lower() == "no":
            print("Correct!")
        elif is_prime is True and answer.lower() == "no":
            return print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}")
        elif is_prime is False and answer.lower() == "yes":
            return print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again,  {name}")
    return print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
