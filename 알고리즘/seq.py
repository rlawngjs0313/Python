def serch(a, x):
    alist = []
    for i in range(len(a)):
        if x == a[i]:
            alist.append(i)
            return alist
    return -1

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(serch(v, 92))