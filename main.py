#!/usr/bin/env python3
"""Write the office-printer joke to /output/entry.txt."""
import os

ENTRY = (
    'Our office printer has shown a "low toner" warning for three years. '
    "It has outlasted three managers, two rebrands, and one entire fiscal year. "
    "At this point it is a heritage feature."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
