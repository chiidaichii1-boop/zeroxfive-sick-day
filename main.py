"""The Funniest Sick-Day Excuse - make.fun entry.

Writes one line, under 200 characters, to /output/entry.txt.
Stdlib only. Reads the output dir from MAKEFUN_OUTPUT_DIR
(fallback /output), creates it if needed, never deletes it.
"""

import os

ENTRY = (
    # Verified: 131 characters, within the 1-200 gate.
    "Can't come in \u2014 my fridge updated overnight and locked itself "
    "until I rate the update, and I've been negotiating with it since 6am."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry is only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
