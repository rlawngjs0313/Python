from collections import defaultdict

N = int(input())
S = input()
D1 = defaultdict(int)
for i in range(N//2):
    D1[S[i]] += 1
    D1[S[-i-1]] += 1
for i in D1.values():
    if i%2 != 0:
        print("No")
        break
else:
    print("Yes")