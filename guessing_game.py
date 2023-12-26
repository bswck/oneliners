# Split into multi-line for readability; this stmt expression can be fit into one line.

# Usage: python -m guessing_game [-h] [-min MIN_NUMBER] [-max MAX_NUMBER] [-g GUESSES]

# Options:
#   -h, --help                                  show this help message and exit
#   -min MIN_NUMBER, --min-number MIN_NUMBER    minimum number
#   -max MAX_NUMBER, --max-number MAX_NUMBER    maximum number
#   -g GUESSES, --guesses GUESSES               number of guesses

(p := __import__("argparse").ArgumentParser()) and (
    p.add_argument("-min", "--min-number", type=int, default=1)
) and (p.add_argument("-max", "--max-number", type=int, default=10)) and (
    p.add_argument("-g", "--guesses", type=int, default=5)
) and (ns := p.parse_args()) and ((kmin := ns.min_number), (kmax := ns.max_number)) and (
    gmax := ns.guesses
) and (
    ask := lambda prompt: (
        (ih := __import__("typing").cast("list[object]", [0]))
        and (ii := iter(ih))
        and [
            (
                (a := input("Your guess: "))
                and (a.isdigit() and ((g := int(a)) or True)) or ih.append(0)
            )
            for _ in ii
        ]
        and g
    )
) and (n := __import__("random").randint(kmin, kmax)) and (it := iter(r := (range(gmax)))) and (
    log := [
        g
        if (
            (g := ask("What is your guess? ")) != n
            and (print("Too low" if g < n else "Too high") or True)
        )
        else (print("You win!") or list(it))
        for _ in it
    ]
) and len(log) == len(r) and print(f"You ran out of guesses! The right number was {n}.")
