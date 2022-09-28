L1 = [500, 100, 50, 10]
data = int(input("교환할 돈은 얼마인가요?: "))
for i in L1:
    j = data // i
    data %= i
    print(f"{i}원 ==> {j}개")
print(f"바꾸지 못한 잔돈 ==> {data}원")
