import concurrent.futures
import time


def my_sleep(t: int):
    print("starting sleep for {} secs".format(t))
    time.sleep(t)
    print("done sleeping")


if __name__ == '__main__':
    start_time = time.time()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(my_sleep, [1]*10)

    end_time = time.time()
    print("total execution time = {} secs".format(end_time-start_time))