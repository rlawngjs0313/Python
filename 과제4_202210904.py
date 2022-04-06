def trans_year(id):
    year = id[0:2]
    if year.isdigit() == False:
        print("년도가 숫자로 이루어 지지 않았습니다.")
        return 0
    else:
        year = int(year)
        if year <= 22:
            year += 2000
        else:
            year += 1900
        return year
def year_cal(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0:
        if year % 100 == 0:
            return False
        else:
            return True
    else:
        return False
def trans_month(id):
    month = id[2:4]
    if month.isdigit() == False:
        print("월이 숫자로 이루어 지지 않았습니다.")
        return 0
    else:
        month = int(month)
        if month < 1 or month > 12:
            print("없는 날짜입니다.")
            return 0
    return month
def trans_day(id, year, month):
    day = id[4:6]
    strmonth = str(month)
    _31day = "135781012"
    if year == 0 or month == 0:
        return 0
    elif day.isdigit() == False:
        print("일이 숫자로 이루어 지지 않았습니다.")
        return 0
    else:
        day = int(day)
        if year_cal(year) == True:
            if _31day.find(strmonth) != -1:
                if _31day.find(strmonth) == 8:
                    if day <= 29:
                        return True
                    else:
                        print("없는 날짜입니다.")
                        return 0
                elif day <= 31:
                    return True
                elif day > 31:
                    print("없는 날짜입니다.")
                    return 0
            else:
                if day > 30:
                    print("없는 날짜입니다.")
                    return 0
        else:
            if _31day.find(strmonth) != -1:
                if _31day.find(strmonth) == 8:
                    if day <= 28:
                        return True
                    else:
                        print("없는 날짜입니다.")
                        return 0
                elif day <= 31:
                    return True
                elif day > 31:
                    print("없는 날짜입니다.")
                    return 0
            else:
                if day > 30:
                    print("없는 날짜입니다.")
                    return 0
def iscorrect_7num(id, year):
    seven = id[7]
    year2000 = "34"
    year1900 = "12"
    if seven.isdigit() == False:
        print("성별값이 숫자로 이루어 지지 않았습니다.")
    else:
        intseven = int(seven)
        if intseven > 4:
            print("유효한 성별값이 아닙니다.")
            return 0
        else:
            if year >= 2000:
                if year2000.find(seven) != -1:
                    return True
                else:
                    print("2000년 이후 출생자는 번호가 3 또는 4로 시작함")
                    return 0
            else:
                if year1900.find(seven) != -1:
                    return True
                else:
                    print("1900년 이후 출생자는 번호가 1 또는 2로 시작함")
                    return 0
def isValid(id):
    if len(id) != 14:
        print("주민등록번호의 길이가 맞지 않습니다.")
        return 0
    else:
        if id.find("-") != 6:
            print("'-'의 위치가 잘못 되었습니다.")
            return 0
        else:
            return True
def isValid_RRN(year, month, day, _7num, islencorrect):
    if year == 0 or month == 0 or day == 0 or _7num == 0 or islencorrect == 0:
        print("주민등록번호가 적합하지 않습니다.")
        return 0
    else:
        print("주민등록번호가 적합해 보입니다.")
        return 0

RRN = input("주민등록번호 13자리를 '-'포함해서 입력해주세요. : ")
islencorrect = isValid(RRN)
if islencorrect != 0:
    year = trans_year(RRN)
    month = trans_month(RRN)
    day = trans_day(RRN, year, month)
    _7num = iscorrect_7num(RRN, year)
    isValid_RRN(year, month, day, _7num, islencorrect)
else:
    print("주민등록번호가 적합하지 않습니다.")