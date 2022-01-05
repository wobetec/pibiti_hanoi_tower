from intpy.intpy import deterministic, initialize_intpy
import sys
from time import perf_counter


dic = {1:2, 2:1, 3:0}
@deterministic
def rec_1(n, begin, end):
    aux = dic[begin+end]
    if n != 1: 
        return rec_1(n-1, begin, aux) + [(begin, end)] + rec_1(n-1, aux, end)
    else:
        return [(begin, end)]


@initialize_intpy(__file__)
def main(n):
    moves = rec_1(n, 0, 2)


if __name__ == '__main__':
    n = int(sys.argv[1])

    start = perf_counter()
    main(n)
    t = perf_counter() - start

    print(t)