#!/usr/bin/env/python

from brain_games.engine import run_game
from brain_games.games.calc_game import GAME_QUIESTION, game_specifics


def main():
    run_game(GAME_QUIESTION, game_specifics)


if __name__ == '__main__':
    main()