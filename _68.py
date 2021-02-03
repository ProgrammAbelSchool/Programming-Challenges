import turtle
import random

window = turtle.Screen()

for line in range(random.randint(10, 20)):
    turtle.right(random.randint(0, 360))
    turtle.forward(random.randint(1, 100))

turtle.exitonclick()
