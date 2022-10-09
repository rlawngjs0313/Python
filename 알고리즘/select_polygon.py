from curses import init_pair
import turtle


turtle.shape("turtle")
select = int(input("그리고 싶은 도형을 선택하세요 (1:삼각형, 2:사각형, 3:원) >>> "))

if select == 1:
    for _ in range(3):
        turtle.forward(100)
        turtle.right(120)
elif select == 2:
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
else:
    turtle.circle(50)

turtle.done()