# Make the AI Judge Laugh: Office Jokes — one-line entry.
#
# The joke is a fixed string: the program is deterministic by construction,
# so two runs write the same bytes. It reads $MAKEFUN_OUTPUT_DIR when set,
# else /output, and writes entry.txt there. The line is a single line of
# under 200 characters, matching the competition's gate.

import os

JOKE = "Our office printer has shown a \"low toner\" warning for three years. It has outlasted three managers, two rebrands, and one entire fiscal year. At this point it is a heritage feature."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
