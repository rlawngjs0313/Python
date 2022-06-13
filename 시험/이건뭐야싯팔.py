def readFileData(filename):
    lst = []
    try:
        f = open(filename)
        lst = f.readlines()
        f.close()
    except UnicodeDecodeError:
        f = open(filename, encoding="utf-8")
        lst = f.readlines()
        f.close()
    except FileNotFoundError:
        print(filename, "을 찾을 수 없습니다.")
        exit()
    for i in range(len(lst)):
        lst[i] = lst[i].strip()
    return lst
def createLocation(line, findStr):
    tpl = ()
    acc = 0
    n = line.find(findStr)
    while n != -1:
        tpl = tpl + (acc + (n + 1), )
        acc += (n+len(findStr))
        line = line[n + len(findStr):]
        n = line.find(findStr)
    return tpl
fileName = input("데이터 파일 이름을 입력하세요: ")
while len(fileName) == 0:
    fileName = input("데이터 파일 이름을 입력하세요: ")
lst = readFileData(fileName)
str = input("검색할 문자열을 입력하세요: ")
while len(str) == 0:
    str = input("검색할 문자열을 입력하세요: ")
d = {}
for i in range(len(lst)):
    tpl = createLocation(lst[i], str)
    if tpl != ():
        print(f"{i+1} : {tpl} : {lst[i]}")
        d[tpl] = lst[i]