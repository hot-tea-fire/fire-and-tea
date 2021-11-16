import concurrent.futures
import time

nums = {1: 'a', 3: 'i'}


def fib(item):
    print(item)

    time.sleep(1)


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as e:
        for i in range(5):
            e.submit(fib, i)


if __name__ == '__main__':
    main()
