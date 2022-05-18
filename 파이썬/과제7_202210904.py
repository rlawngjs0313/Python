import math

list_data = []
S_list = []
a = 0
# 리스트 생성, 변수 초기화
with open("MP08data.txt", "r", encoding="euckr") as f:
    data = f.readlines()
    for i in range(0, len(data)):
        data[i] = data[i].strip()
# 파일 읽어와서 줄별로 리스트로 생성, 뒤에 줄바꿈, 공백 제거
for i in range(0, data.count("사각형")+data.count("삼각형")+data.count("원")):
    list_data.append(data[a])
    if data[a] == "사각형":
        t = tuple(data[a+1:a+5])
        list_data.append(t)
        S_list.append(data[a])
        s = (int(t[0])-int(t[2]))*(int(t[1])-int(t[3]))
        if s < 0:
            s = s*-1
        S_list.append(s)
        a += 5
    elif data[a] == "삼각형":
        t = tuple(data[a+1:a+7])
        list_data.append(t)
        S_list.append(data[a])
        a1 = math.sqrt(((int(t[2])-int(t[0]))**2+(int(t[3])-int(t[1]))**2))
        a2 = math.sqrt(((int(t[4])-int(t[2]))**2+(int(t[5])-int(t[3]))**2))
        a3 = math.sqrt(((int(t[4])-int(t[0]))**2+(int(t[5])-int(t[1]))**2))
        s = (a1+a2+a3)/2
        if s < 0:
            s = s*-1
        S_list.append(s)
        a += 7
    elif data[a] == "원":
        t = tuple(data[a+1:a+4])
        list_data.append(t)
        S_list.append(data[a])
        s = math.pi*int(t[2])**2
        if s < 0:
            s = s*-1
        S_list.append(s)
        a += 4
print(S_list)