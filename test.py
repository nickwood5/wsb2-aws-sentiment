from multiprocessing import Process

def f(i):
    print('hello world', i)


if __name__ == '__main__':

    for num in range(0, 10):
        Process(target=f, args=[num]).start()