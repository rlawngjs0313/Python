import sys
input = sys.stdin.readline
print = sys.stdout.write

def work(state,Ti,Si,result:list):
    if state == 1:
        result[0] += Ti
        if Si == 'right':
            state = 4
        else:
            state = 2
    elif state == 2:
        result[1] += Ti
        if Si == 'right':
            state = 1
        else:
            state = 3
    elif state == 3:
        result[0] -= Ti
        if Si == 'right':
            state = 2
        else:
            state = 4
    else:
        result[1] -= Ti
        if Si == 'right':
            state = 3
        else:
            state = 1
    return state,result

N, T = map(int, input().split())
result = [0,0]

state = 1
Tii = 0
for _ in range(N):
    Ti, Si = map(str, input().split())
    Ti = int(Ti)
    state, result = work(state,Ti-Tii,Si,result)
    Tii = Ti

_,result = work(state,T-Tii,state,result)
print(f"{result[0]} {result[1]}")