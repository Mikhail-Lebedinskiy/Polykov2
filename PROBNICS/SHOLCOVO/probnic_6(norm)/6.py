import turtle

turtle.goto(10, 10)

turtle.pendown()

# turtle.setheading(0)
turtle.speed(0.1)

x = 10
for i in range(10 ** 3):
    turtle.forward(10 * x)
    turtle.right(30)
    turtle.left(210)
    turtle.forward(10 * x)
    turtle.left(90)
    turtle.forward(25 * x)
    turtle.left(180)
    turtle.forward(5 * x)
    turtle.right(180)
    turtle.forward(5 * x)
    turtle.left(90)
    turtle.forward(10 * x)
    turtle.left(90)
    turtle.forward(20 * x)
    turtle.forward(5 * x)
    turtle.left(90)
    turtle.forward(10 * x)
    turtle.left(180)
