import random
import prompt

GAME_QUIESTION = 'What number is missing in the progression?'


def game_specifics():
    random_step = random.randint(2, 5)
    progression = list(range(10, 60, random_step))
    number = random.choice(progression)
    progression_str = ' '.join(map(str, progression))
    print("Question:", progression_str.replace(str(number), ".."))
    answer = prompt.string('Your answer: ')
    if str(number) == answer:
        print("Corret!")
        return True
    elif str(number) != answer:
        print(f"{answer} is wrong answer ;(. Correct answer was {number}.")
        return False
