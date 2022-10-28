import sys

def three(idx): # 3개 묶어서 사기
    global result
    temp = min(data[idx: idx + 3])
    data[idx:idx+3] = [data[idx]-temp, data[idx+1]-temp, data[idx+2]-temp]
    result += 7 * temp


def two(idx): # 2개 묶어서 사기
    global result
    temp = min(data[idx: idx + 2])
    data[idx:idx+2] = [data[idx]-temp, data[idx+1]-temp]
    result += 5 * temp


def one(idx): # 1개 사기
    global result
    result += 3 * data[idx]


N = int(input())
L1 = [0 for _ in range(N)]
data = list(map(int, sys.stdin.readline().split())) + [0, 0]
result = 0

for i in range(N):
    if data[i+1] > data[i+2]: # 만약 2번째가 3번째보다 크면
        temp = min(data[i], data[i+1] - data[i+2])          #
        data[i:i+2] = [data[i]-temp, data[i+1]-temp]        # 2개 먼저 묶어서 사기
        result += 5 * temp                                  #
        three(i)    # 그 다음에 3개 묶어서 사기
    else:   # 그 이외에는
        three(i)    # 3개 먼저 묶어서 사고
        two(i)  # 2개 묶어서 사기
    one(i)  # i에 존재하는 갯수 사기
    if data == L1: # 만약 다 샀다면
        break   # 빠르게 종료
print(result)