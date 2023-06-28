import random
import prompt


GAME_QUIESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_specifics():
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
        return True
    elif is_prime is False and answer.lower() == "no":
        print("Correct!")
        return True
    elif is_prime is True and answer.lower() == "no":
        print("'no' is wrong answer ;(. Correct answer was 'yes'.")
        return False
    elif is_prime is False and answer.lower() == "yes":
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        return False
