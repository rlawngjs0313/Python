def inputing():
    data_name = input("데이터 파일 이름을 입력하세요: ")
    if data_name == '':
        inputing()
    return data_name
def line_inputing():
    find_lines = input("검색할 문자열을 입력하세요: ")
    if find_lines == '':
        line_inputing()
    return find_lines
def reading():
    file_name = inputing()
    try:
        print(file_name)
        with open(file_name, "r", encoding="cp949") as f:
            file_data = f.readlines()
            for i in range(0, len(file_data)):
                file_data[i] = file_data[i].strip()
        return file_data
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        exit()
    except UnicodeDecodeError:
        with open(file_name, "r", encoding="utf-8") as f:
            file_data = f.readlines()
            for i in range(0, len(file_data)):
                file_data[i] = file_data[i].strip()
        return file_data
def finding(data, lines):
    result_data = []
    cnt = []
    word = lines
    counting = 0
    for i in data:
        counting += 1
        new_data = str(i)
        locate_word = []
        startPos = 0
        if new_data.find(lines) != -1:
            while True:
                if new_data.find(lines, startPos) != -1:
                    locate_word.append(new_data.find(lines, startPos)+1)
                    startPos += new_data.find(lines, startPos)+1
                else:
                    locate_word = tuple(locate_word)
                    break
            result_data.append(locate_word)
            result_data.append(new_data)
            cnt.append(counting)
    return cnt, result_data, word
# 53:00
result = finding(reading(), line_inputing())
d = {}
for i in range(0, len(result[1]), 2):
    d[result[1][i]] = result[1][i+1]
if d == {}:
    print(f"{result[2]}를 찾을 수 없습니다.")
else:
    for i in range(len(d)):
        print(f"{result[0][i]} : {list(d.keys())[i]} : {list(d.values())[i]}")