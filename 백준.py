A, B, C = list(map(int, input().split()))
if A == B == C:
    print(10000+A*1000)
elif A == B or B == C or A == C:
    if A == B:
        print(1000+A*100)
    elif B == C:
        print(1000+C*100)
    else:
        print(1000+A*100)
else:
    print(max(A,B,C)*100)