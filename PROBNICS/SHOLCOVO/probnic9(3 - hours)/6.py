import turtle

x = 20
for i in range(7):
    turtle.speed(2)
    turtle.right(90)
    turtle.forward(4 * x)
    for j in range(2):
        turtle.right(270)
        turtle.forward(3 * x)
