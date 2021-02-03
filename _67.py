import turtle

window = turtle.Screen()

for shape in range(10):
    turtle.right(36)
    for line in range(8):
        turtle.right(45)
        turtle.forward(50)

turtle.exitonclick()
