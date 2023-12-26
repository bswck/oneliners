# Split into multi-line for readability.
# This expression statement (https://docs.python.org/3/reference/simple_stmts.html#expression-statements)
#   can be fit into one line.

# Usage: guessing_game.py [-h] [-min MIN_NUMBER] [-max MAX_NUMBER] [-g GUESSES]

# Options:
#   -h, --help                                  show this help message and exit
#   -min MIN_NUMBER, --min-number MIN_NUMBER    minimum random number to be guessed
#   -max MAX_NUMBER, --max-number MAX_NUMBER    maximum random number to be guessed
#   -g GUESSES, --max-guesses GUESSES           maximum number of player's guesses

(argument_parser := __import__("argparse").ArgumentParser()) and (
    argument_parser.add_argument(
        "-min",
        "--min-number",
        type=int,
        help="minimum random number to be guessed",
        default=1,
    )
) and (
    argument_parser.add_argument(
        "-max",
        "--max-number",
        type=int,
        help="maximum random number to be guessed",
        default=10,
    )
) and (
    argument_parser.add_argument(
        "-g",
        "--max-guesses",
        type=int,
        help="maximum number of player's guesses",
        default=5,
    )
) and (arguments := argument_parser.parse_args()) and (
    (min_number := arguments.min_number),
    (max_number := arguments.max_number),
) and (max_guesses := abs(arguments.max_guesses)) and (
    input_number := lambda prompt: (
        (__input_helper := __import__("typing").cast("list[object]", [0]))
        and (__input_iterator := iter(__input_helper))
        and [
            (
                answer_candidate := input(
                    (prompt := prompt or "Input a number:")
                    + " " * (not prompt.endswith(" "))
                )
            ).strip()
            and (
                (
                    answer_candidate[1:].isdigit()
                    if answer_candidate.startswith("-")
                    else answer_candidate.isdigit()
                )
                and ((number_from_player := int(answer_candidate)) or True)
            )
            or __input_helper.append(0)
            for _ in __input_iterator
        ]
        and number_from_player
    )
) and (random_number := __import__("random").randint(min_number, max_number)) and (
    __game_iterator := iter(range(max_guesses))
) and (
    guesses_made := [
        answered_number
        if (
            (answered_number := input_number("What is your guess?")) != random_number
            and (
                print(
                    "Too low" if answered_number < random_number else "Too high"
                ) or True
            )
        )
        else (print("You win!") or list(__game_iterator))
        for _ in __game_iterator
    ]
) and len(guesses_made) == max_guesses and answered_number != random_number and print(
    f"You ran out of guesses! The right number was {random_number}."
)
