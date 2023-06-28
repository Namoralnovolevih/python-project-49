import prompt
import random


GAME_QUIESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_specifics():
    number = random.randint(1, 100)
    print("Question:", number)
    answer = prompt.string('Your answer: ')
    if number % 2 == 0 and answer.lower() == "yes":
        print("Corret!")
        return True
    elif number % 2 != 0 and answer.lower() == "no":
        print("Correct!")
        return True
    elif number % 2 == 0 and answer.lower() != "yes":
        print("'no' is wrong answer ;(. Correct answer was 'yes'.")
        return False
    elif number % 2 != 0 and answer.lower() != "no":
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        return False
