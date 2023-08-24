
from threading import *
import queue

def functionA(listArgumen):
    for i in range(1, 50):
        print('A')

    return listArgumen[0] + listArgumen[1]

def functionB(listArgumen):
    for i in range(1, 50):
        print('B')

    return listArgumen[0] * listArgumen[1]

def main():
    queT1 = queue.Queue()
    queT2 = queue.Queue()
    t1 = Thread(target=lambda q, arg1: q.put(functionA(arg1)), args=(queT1, [2, 3]))
    t1.start()
    t2 = Thread(target=lambda q, arg1: q.put(functionB(arg1)), args=(queT2, [2, 3]))
    t2.start()
    t1.join()
    t2.join()

    print('Hasil Thread 1 : ' + str(queT1.get()))
    print('Hasil Thread 2 : ' + str(queT2.get()))


main()  # Ngeprint huruf A dan B akan berbarengan