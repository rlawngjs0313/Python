import sys

T = int(input())

for i in range(T):
    N = int(sys.stdin.readline())
    data = []
    result = 1
    for j in range(N):
        data.append(list(map(int, sys.stdin.readline().split())))
    data.sort(key=lambda x: (x[0]))
    last = 0
    for j in range(N-1):
        if data[j+1][1] < data[last][1]:    # 1차 점수로 정렬 한뒤, 2차 점수를 비교 / 만약 점수가 낮다면 둘 다 떨어지니 불합
            last = j + 1                    # 합격했다면 비교 점수를 그 점수로 설정 / 이 점수보다 떨어진다면 둘 다 떨어지는 경우
            result += 1
    print(result)