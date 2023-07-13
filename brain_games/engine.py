import prompt


NUMBER_OF_ROUNDS = 3


def run_game(game):
    print("Welcom to the brain games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n{game.G_QUIESTION}')
    index = 0
    while index < NUMBER_OF_ROUNDS:
        index += 1
        question, result = game.question_and_answer()
        print("Question:", question)
        answer = prompt.string('Your answer: ')
        if answer == result:
            print("Correct!")
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {result}.")
            print(f"Let's try again, {name}!")
            return
    return print(f'Congratulations, {name}!')
