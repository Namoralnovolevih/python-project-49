import prompt


def run_game(game_task, game_specifics):
    print("Welcom to the brain games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n{game_task}')
    index = 0
    windscore = 3
    while index < windscore:
        index += 1
        if not game_specifics():
            return print(f"Let's try again, {name}!")
    return print(f'Congratulations, {name}!')