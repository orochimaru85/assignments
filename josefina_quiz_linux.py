"""Hej Josefina — frågesport i terminalen (ren text).

Körs i Linux (eller valfri terminal) via:

    python josefina_quiz_linux.py
"""

import sys
import time

JA = ("ja", "j", "yes", "y")
NEJ = ("nej", "n", "no")


def fraga(text: str, ratt: str, fel: str) -> None:
    """Ställ en ja/nej-fråga tills svaret är rätt."""
    while True:
        svar = input(text).strip().lower()
        if svar in JA:
            print(ratt)
            return
        if svar in NEJ:
            print(fel)
        else:
            print("Svara ja eller nej.")


def main() -> None:
    fraga(
        "Hej Josefina! Älskar du Fredrik? (ja/nej): ",
        "Rätt svar, han älskar dig också!",
        "Fel svar, gör om gör rätt!",
    )
    fraga(
        "Vill du äta god mat och kolla på Harry Potter sen ikväll? (ja/nej): ",
        "Rätt svar :)",
        "Fel svar, prova igen!",
    )

    print("HURRAAAA!!!!")
    time.sleep(5)
    sys.exit(0)


if __name__ == "__main__":
    main()
