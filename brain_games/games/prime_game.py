import random
import prompt


GAME_QUIESTION = 'What number is missing in the progression?'


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
        print(f"'no' is wrong answer ;(. Correct answer was 'yes'.")
        return False
    elif is_prime is False and answer.lower() == "yes":
        print(f"'yes' is wrong answer ;(. Correct answer was 'no'.")
        return False