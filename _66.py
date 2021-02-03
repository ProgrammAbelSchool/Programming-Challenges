import turtle
import random

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
window = turtle.Screen()

for i in range(8):
    turtle.color(random.choice(colours))
    turtle.right(45)
    turtle.forward(50)

turtle.exitonclick()
