import sys

word = sys.stdin.readline().rstrip()

last = word[0]
result = 1
if word[0] == 'c':
    result *= 26
else:
    result *= 10
for i in range(1, len(word)):
    if last == word[i]:
        if word[i] == 'c':
            result *= 25
        else:
            result *= 9
    else:
        if word[i] == 'c':
            result *= 26
        else:
            result *= 10
    last = word[i]
    result %= 1000000009

sys.stdout.write(f"{result}")