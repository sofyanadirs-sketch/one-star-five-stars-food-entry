"""one-star-five-stars-food-entry.

The entry is one sentence, spoken by an alien tourist leaving
Earth a one-star review that still compliments the food:

    Your waiters demand extra coins for carrying a plate ten
    steps, which is extortion with a smile, but the beef
    rendang melted so slowly I tipped twice and apologised
    to the cow.

The joke works because the alien reads an ordinary human
custom -- tipping -- as a shakedown: waiters "demand extra
coins" for carrying a plate ten steps. That is the one-star
grievance, an outsider's bafflement at a habit humans never
question. The turn lands on the rendang: the beef melted so
slowly that the same alien who called tipping extortion tipped
twice anyway, and then apologised to the cow -- the complainer
does the very thing he complained about, and the apology goes
to the animal, not the waiter. One joke, one concrete food,
no second gag crowding it, and it reads cleanly aloud.

Joke construction: tipping is the perfect alien grievance
because it is a human custom nobody on Earth questions, so an
outsider calling it "extortion with a smile" instantly sounds
like a tourist from another planet, not a tourist from another
country. The number is concrete -- ten steps -- so the
complaint is a counted fact, not a vague grumble. The second
twist is the alien tipping twice anyway: the food beat the
grievance, and apologising to the cow (rather than thanking
the waiter) keeps the voice alien to the last word.

This program writes that one sentence, exactly as-is, to
``entry.txt`` in the output directory. It uses only the Python
3 standard library: no network, no randomness, no clock, no
input.
"""

import os

ENTRY = (
    "Your waiters demand extra coins for carrying a plate ten "
    "steps, which is extortion with a smile, but the beef "
    "rendang melted so slowly I tipped twice and apologised "
    "to the cow."
)


def _validate(line):
    """Check the entry line against the competition rules."""
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    if line != line.strip():
        raise ValueError("entry must not have surrounding whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.endswith("."):
        raise ValueError("entry must end with a period")


def _write(path, line):
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    os.chmod(path, 0o644)


def main():
    _validate(ENTRY)

    # Fail-fast gate: re-assert the entry contract right before
    # writing, so a bad entry dies here instead of producing a
    # file that would fail judging.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY == ENTRY.strip(), "entry must not have edge whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, (
        "entry must be a single line"
    )
    assert ENTRY.endswith("."), "entry must end with a period"

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(output_dir, "entry.txt")

    try:
        os.makedirs(output_dir, exist_ok=True)
        _write(target, ENTRY)
    except OSError:
        fallback_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "output"
        )
        os.makedirs(fallback_dir, exist_ok=True)
        target = os.path.join(fallback_dir, "entry.txt")
        _write(target, ENTRY)

    with open(target, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != ENTRY:
        raise ValueError("entry.txt does not match the entry line")

    print(ENTRY)


if __name__ == "__main__":
    main()
