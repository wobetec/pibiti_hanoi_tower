from os import system
import sys

def game(n, method = "play_game", show_steps = False):
    tower = [list(range(n, 0, -1)), [], []]
    moves = 0

    def move(begin, end):
        if len(tower[end]) == 0 or tower[end][-1] > tower[begin][-1]:
            tower[end].append(tower[begin].pop(-1))
            return True
        else:
            return False
    
    def show():
        print("################")
        for i in tower:
            print(i)
        print("################")
    
    def play_game():
        while True:
            system("cls")
            show()
            begin, end = input("from / to: ").split()
            move(int(begin), int(end))


    dic = {1:2, 2:1, 3:0}
    def rec_1(n, begin, end):
        aux = dic[begin+end]
        if n != 1:
            rec_1(n-1, begin, aux)
            move(begin, end)
            rec_1(n-1, aux, end)
        else:
            move(begin, end)

    def recursive_1():
        show()
        rec_1(n, 0, 2)
        show()


    if method == "play_game":
        play_game()
    elif method == "recursive_1":
        recursive_1()


if __name__ == '__main__':
    n = int(sys.argv[1])
    if len(sys.argv) == 3:
        method = str(sys.argv[2])
        game(n, method)
    else:
        game(n)

