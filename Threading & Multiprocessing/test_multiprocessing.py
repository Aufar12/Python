from multiprocessing import Process
import time


def print_func(name, tes_arg):
    print('The name of continent is : ', name,tes_arg)

if __name__ == "__main__":  # confirms that the code is under main function
    start_time_multiprocess = time.time()
    names = ['America', 'Europe', 'Africa'] * 100
    procs = []

    # proc = Process(target=print_func)  # instantiating without any argument
    # procs.append(proc)
    # proc.start()

    # instantiating process with arguments
    for name in names:
        # print(name)
        proc = Process(target=print_func, args=(name,'aaa'))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()

    end_multiprocess = time.time() - start_time_multiprocess

    basic = time.time()

    for name in names:
        print_func(name, 'aaa')

    print("--- %s seconds ---" % (time.time() - basic))
    print("--- %s seconds ---" % (end_multiprocess))