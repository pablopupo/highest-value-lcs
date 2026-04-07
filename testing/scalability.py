import os
import sys
import time
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
from hvlcs import parse_input, solve


"""
Times the HVLCS solver on test1.in through test10.in and writes a runtime
plot to data/runtimes.png.

USAGE:
    python testing/scalability.py
"""

TEST_FILES = [f"test{i}.in" for i in range(1, 11)]
REPEATS = 5


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    proj_root = os.path.dirname(base_dir)
    data_dir = os.path.join(proj_root, "data")

    products = []
    times = []

    for name in TEST_FILES:
        path = os.path.join(data_dir, name)
        parsed = parse_input(path)
        if parsed is None:
            continue

        values, A, B = parsed
        n, m = len(A), len(B)

        # run a few times and keep the best one to cut down on noise
        best = None
        for _ in range(REPEATS):
            t0 = time.perf_counter()
            solve(values, A, B)
            elapsed = time.perf_counter() - t0
            if best is None or elapsed < best:
                best = elapsed

        products.append(n * m)
        times.append(best)

        print(f"{name}: n={n}, m={m}, n*m={n * m}, time={best:.6f}s")

    # plot runtime against n*m
    plt.figure()
    plt.plot(products, times, marker='o')
    plt.xlabel("n*m")
    plt.ylabel("Runtime (seconds)")
    plt.title("HVLCS solver runtime")
    plt.grid(True)

    out_path = os.path.join(data_dir, "runtimes.png")
    plt.savefig(out_path)
    print("\nRuntime plot saved to " + out_path)


if __name__ == "__main__":
    main()
