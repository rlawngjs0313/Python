import random
import time

def generate(n):
    a = []
    for i in range(n):
        a.append(random.randrange(0, 1000))
    return a

def bubble(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

array1 = random.sample(range(1, 1000), 100)
array2 = generate(100)

print(array1)
start = time.time()
print(bubble(array1))
print("time: ", time.time() - start)

print(array2)
start = time.time()
print(bubble(array2))
print("time: ", time.time() - start)