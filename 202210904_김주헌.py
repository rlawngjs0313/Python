#202210904_김주헌_rlawngjs

def readData(filename):
    try:
        with open(filename, "r") as f:
            data = f.readlines()
            dic = {}
            for i in data:
                i = i.strip()
                k = i[:i.find(",")]
                i = i[len(k)+1:]
                v1 = i[:i.find(",")]
                v2 = i[len(v1)+1:]
                dic[k] = [v1, v2]
    except FileNotFoundError:
        print(f"{filename}이 없습니다.")
        exit()
    return dic
def printItem(d, itemName):
    d = dict(d)
    cnt = 0
    for i in d.keys():
        if str(i).find(itemName):
            cnt += 1
            print(f"상품명 : {i}, 분류: {d[i][0]}, 가격: {d[i][1]}")
    if cnt == 0:
        print(f"상품 {itemName}이 없습니다.")
def printCategory(d, category):
    d = dict(d)
    cnt = 0
    category = str(category)
    for i in d.values():
        for j in i:
            if str(i).upper() in category.upper():
                cnt += 1
            print(f"상품명 : {i}, 분류: {d[i][0]}, 가격: {d[i][1]}")
    if cnt == 0:
        print(f"분류항목 {category}이 없습니다.")
def printPriceInRange(d,price1,price2):
    cnt = 0
    for i in d.values():
        for j in i:
            if price1 <= j[1] < price2:
                cnt += 1
            print(f"상품명 : {i}, 분류: {d[i][0]}, 가격: {d[i][1]}")
    if cnt == 0:
        print(f"가격이 {price1} ~ {price2}에 해당되는 물품이 없습니다.")
def main(filename):
    word = input('"명령:데이터" 형태로 입력하세요.: ')
    A = word[:word.find(":")]
    B = word[word.find(":"):]
    if B in "~":
        B1 = B[:B.find("~")]
        B2 = B[B.find("~"):]
        if B1.isdigit() and B2.isdigit():
            printPriceInRange(readData(filename),B1,B2)
        else:
            print("숫자를 입력하세요>")
            exit()
    elif A == "item":
        printItem(readData(filename), B)
    elif A == "category":
        printCategory(readData(filename), B)
main("items.cp949.txt")