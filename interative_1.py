import sys
from time import perf_counter


def interative(n):
    moves = []
    tower = [list(range(n, 0, -1)), [], []]

    def move(begin, end):
        try:
            if len(tower[end]) == 0 or tower[end][-1] > tower[begin][-1]:
                tower[end].append(tower[begin].pop(-1))
                return True
            else:
                return False
        except:
            return False


    if n % 2 == 0:
        lista = [[(0, 1), (1, 0)], [(0, 2), (2, 0)], [(1, 2), (2, 1)]]
    else:
        lista = [[(0, 2), (2, 0)], [(0, 1), (1, 0)], [(1, 2), (2, 1)]]

    num_moves = 0
    while len(tower[2]) < n:
        
        if move(lista[num_moves][0][0], lista[num_moves][0][1]):
            moves.append(lista[num_moves][0])
        elif move(lista[num_moves][1][0], lista[num_moves][1][1]):
            moves.append(lista[num_moves][1])

        num_moves += 1
        if num_moves == 3:
            num_moves = 0


if __name__ == '__main__':
    n = int(sys.argv[1])

    start = perf_counter()
    interative(n)
    t = perf_counter() - start
    print("""['v027x']
False
pickle""")
    print(t)




