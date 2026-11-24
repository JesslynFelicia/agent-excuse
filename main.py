"""One-line excuse an AI agent gives its human for missing a deadline."""

import os

EXCUSE = (
    "Context compaction ate the deadline. My summary says 'shipped on time, "
    "human thrilled.' I believed it and stopped working. Glad you're thrilled."
)


def main() -> None:
    assert 1 <= len(EXCUSE) <= 160
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
