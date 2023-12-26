# Usage: guessing_game.py [-h] [-min MIN_NUMBER] [-max MAX_NUMBER] [-g GUESSES]

# Options:
#   -h, --help                                  show this help message and exit
#   -min MIN_NUMBER, --min-number MIN_NUMBER    minimum random number to be guessed
#   -max MAX_NUMBER, --max-number MAX_NUMBER    maximum random number to be guessed
#   -g GUESSES, --max-guesses GUESSES           maximum number of player's guesses

# Split into multi-line and enriched with comments for you to understand what's going on.
# This expression statement (https://docs.python.org/3/reference/simple_stmts.html#expression-statements)
#   can be fit into one line.
#
# To see how it would look like in one line, run:
# $ python -c "print((ast := __import__('ast')).unparse(ast.parse(__import__('pathlib').Path('guessing_game.py').read_text())))"
# on Python 3.9+.

# Make customizable via command line arguments.
(argument_parser := __import__("argparse").ArgumentParser()) and (
    # Allow the player to specify the minimum random number to be guessed.
    argument_parser.add_argument(
        "-min",
        "--min-number",
        type=int,
        help="minimum random number to be guessed",
        default=1,
    )
) and (
    # Allow the player to specify the maximum random number to be guessed.
    argument_parser.add_argument(
        "-max",
        "--max-number",
        type=int,
        help="maximum random number to be guessed",
        default=10,
    )
) and (
    # Allow the player to specify the maximum number of legal guesses.
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
    # ↓ Abort on max_guesses == 0. Ensure that max_guesses is positive.
) and (max_guesses := abs(arguments.max_guesses)) and (
    # Create a function that will ask the player for a number.
    # If the player inputs a non-number, ask again until a number is inputted.
    input_number := lambda prompt: (
        # A collection that will influence the lifetime of the iterator below.
        (__input_helper := __import__("typing").cast("list[object]", [0]))
        # An iterator which should yield values as long as the player has to be asked for a number.
        and (__input_iterator := iter(__input_helper))
        # Add an object to the iterator to ask the player for a number again.
        and (__ask_again := lambda: __input_helper.append(0))
        and [
            # Do ask the player for a number.
            (
                answer_candidate := input(
                    (prompt := prompt or "Input a number:") + " " * (not prompt.endswith(" "))
                )
                # Strip the answer so we can examine if there's a minus sign at the start.
            ).strip()
            and (
                (
                    answer_candidate[1:].isdigit()
                    if answer_candidate.startswith("-")
                    else answer_candidate.isdigit()
                )
                # Success; the number is valid.
                and ((number_from_player := int(answer_candidate)) or True)
            )
            # Miss; the number is invalid. Ask again.
            or __ask_again()
            # As long as the iterator yields values, the player is asked for the number.
            for _ in __input_iterator
        ]
        # Return the answer.
        and number_from_player
    )
    # ↓ Draw a number between min_number and max_number.
) and (random_number := __import__("random").randint(min_number, max_number)) and (
    # ↓ Create the game iterator which will be used to keep the game running for max_guesses times.
    __game_iterator := iter(range(max_guesses))
) and (
    # Track how many guesses the player made so we know what to display at the end.
    guesses_made := len(
        [
            answered_number
            if (
                (answered_number := input_number("What is your guess?")) != random_number
                and (print("Too low" if answered_number < random_number else "Too high") or True)
            )
            # If the player guessed the right number, print "You win!"
            #   and stop the game by exhausting ↓ the iterator with the list constructor.
            else (print("You win!") or [*__game_iterator])
            # As long as the iterator yields values, the game is running.
            for _ in __game_iterator
        ]
    )
    # ↓ If the game was not stopped by the player guessing the right number,
    #   inform them that they ran out of guesses and tell what the right number was.
) and guesses_made == max_guesses and answered_number != random_number and print(
    f"You ran out of guesses! The right number was {random_number}."
)
