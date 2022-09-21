import turtle

turtle.title("거북이 오각형 그리기")
turtle.shape("turtle")

A = 72
d = 100

for _ in range(5):
    turtle.forward(d)
    turtle.right(A)
turtle.done()