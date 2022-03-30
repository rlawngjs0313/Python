year = int(input("년도를 입력하십시오 : "))
month_input = int(input("월을 입력하십시오 : "))
day_input = int(input("일을 입력하십시오 : "))
DayOfYear = 0

if year % 400 == 0 :
    print(year, "는 윤년입니다.")
elif year % 4 == 0 :
    if year % 100 == 0 :
        print(year, "는 윤년이 아닙니다.")
    else :
        print(year, "는 윤년입니다.")

DayOfYear = 