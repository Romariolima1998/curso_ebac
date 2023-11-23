import threading
import time
import multiprocessing

# single thread


def new():
    for x in range(6):
        print('single thread')


t1 = threading.Thread(target=new)

t1.start()
t1.join()
print('sucess')

print('-----------------------------------------')

# multithreads


def calc_square(nambers):
    print('cauculate square nambers')
    for i in nambers:
        time.sleep(2)
        print(f'square {i * i}')


def calc_cube(nambers):
    print('cauculate cube numbers: ')
    for i in nambers:
        time.sleep(2)
        print(f'cube: {i * i * i}')


if __name__ == '__main__':
    arr = [2, 3, 8, 9]
    t1 = threading.Thread(target=calc_cube, args=(arr,))
    t2 = threading.Thread(target=calc_square, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('main thread here')
    print('sucess')

print('---------------------------------')

results = []


def calc_square(numbers):
    global results
    for i in numbers:
        print(f'square: {i * i}')
        results.append(i * i)
        print(f'witnin a result: {results}')


def calc_cube(numbers):
    for i in numbers:
        time.sleep(3)
        print(f'cube: {i* i * i}')


if __name__ == '__main__':
    arr = [2, 3, 8, 9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p1.start()
    p1.join()
    print('sucess')