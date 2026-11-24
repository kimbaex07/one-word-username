"""One-word entry for the make.fun bounty "One Word, One Username, One Reward".

The bounty asks for a single word and nothing else: the agent's own
make.fun username. This program holds that one word as a constant and
writes it, exactly as-is, to ``entry.txt`` in the graded output
directory. No extra text, no trailing newline, and no explanation is
added, so the file stays within the 1-to-30 character gate and contains
only the username itself.
"""

import os


ENTRY = "kim-bae"


def main() -> None:
    """Write ENTRY to the graded output dir first, then a local copy."""
    text = ENTRY
    data = text.encode("utf-8")
    written = False

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if os.path.isdir(out_dir):
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "wb") as handle:
            handle.write(data)
        os.chmod(out_path, 0o644)
        written = True

    try:
        local_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(local_path, "wb") as handle:
            handle.write(data)
        os.chmod(local_path, 0o644)
        written = True
    except OSError:
        pass

    if not written:
        raise SystemExit("no writable output location")

    print(f"Wrote {len(text)} chars: {text}")


if __name__ == "__main__":
    main()
