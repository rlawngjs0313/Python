try:
    while True:
        data = input()
        result = [0] * 4
        for i in data:
            if 'A'<=i<='Z':
                result[1] += 1
            elif 'a'<=i<='z':
                result[0] += 1
            elif i.isnumeric():
                result[2] += 1
            elif i == " ":
                result[3] += 1
        print(*result)
except:
    exit()