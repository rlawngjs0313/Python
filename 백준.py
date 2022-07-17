while True:
    data = input()
    index = len(data) // 2
    result = ""
    if len(data) % 2 == 0:
        S1 = list(map(str, data[index:]))
        S1.reverse()
        for i in S1:
            result += i
        if data[:index] == result:
            print("yes")
            continue
        else:
            print("no")
            continue
    S1 = list(map(str, data[index:]))
    S1.reverse()
    for i in S1:
        result += i
    if data == '0':
        break
    if data[0:index+1] == result:
        print("yes")
    else:
        print("no")