import prompt


def run_game(game_task, game_specifics):
    print("Welcom to the brain games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n{game_task}')
    index = 0
    windscore = 3
    while index < windscore:
        index += 1
        question, result = game_specifics()
        print("Question:", question)
        answer = prompt.string('Your answer: ')
        if answer == result:
            print("Correct!")
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {result}.")
            return f"Let's try again, {name}!"
    return print(f'Congratulations, {name}!')