list_data = []
a = 0
with open("MP08data.txt", "r", encoding="euckr") as f:
    data = f.readlines()

for i in range(0, data.count("사각형\n")+data.count("삼각형\n")+data.count("원\n")):
    list_data.append(data[a])
    if data[a] == "사각형\n":
        t = tuple(data[a+1:a+5])
        list_data.append(t)
        a += 5
    elif data[a] == "삼각형\n":
        t = tuple(int(data[a+1:a+7]))
        list_data.append(t)
        a += 7
    elif data[a] == "원\n":
        t = tuple(data[a+1:a+4])
        list_data.append(t)
        a += 4

print(list_data)