S = sum(list(map(int, input().split())))
T = sum(list(map(int, input().split())))

print(S if S>=T else T)