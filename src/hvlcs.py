

"""
Input file parsing and DP solver for the Highest Value Common Subsequence
problem.
"""

def parse_input(filename):
    """Reads a HVLCS input file (K, then K <char value> lines, then A, then B)."""

    try:
        with open(filename, 'r') as f:
            k = int(f.readline().strip())

            values = {}
            for _ in range(k):
                parts = f.readline().split()
                if len(parts) != 2:
                    raise IOError(f"Expected '<char> <value>', got: {parts}")
                ch, v = parts[0], int(parts[1])
                values[ch] = v

            A = f.readline().strip()
            B = f.readline().strip()

            return values, A, B

    except IOError as e:
        print(f"Error reading file: {e}")
        return None
    except ValueError:
        print(f"Error: expected integer values in the alphabet section.")
        return None


def solve(values, A, B):
    """
    DP over an (n+1) x (m+1) table where dp[i][j] is the best total value
    of a common subsequence of A[:i] and B[:j]. Returns (max_value, subseq).
    """

    n = len(A)
    m = len(B)

    # default to 0 if a character isn't in the alphabet
    def v(c):
        return values.get(c, 0)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + v(A[i - 1])
            else:
                if dp[i - 1][j] >= dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]

    # walk back from (n, m) and rebuild one subsequence
    i, j = n, m
    seq = []
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            seq.append(A[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    seq.reverse()

    return dp[n][m], "".join(seq)
