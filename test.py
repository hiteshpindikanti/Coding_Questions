def say_hello_5_times():
    for _ in range(5):
        print("hello : {}".format(__name__))


# say_hello_5_times()
print("Name: {}".format(__name__))

if __name__ == "__main__":
    say_hello_5_times()