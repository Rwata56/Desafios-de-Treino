import string
from typing import Any


# TODO CORRIGIR USANDO CLASSE
def start_game(word: str, max_attempts: int = 9) -> dict[str, Any]:
    return {
        "word": word.lower(),
        "attempts_left": max_attempts,
        "guessed_letters": set(),
        "correct_letters": set(),
        "status": "ongoing",  # can be 'ongoing', 'won', 'lost'
    }


def guess(game: dict[str, Any], letter: str) -> None:
    if game["status"] != "ongoing" or letter not in string.ascii_letters:
        return

    letter = letter.lower()
    if letter in game["guessed_letters"]:
        return

    game["guessed_letters"].add(letter)

    if letter in game["word"]:
        game["correct_letters"].add(letter)
        if set(game["word"]) <= game["correct_letters"]:
            game["status"] = "won"
    else:
        game["attempts_left"] -= 1
        if game["attempts_left"] <= 0:
            game["status"] = "lost"


def get_display_word(game: dict[str, Any]) -> str:
    return "".join([c if c in game["correct_letters"] else "_" for c in game["word"]])


def is_won(game: dict[str, Any]) -> bool:
    return game["status"] == "won"


def is_lost(game: dict[str, Any]) -> bool:
    return game["status"] == "lost"


def is_finished(game: dict[str, Any]) -> bool:
    return game["status"] in ("won", "lost")
