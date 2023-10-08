from multiprocessing import Process, cpu_count
import time


def count(num):
    count = 0
    while count < num:
        count += 1


def main():

    print(cpu_count())

    a = Process(target=count, args=(250000000,))
    b = Process(target=count, args=(250000000,))
    c = Process(target=count, args=(250000000,))
    d = Process(target=count, args=(250000000,))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    print('finished in: ', time.process_time(), ' sec')

if __name__ == '__main__':
    main()
