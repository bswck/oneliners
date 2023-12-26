# Split into multi-line for readability; this stmt expression can be fit into one line.

(
    ask := lambda prompt: (
        (ih := __import__("typing").cast("list[object]", [0]))
        and (ii := iter(ih))
        and [
            ((a := input("Your guess: ")) and ((a.isdigit() and (g := int(a))) or ih.append(0)))
            for _ in ii
        ]
        and g
    )
) and (n := __import__("random").randint(kmin := 1, kmax := 10)) and (it := iter(r := (range(kmin, kmax+1)))) and (
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
