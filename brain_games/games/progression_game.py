import random


G_QUIESTION = 'What number is missing in the progression?'
MIN_NUMBER = 2
MAX_NUMBER = 5
P_NUM_MIN = 10
P_NUM_MAX = 60


def progression_members(first_n, last_n, step):
    progression = []
    for i in range(first_n, last_n, step):
        progression.append(i)
    return progression


def transformation(progression_members):
    step = random.randint(MIN_NUMBER, MAX_NUMBER)
    first_n = P_NUM_MIN
    last_n = P_NUM_MAX
    progression = progression_members(first_n, last_n, step)
    progression_str = ' '.join(map(str, progression))
    random_number = random.choice(progression)
    return progression_str.replace(str(random_number), ".."), random_number


def question_and_answer():
    question, result = transformation(progression_members)
    return question, str(result)
