name = []
tel = []

def print_title():
    print("=" * 28)
    print("=" * 8, "전화번호부", "=" * 8)
    print("=" * 28)

def print_menu():
    L1 = ["1. 연락처 추가", "2. 연락처 수정", "3. 연락처 출력", "4. 연락처 삭제", "5. 종료"]
    for i in L1:
        print(i)
    return int(input("원하는 번호를 선택하세요: "))

def add():
    name.append(input("이름: "))
    tel.append(input("전화번호: "))

def updata(n, t):
    for i in range(len(name)):
        if name[i] == n:
            tel[i] = t
            return True
    return False

def print_tel():
    for i in range(len(name)):
        print("이름: ", name[i])
        print("전화번호: ", tel[i])

def delete(n):
    for i in range(len(name)):
        if name[i] == n:
            del(name[i])
            del(tel[i])
            return True
    return False

def print_end():
    print("=" * 28)

while True:
    print_title()
    menu = print_menu()
    if menu == 1:
        add()
        print_tel()
    elif menu == 2:
        print_tel()
        n = input("수정하고 싶은 이름을 입력하세요: ")
        t = input("전화번호: ")
        if updata(n,t) == True:
            print(n, "의 전화번호를 수정하였습니다.")
        else:
            print(n, "는(은) 존재하지 않습니다.")
        print_tel()
    elif menu == 3:
        print_tel()
    elif menu == 4:
        print_tel()
        n = input("삭제하고 싶은 이름을 입력하세요: ")
        if delete(n):
            print(n, "를(을) 삭제하였습니다.")
        else:
            print(n, "는(은) 존재하지 않습니다.")
        print_tel()
    elif menu == 5:
        print_end()
        break