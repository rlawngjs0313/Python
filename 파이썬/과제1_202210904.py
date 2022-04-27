import math
#입력
hum = float(input("습도를 입력하십시오: "))
tem = float(input("온도를 입력하십시오: "))
#이슬점 계산
hum_cal = math.log(hum / 100)
tem_cal = (17.62 * tem) / (243.12 + tem)
dew = (243.12 * (hum_cal + tem_cal)) / (17.62 - (hum_cal + tem_cal))
#소수점 버림
dew_cal = float(int(dew * 10) / 10)
#출력
print(dew_cal)