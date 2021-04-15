import random

n = 10 ** 7
circle_points = 0
total_points = n

for _ in range(n):
    x, y = (random.random(), random.random())
    if (x-0.5) ** 2 + (y-0.5) ** 2 < 0.25:
        circle_points += 1

print(circle_points)
print("Pi = {}".format(format(4*(circle_points/total_points), '.3f')))
