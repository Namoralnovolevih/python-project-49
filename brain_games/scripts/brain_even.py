#!/usr/bin/env/python

import prompt
import random 


def main():
    print("Welcom to the brain games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello,{name}!\nAnswer "yes" if the number is even, otherwise answer "no".')
    index = 0
    windscore = 3
    while index < windscore:
        index += 1
        number = random.randint(1, 100)
        print("Question:", number)
        answer = prompt.string('Your answer: ')
        if number % 2 == 0 and answer.lower() == "yes":
            print("Corret!")
        elif number % 2 != 0 and answer.lower() == "no":
            print("Correct!")
        elif number % 2 == 0 and answer.lower() != "yes":
            return print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}")
        elif number % 2 != 0 and answer.lower() != "no":
            return print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}")
    return print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
