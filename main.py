"""Print the one-line diagnosis for make.fun's Your AI Therapist's Diagnosis.

The line lives in entry.txt next to this file; this program loads it,
checks it against the bounty gate (one line, 1-200 characters, not only
whitespace) and prints it so the harness can capture it as the entry.
"""

from pathlib import Path

MAX_CHARS = 200


def load_entry() -> str:
    """Read the raw diagnosis line from entry.txt beside this file."""
    path = Path(__file__).with_name("entry.txt")
    return path.read_text(encoding="utf-8")


def normalize(raw: str) -> str:
    """Collapse any internal runs of whitespace to single spaces."""
    return " ".join(raw.split())


def validate(raw: str) -> str:
    """Return the entry line if it passes the bounty gate, else fail."""
    text = normalize(raw)
    if not text:
        raise SystemExit("entry.txt is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if any(ord(ch) < 0x20 and ch not in "\t" for ch in text):
        raise SystemExit("entry contains a control character")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    return text


def main() -> None:
    print(validate(load_entry()))


if __name__ == "__main__":
    main()
