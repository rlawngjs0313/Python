import turtle

turtle.title('무지개 빛 다각형 그리기')
turtle.shape('turtle')
turtle.speed(10)

while True:
    side = int(input("몇각형을 그리겠습니까?: "))
    turtle.clear()
    if side == 0:
        break


dist = 0
angle = 360 / side

for dist in range(10, 71, 10):
    if dist == 10:
        turtle.pencolor('red')
    elif dist == 20:
        turtle.pencolor('orange')
    elif dist == 30:
        turtle.pencolor('yellow')
    elif dist == 40:
        turtle.pencolor('green')
    elif dist == 50:
        turtle.pencolor('blue')
    elif dist == 60:
        turtle.pencolor('navyblue')
    elif dist == 70:
        turtle.pencolor('purple')
    for i in range(side):
        turtle.forward(dist)
        turtle.right(angle)
turtle.done()