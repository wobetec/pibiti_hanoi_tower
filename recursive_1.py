from intpy.intpy import deterministic, initialize_intpy
import sys
from time import perf_counter


tower = []
def move(tup):
    if len(tower[tup[1]]) == 0 or tower[tup[1]][-1] > tower[tup[0]][-1]:
        tower[tup[1]].append(tower[tup[0]].pop(-1))
        return True
    else:
        return False


dic = {1:2, 2:1, 3:0}
@deterministic
def rec_1(n, begin, end):
    aux = dic[begin+end]
    if n != 1: 
        return rec_1(n-1, begin, aux) + [(begin, end)] + rec_1(n-1, aux, end)
    else:
        return [(begin, end)]


def show():
    print("################")
    for i in tower:
        print(i)
    print("################")


@initialize_intpy(__file__)
def main():
    #show()
    moves = rec_1(n, 0, 2)
    for tup in moves:
        move(tup)
    #show()

if __name__ == '__main__':
    n = int(sys.argv[1])
    tower = [list(range(n, 0, -1)), [], []]
    moves = 0
    start = perf_counter()
    main()
    t = perf_counter() - start
    print(t)