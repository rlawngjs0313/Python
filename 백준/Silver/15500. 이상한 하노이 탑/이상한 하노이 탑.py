import sys

K = int(input())
L1 = list(map(int, input().split()))
L2 = []

result = 0
result_list = []
while K != 0:
    if L1.count(K) != 0:
        for i in range(len(L1)-1,-1,-1):
            if L1[i] != K:
                L2.append(L1[i])
                result_list.append("1 2")
                result += 1
            else:
                L1 = L1[:i]
                result_list.append("1 3")
                result += 1
                break
    else:
        for i in range(len(L2)-1,-1,-1):
            if L2[i] != K:
                L1.append(L2[i])
                result_list.append("2 1")
                result += 1
            else:
                L2 = L2[:i]
                result_list.append("2 3")
                result += 1
                break
    K -= 1

print(result)
for i in result_list:
    sys.stdout.write(f"{i}\n")