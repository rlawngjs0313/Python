A, B = list(map(int, input().split()))
if B >= 45:
    print(f"{A} {B-45}")
else:
    if A == 0:
        print(f"{24-(A+1)} {50-(35-B)}")
    else:
        print(f"{A-1} {50-(35-B)}")