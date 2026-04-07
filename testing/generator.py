import os
import random
import sys


"""
Random input file generator for the HVLCS problem. Picks a small alphabet,
assigns random values, and writes two random strings of length n.

USAGE:
    python testing/generator.py <n> <filename>
"""

ALPHABET = ['a', 'b', 'c', 'd']
MAX_VALUE = 10

def generate(n, filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    proj_root = os.path.dirname(base_dir)
    path = os.path.join(proj_root, "data", filename)

    k = len(ALPHABET)
    values = [random.randint(1, MAX_VALUE) for _ in ALPHABET]

    A = "".join(random.choices(ALPHABET, k=n))
    B = "".join(random.choices(ALPHABET, k=n))

    try:
        with open(path, 'w') as f:
            f.write(f"{k}\n")
            for ch, v in zip(ALPHABET, values):
                f.write(f"{ch} {v}\n")
            f.write(f"{A}\n")
            f.write(f"{B}\n")
    except Exception as e:
        print(f"Error: {e}")




if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise Exception("Usage: python generator.py <n> <filename>")

    n = int(sys.argv[1])
    filename = sys.argv[2]

    generate(n, filename)
