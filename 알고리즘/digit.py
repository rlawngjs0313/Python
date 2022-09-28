b = int(input("입력진수 결정(16/10/8/2): "))
data = input("값 입력: ")
if b == 16:
    data = int(data, 16)
if b == 10:
    data = int(data, 10)
if b == 8:
    data = int(data, 8)
if b == 2:
    data = int(data, 2)

print(f"16진수 ==> {hex(data)}")
print(f"10진수 ==> {data}")
print(f"8진수 ==> {oct(data)}")
print(f"2진수 ==> {bin(data)}")
