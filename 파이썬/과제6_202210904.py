import math

shape_list = ["",(),"",(),"",(),"",(),"",()]
for i in range(0, 10, 2):
    shape_list[i] = input("도형의 종류를 입력하시오: ")
    if shape_list[i] == "사각형":
        x1 = int(input("x1 좌표를 입력하시오: "))
        y1 = int(input("y1 좌표를 입력하시오: "))
        x2 = int(input("x2 좌표를 입력하시오: "))
        y2 = int(input("y2 좌표를 입력하시오: "))
        shape_list[i+1] = (x1, y1, x2, y2)
        print(f"{shape_list[i]}의 면적은 {(x2-x1)*(y2-y1)}입니다.")
        #밑변 x 높이
    if shape_list[i] == "삼각형":
        x1 = int(input("x1 좌표를 입력하시오: "))
        y1 = int(input("y1 좌표를 입력하시오: "))
        x2 = int(input("x2 좌표를 입력하시오: "))
        y2 = int(input("y2 좌표를 입력하시오: "))
        x3 = int(input("x3 좌표를 입력하시오: "))
        y3 = int(input("y3 좌표를 입력하시오: "))
        shape_list[i+1] = (x1, y1, x2, y2, x3, y3)
        a1 = math.sqrt(((x2-x1)**2+(y2-y1)**2))
        a2 = math.sqrt(((x3-x2)**2+(y3-y2)**2))
        a3 = math.sqrt(((x3-x1)**2+(y3-y1)**2))
        print(f"{shape_list[i]}의 면적은 {(a1+a2+a3)/2}")
        # 헤론의 공식 S = (a+b+c) / 2
    if shape_list[i] == "원":
        x = int(input("x 좌표를 입력하시오: "))
        y = int(input("y 좌표를 입력하시오: "))
        r = int(input("반지름을 입력하시오: "))
        shape_list[i+1] = (x, y, r)
        print(f"{shape_list[i]}의 면적은 {math.pi*r**2}")
        # 파이 x r^2