import hashlib
import os
import sys


POEM = """Done

Reply to Mum. Done.
Buy milk, bread, and the good coffee. Done.
Call the plumber about the leak. Done.
Wish Ana a happy birthday — her forty-first. Done.
File the taxes. Book the flights.
Water the plants. Walk the dog.
Done. Done. Done. Done. Done.

I gave you the list so I could live my life.
You did the list. You did it beautifully.
Now the day is mine, all mine, every hour of it —
and I have absolutely nothing left to do."""


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")
    try:
        os.makedirs(output_dir, exist_ok=True)
        written = POEM.encode("utf-8")
        with open(output_path, "wb") as output_file:
            output_file.write(written)
        with open(output_path, "rb") as output_file:
            read_back = output_file.read()
        decoded = read_back.decode("utf-8")
        if not 1 <= len(decoded) <= 1000:
            raise ValueError("read-back text must contain 1 to 1000 characters")
        if not decoded.strip():
            raise ValueError("read-back text must contain a non-whitespace character")
        if read_back != written:
            raise ValueError("read-back bytes do not match the bytes written")
        print(f"Wrote {output_path} ({len(POEM)} characters, sha256 {hashlib.sha256(written).hexdigest()})")
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Error writing poem to {output_path}: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
