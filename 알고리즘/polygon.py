import turtle

turtle.title('다각형 그리기')
turtle.shape('turtle')

def draw(num) :
    dist = 100
    angle = 360/num

    for i in range (0, num) :
        turtle.forward(dist)
        turtle.right(angle)

n = int(input('몇각형을 그리시겠습니까? : '))

draw(n)

turtle.done()