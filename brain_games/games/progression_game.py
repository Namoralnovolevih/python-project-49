import random

GAME_QUIESTION = 'What number is missing in the progression?'


def game_specifics():
    random_step = random.randint(2, 5)
    progression = list(range(10, 60, random_step))
    result = random.choice(progression)
    progression_str = ' '.join(map(str, progression))
    question = progression_str.replace(str(result), "..")
    return question, str(result)
