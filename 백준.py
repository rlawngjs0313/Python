import sys

data = "0b" + sys.stdin.readline().rstrip()
print(oct(int(data, 2)).replace("0o", ""))