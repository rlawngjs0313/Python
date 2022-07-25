import sys

data = sys.stdin.readline().rstrip()
result = []
temp = ""
isTag = False

for i in data:
    if isTag:
        if i == ">":
            temp += i
            result.append(temp)
            isTag = False
            temp = ""
            continue
        else:
            temp += i
    elif i == "<":
        if temp:
            result.append(temp)
            temp = "<"
            isTag = True
            continue
        else:
            temp += i
            isTag = True
    elif i == " " and temp:
        result.append(temp)
        temp = ""
        continue
    else:
        temp += i
if temp:
    result.append(temp)

for i in range(len(result)):
    if "<" in result[i]:
        sys.stdout.write(str(result[i]))
        isTag = True
    else:
        temp = list(result[i])
        temp.reverse()
        if isTag:
            sys.stdout.write(str(temp).replace("[", "").replace("]", "").replace(", ", "").replace("'", ""))
            isTag = False
        else:
            if i == 0:
                sys.stdout.write(str(temp).replace("[", "").replace("]", "").replace(", ", "").replace("'", ""))
            else:
                sys.stdout.write(" " + str(temp).replace("[", "").replace("]", "").replace(", ", "").replace("'", ""))