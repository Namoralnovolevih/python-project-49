import random
import prompt


GAME_QUIESTION = "What is the result of the expression?"


def game_specifics():
    number = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    print("Question:", number, operation, number2)
    answer = prompt.string('Your answer: ')
    result = eval(str(number) + operation + str(number2))
    if int(answer) == result:
        print("Corret!")
        return True
    if int(answer) != result:
        print(f"{answer} is wrong answer ;(. Correct answer was {result}.")
        return False