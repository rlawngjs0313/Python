with open("MP09Data1.txt", "r") as f:
    data_1 = f.readlines()
with open("MP09Data2.txt", "r") as f:
    data_2 = f.readlines()
data = data_1 + data_2
for i in range(len(data)):
    for j in range(i+1,len(data)):
        if float(data[i]) < float(data[j]):
            num = float(data[i])
            data[i] = float(data[j])
            data[j] = num
        else:
            data[i] = float(data[i])
for k in data:
    print(k)