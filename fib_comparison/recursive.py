from intpy.intpy import deterministic, initialize_intpy
import sys
from time import perf_counter


@deterministic
def recursive(n):
    if n == 1 or n == 2: 
        return 1
    else:
        return recursive(n-1) + recursive(n-2)


@initialize_intpy(__file__)
def main(n):
    moves = recursive(n)


if __name__ == '__main__':
    n = int(sys.argv[1])

    start = perf_counter()
    main(n)
    t = perf_counter() - start

    print(t)