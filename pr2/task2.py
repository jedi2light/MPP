#!/usr/bin/env python3

import sys
import functools

def main():

    # Even in Clojure we have let macros, so...

    list_one = list(map(lambda s: pow(int(s), 2), input().split(' ')))
    list_two = list(map(lambda s: pow(int(s), 2), input().split(' ')))

    # Now we have to build a transposed matrix

    matrix = list(zip(list_one, list_two))

    # Now we have to build a list of sums

    sums = list(map(lambda e: sum(e), matrix ))

    # Now we can print generated list

    print(sums)

    return 0

if __name__ == '__main__':

    sys.exit(main())
