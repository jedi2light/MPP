#!/usr/bin/env python3

import sys


def main():

    n, a, b = [int(_) for _ in input().split(' ')]

    ranged = range(a, b+1)

    try:
        assert(len(ranged) == n*n)
    except AssertionError:
        return -1

    matrix = [[0] * n] * n

    return 0

if __name__ == '__main__':

    sys.exit(main())
