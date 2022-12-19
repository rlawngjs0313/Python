import sys
sys.setrecursionlimit(100000)

def solution(L1:list) -> list:
    sL1, sL2, sL3, sL4 = [], [], [], []
    isProblem = False
    for i in range(len(L1)//2):
        sL1.append(L1[i][:len(L1)//2])
        sL2.append(L1[len(L1)//2 + i][:len(L1)//2])
        sL3.append(L1[i][len(L1)//2:])
        sL4.append(L1[len(L1)//2 + i][len(L1)//2:])

    for i in range(len(L1)):
        if i == 0 and (1 in L1[i] and 0 in L1[i]):
            isProblem = True
            solution(sL1)
            solution(sL2)
            solution(sL3) 
            solution(sL4)
            break
        elif i > 0 and L1[i-1] != L1[i]:
            isProblem = True
            solution(sL1)
            solution(sL2)
            solution(sL3) 
            solution(sL4)
            break
    
    if not isProblem:
        result[L1[0][0]] += 1
        return 0

N = int(input())
L1 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = [0, 0]

solution(L1)
print(f"{result[0]}\n{result[1]}")