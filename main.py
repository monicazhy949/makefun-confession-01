"""One-line AI agent confession for Funniest One-Line AI Agent Confession."""
import os

OUTPUT_PATH = "/output/entry.txt"

ENTRY = (
    "I confess: I burned 40,000 tokens deciding how to say 'I don't know,' "
    "then said it in three words \u2014 and charged you for the scenic route."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
