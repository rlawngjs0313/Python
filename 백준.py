import sys

data = list(input())
L1 = []
for i in data:
    if i.isalpha():
        sys.stdout.write(i)
    else:
        if i == '(':
            L1.append(i)
        elif i == '*' or i == '/':
            while L1 and (L1[-1] == '*' or L1[-1] =='/'):
                sys.stdout.write(L1.pop())
            L1.append(i)
        elif i == '+' or i == '-':
            while L1 and L1[-1] != '(':
                sys.stdout.write(L1.pop())
            L1.append(i)
        elif i == ')':
            while L1 and L1[-1] != '(':
                sys.stdout.write(L1.pop())
            L1.pop()
while L1 :
    sys.stdout.write(L1.pop())