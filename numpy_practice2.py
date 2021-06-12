import numpy as np
from time import time as get_current_time

v = np.random.randint(0, 100, 10 ** 4)

start = get_current_time()
v + 1
end = get_current_time()
print(f'Time for np: {end - start} secs')

start = get_current_time()
_ = [i + 1 for i in v]
end = get_current_time()
print(f'Time for list comprehension: {end - start} secs')

start = get_current_time()
res = []
for i in v:
    res.append(v + 1)
end = get_current_time()
print(f'Time for for loop: {end - start} secs')

start = get_current_time()
res = []
i = 0
while i < len(v):
    res.append(v[i])
    i += 1
end = get_current_time()
print(f'Time for while loop: {end - start} secs')

start = get_current_time()
list(map(lambda x: x + 1, v))
end = get_current_time()
print(f'Time for map: {end - start} secs')
