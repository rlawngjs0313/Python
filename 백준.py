A, B = list(map(int, input().split()))
C = int(input())

if B+C < 60:
    print(f"{A} {B+C}")
else:
    if A+(B+C)//60 >= 24:
        print(f"{(A+(B+C)//60)%24} {(B+C)-60*((B+C)//60)}")
    else:
        print(f"{A+(B+C)//60} {(B+C)-60*((B+C)//60)}")