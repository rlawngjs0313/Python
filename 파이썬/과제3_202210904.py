year = int(input("년도를 입력하십시오 : "))
month_input = int(input("월을 입력하십시오 : "))
day_input = int(input("일을 입력하십시오 : "))
DayOfYear = 0

if year % 400 == 0 :
    print(year, "는 윤년입니다.")
    if month_input >= 3 :
        DayOfYear += 1
elif year % 4 == 0 :
    if year % 100 == 0 :
        print(year, "는 윤년이 아닙니다.")
    else :
        print(year, "는 윤년입니다.")
        if month_input >= 3 :
            DayOfYear += 1
else :
    print(year, "는 윤년이 아닙니다.")

for i in range(1, month_input) :
    if i % 2 == 0 :
        if i == 2 :
            DayOfYear += 28
        else :
            if i >= 8 :
                DayOfYear += 31
            else :
                DayOfYear += 30
    else :
        if i >= 8 :
            DayOfYear += 30
        else :
            DayOfYear += 31
DayOfYear += day_input

print("통일 : ", DayOfYear)