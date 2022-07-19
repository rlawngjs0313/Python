data = input().split("-")
result1 = 0
result2 = 0

if len(data) == 1:
    data = list(map(int, data[0].split("+")))
    for i in data:
        result1 += i
    print(result1)
else:
    data1 = list(map(int, data[0].split("+")))
    for i in data1:
        result1 += i
    for i in range(len(data[1:])):
        data[i+1] = sum(list(map(int, data[i+1].split("+"))))
    result2 = sum(data[1:])
    data.clear()
    data.append(str(result1-result2))
    print(data[0])