import sys
from time import perf_counter

def interative(n):
    cache = [1, 1]
    
    if n < 2:
        return cache[n-1]
    else:
        for i in range(2, n):
            cache.append(cache[i-1]+cache[i-2])
        return cache[-1]


if __name__ == '__main__':
    n = int(sys.argv[1])

    start = perf_counter()
    interative(n)
    t = perf_counter() - start
    print("""No Intpy
True
pickle""")
    print(t)
