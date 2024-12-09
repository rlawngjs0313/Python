import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
word = input().rstrip()

prev = 'Q'
result = ''
s,e = 0,0
while N != 0:
    if e+1 < len(word) and word[e+1] in '-0+':
        e += 1
    node = word[s:e+1]
    if s == e:
        node += '0'
    
    if node in 'C+C0C-':
        result += 'B'
    elif node in 'B0B-':
        if prev == 'Q' or prev in 'C+C0C-':
            result += 'D'
        else:
            result += 'B'
    elif node in 'A-B+':
        if prev == 'Q' or prev in 'B0B-C+C0C-':
            result += 'P'
        else:
            result += 'D'
    elif node in 'A0':
        if prev in 'A+A0':
            result += 'P'
        else:
            result += 'E'
    else:
        result += 'E'
    prev = node
    N -= 1
    s,e = e+1,e+1

print(f"{result}\n")