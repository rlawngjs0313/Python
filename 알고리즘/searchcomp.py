import random
import time

def gen(list, n):
    for i in range(n):
        list.append(random.randrange(0, 100))

def binary(a, x):
    start = 0
    end = len(a) - 1
    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def linear(a, x):
    n = len(a)
    for i in range(n):
        if x == a[i]:
            return i
    return -1

v = []

gen(v, 1000000)
v.sort()

start = time.time()
print(linear(v, 15))
print(linear(v, 45))
print(linear(v, 200))
print("time: ", time.time() - start)

start = time.time()
print(binary(v, 15))
print(binary(v, 45))
print(binary(v, 200))
print("time: ", time.time() - start)