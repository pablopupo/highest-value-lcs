import os
import sys
from hvlcs import *


"""
Main entry point for the HVLCS solver. Reads an input file, runs the DP,
prints the results, and saves them to data/<name>.out.

USAGE:
    python src/main.py <filename>
"""

def main():

    # Set up
    base_dir = os.path.dirname(os.path.abspath(__file__))
    proj_root = os.path.dirname(base_dir)
    data_dir = os.path.join(proj_root, "data")

    filename = "example.in"
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    input_path = os.path.join(data_dir, filename)
    output_path = os.path.join(data_dir, filename[:-3] + ".out")

    print("Parsing input file " + filename)

    print("=" * 50)

    parsed = parse_input(input_path)

    if parsed is not None:
        values, A, B = parsed

        total, subseq = solve(values, A, B)

        print(total)
        print(subseq)

        with open(output_path, 'w') as f:
            f.write(f"{total}\n")
            f.write(f"{subseq}\n")

        print("Output saved to " + filename[:-3] + ".out")




if __name__ == "__main__":
    main()
