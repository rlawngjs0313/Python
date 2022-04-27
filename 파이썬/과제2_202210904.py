#계산
def cal (A, B) :
    return A + (B / 10) * 3800 + (B / 40) * 18320

#입력
A_dist = float(input("A 쇼핑몰까지의 거리는? : "))
A_com = float(input("A 쇼핑몰의 컴퓨터 가격은? : "))
A_cal = cal(A_com, A_dist)
print("A 쇼핑몰의 전체비용은", A_cal, "입니다.")

B_dist = float(input("B 쇼핑몰까지의 거리는? : "))
B_com = float(input("B 쇼핑몰의 컴퓨터 가격은? : "))
B_cal = cal(B_com, B_dist)
print("B 쇼핑몰의 전체비용은 ", B_cal,"입니다.")

online_com = float(input("온라인 컴퓨터 가격은? : "))
online_deli = float(input("택배 비용은? : "))
online_cal = online_com + online_deli
print("온라인 쇼핑몰의 전체비용은", online_cal, "입니다.")

#비교
min_cal = min(A_cal, B_cal, online_cal)
if A_cal == online_cal or B_cal == online_cal or A_cal == B_cal == online_cal :
    print("온라인 쇼핑몰에서 구입하는 것이 좋습니다.")
elif min_cal == A_cal :
    print("A 쇼핑몰에서 구입하는 것이 좋습니다.")
elif min_cal == B_cal :
    print("B 쇼핑몰에서 구입하는 것이 좋습니다.")
elif min_cal == online_cal :
    print("온라인 쇼핑몰에서 구입하는 것이 좋습니다.")