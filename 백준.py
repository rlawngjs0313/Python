import sys

data = "0o" + sys.stdin.readline().rstrip()
print(bin(int(data, 8)).replace("0b", ""))