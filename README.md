# Programming Assignment 3 - Highest Value Common Subsequence

**Name:** Pablo Pupo
**UFID:** 96796601

## Problem

Given an alphabet of K characters where each character has a nonnegative
integer value, and two strings A and B, find a common subsequence of A
and B with the maximum total value. Output both the value and one such
subsequence.

## Layout

```
highest-value-lcs/
    src/
        main.py     (entry point, arg parsing and file I/O)
        hvlcs.py    (input parser, DP solver, reconstruction)
    data/
        example.in  (worked example from the assignment PDF)
        example.out (expected output for example.in)
        test1.in ... test10.in   (10 randomly generated test inputs)
    testing/
        generator.py   (random input file generator)
```

## Build and Run

Needs Python 3. No compile step.

From the project root:

```
python src/main.py example.in
```

This reads `data/example.in`, runs the DP, prints the max value and
one optimal subsequence, and writes the same thing to
`data/example.out`. For the included example you should see:

```
9
cb
```

If you leave off the filename it defaults to `example.in`. The repo
also ships 10 randomly generated test files (`data/test1.in` through
`data/test10.in`, string lengths 25 to 600) which can be run the same
way, e.g. `python src/main.py test5.in`.

To generate your own random input file:

```
python testing/generator.py <n> <filename>
```

## Input format

```
K
x1 v1
x2 v2
...
xK vK
A
B
```

- K is the alphabet size.
- The next K lines each give a character and its nonnegative integer value.
- A and B are the two strings, on their own lines.
