#!/usr/bin/env/python

import random
import prompt


def main():
    print("Welcom to the brain games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\nWhat number is missing in the progression?')
    index = 0
    windscore = 3
    while index < windscore:
        index += 1
        random_step = random.randint(2, 5)
        progression = list(range(10, 60, random_step))
        number = random.choice(progression)
        progression_str = ' '.join(map(str, progression))
        print("Question:", progression_str.replace(str(number), ".."))
        answer = prompt.string('Your answer: ')
        if str(number) == answer:
            print("Corret!")
        elif str(number) != answer:
            return print(f"{answer} is wrong answer ;(. Correct answer was {number}.\nLet's try again,{name}!")
    return print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
