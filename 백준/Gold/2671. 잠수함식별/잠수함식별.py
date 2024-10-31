import sys, re
input = sys.stdin.readline
print = sys.stdout.write

pattern = re.compile(r'(100+1+|01)+')
word = input().rstrip()
matching = pattern.fullmatch(word)

if matching:
    print("SUBMARINE\n")
else:
    print("NOISE\n")