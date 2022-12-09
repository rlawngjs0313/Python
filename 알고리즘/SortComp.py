import sys
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
Testset = ["bubble sort time: ", "insert sort(1) time: ", "insert sort(2) time: ", "select sort(1) time: ", "select sort(2) time: ", "python sort time: "]
Testdef = [bubble(L1), ins_sort1(L1), ins_sort2(L1), sel_sort1(L1), sel_sort2(L1), L1.sort()]

for i, j in zip(Testset, Testdef):
    start = time.time()
    j
    print(i, time.time() - start)