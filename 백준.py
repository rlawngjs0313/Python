T = 10

for test_case in range(1, T+1):
    N = int(input())
    L1 = list(map(int, input().split()))
    result = 0

    for idx, value in enumerate(L1):
        if value == 0:
            continue
        else:
            if max(L1[idx-2:idx+3]) == value:
                large = max(L1[idx-2:idx+3].remove(value))
                result += value - large
    
    print(f'#{test_case} {result}')