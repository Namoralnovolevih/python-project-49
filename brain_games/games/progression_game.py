import random


GAME_QUIESTION = 'What number is missing in the progression?'
MIN_NUMBER = 2
MAX_NUMBER = 5


def progression_members():
    random_step = random.randint(MIN_NUMBER, MAX_NUMBER)
    progression = list(range(10, 60, random_step))
    return progression


def transformation(progression_members):
    progression_str = ' '.join(map(str, progression_members()))
    random_number = random.choice(progression_members())
    return progression_str.replace(str(random_number), ".."), random_number


def question_and_answer():
    question, result = transformation(progression_members())
    return question, str(result)
