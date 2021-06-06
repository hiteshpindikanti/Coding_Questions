import concurrent.futures
import time


def my_sleep(t: int):
    print("starting sleep for {} secs".format(t))
    time.sleep(t)
    print("done sleeping")


def my_print(num: int):
    print('start:', num)
    time.sleep(num)
    print('end:', num)


if __name__ == '__main__':
    # start_time = time.time()
    # for i in range(4, -1, -1):
    #     my_print(i)
    # end_time = time.time()
    # print("total execution time = {} secs".format(end_time - start_time))

    print('-------Now with multiprocessing------')
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        executor.submit(my_print, 1)
        print('now second one')
        time.sleep(1)
        executor.submit(my_print, 2)
        print('now thrid one')
        time.sleep(1)
        executor.submit(my_print, 3)

    end_time = time.time()
    print("total execution time = {} secs".format(end_time - start_time))
