import random
import time

def bubble(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def find(r, v):
    for i in range(len(r)):
        if v < r[i]:
            return i
    return len(r)

def ins_sort1(a:list) -> list:
    result = []
    while len(a):
        value = a.pop(0)
        ins_idx = find(result, value)
        result.insert(ins_idx, value)
    return result

def ins_sort2(a:list):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key

def find_min(a:list):
    min_idx = 0
    for i in range(1, len(a)):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort1(a:list):
    result = []
    while a:
        min_idx = find_min(a)
        value = a.pop(min_idx)
        result.append(value)
    return result

def sel_sort2(a:list):
    for i in range(len(a)-1):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

L1 = random.sample(range(1, 100000), 10000)

start = time.time()
bubble(L1)
print("bubble sort time: ", time.time() - start)

start = time.time()
ins_sort1(L1)
print("insert sort(1) time: ", time.time() - start)

start = time.time()
ins_sort2(L1)
print("insert sort(2) time: ", time.time() - start)

start = time.time()
sel_sort1(L1)
print("select sort(1) time: ", time.time() - start)

start = time.time()
sel_sort2(L1)
print("select sort(2) time: ", time.time() - start)

start = time.time()
L1.sort()
print("python sort time: ", time.time() - start)