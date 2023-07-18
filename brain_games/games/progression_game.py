import random


G_QUIESTION = 'What number is missing in the progression?'
MIN_NUMBER = 2
MAX_NUMBER = 5
P_NUM_MIN = 10
P_NUM_MAX = 60

def progression_members():
    random_step = random.randint(MIN_NUMBER, MAX_NUMBER)
    progression = list(range(P_NUM_MIN, P_NUM_MAX, random_step))
    return progression


def transformation(progression):
    progression_str = ' '.join(map(str, progression))
    random_number = random.choice(progression)
    return progression_str.replace(str(random_number), ".."), random_number


def question_and_answer():
    question, result = transformation(progression_members())
    return question, str(result)
