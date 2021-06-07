from concurrent.futures import ThreadPoolExecutor
from time import sleep, time


# class Debounced:
#     lock = False
#
#     def __init__(self, function, time_limit):
#         self.function = function
#         self.time = time_limit
#
#     def my_fun(self):
#         start = time()
#         if Debounced.lock == 0:
#             Debounced.lock = True
#             self.function()
#             sleep(self.time - (time()-start))
#             Debounced.lock = False


def debounced(time_limit):
    lock = False

    def wrapper_fun(function):
        def inner():
            start = time()
            nonlocal lock
            if not lock:
                lock = True
                function()
                sleep(time_limit - (time()-start))
                lock = False
        return inner
    return wrapper_fun


@debounced(0.5)
def fun():
    print("Hello World")


if __name__ == '__main__':
    ThreadPoolExecutor().submit(fun)
    ThreadPoolExecutor().submit(fun)
    ThreadPoolExecutor().submit(fun)
    ThreadPoolExecutor().submit(fun)
    sleep(2)
    ThreadPoolExecutor().submit(fun)
    ThreadPoolExecutor().submit(fun)
    sleep(1)
    ThreadPoolExecutor().submit(fun)

    # obj = Debounced(fun, 1)
    # with ThreadPoolExecutor() as executor:
    #     executor.submit(obj.my_fun)
    #     executor.submit(obj.my_fun)
    #     executor.submit(obj.my_fun)
    #     executor.submit(obj.my_fun)
    #     sleep(2)
    #     executor.submit(obj.my_fun)
    #     executor.submit(obj.my_fun)
    #     sleep(1)
    #     executor.submit(obj.my_fun)
    #     executor.submit(obj.my_fun)
