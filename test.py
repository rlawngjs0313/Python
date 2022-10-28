import sys

queue = []
data = sys.stdin.readline()

for i in data:
    try:
        if i in "[{(":
            queue.append(i)
        elif i == ')' and queue[-1] == '(':
            queue.pop()
        elif i == '}' and queue[-1] == '{':
            queue.pop()
        elif i == ']' and queue[-1] == '[':
            queue.pop()
    except:
        print("False")
        exit()
if queue != []:
    print("False")
else:
    print("True")