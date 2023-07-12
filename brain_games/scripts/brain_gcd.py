#!/usr/bin/env/python
from brain_games.engine import run_game
from brain_games.games.gcd_game import G_QUIESTION, question_and_answer


def main():
    run_game(G_QUIESTION, question_and_answer)


if __name__ == '__main__':
    main()
