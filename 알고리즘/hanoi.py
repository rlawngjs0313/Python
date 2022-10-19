def hano(n, f, t, a):
    if n == 1:
        L1.append(f"{f} -> {t}")
        return
    hano(n-1, f, a, t)
    L1.append(f"{f} -> {t}")
    hano(n-1, a, t, f)
L1 = []
N = int(input())
hano(N, 1, 3, 2)
print(f"n = {N}")
print('\n'.join(L1))