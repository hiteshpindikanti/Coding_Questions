import time

start = time.time()
with open('words_alpha.txt') as file:
    s = file.read()
    for line in s.split('\n'):
        if line == "ant":
            print("FOUND")
            break
end = time.time()
print("TimeTaken={}".format(end-start))

start = time.time()
with open('words_alpha.txt') as file:
    for line in file:
        if line == "ant":
            print("FOUND")
            break
end = time.time()
print("TimeTaken={}".format(end-start))
