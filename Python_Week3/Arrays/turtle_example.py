import turtle
from turtle import *
from random import randint

john = Turtle()
bob = Turtle
sally = Turtle()

john.color("red")
bob.color("blue")
sally.color("green")

john.penup()
john.goto(-160, 100)
john.pendown()

bob.penup()
bob.goto(-160, 70)
bob.pendown()

sally.penup()
sally.goto(-160, 40)
sally.pendown()

for movement in range(100):
    john.forward(randint(1, 5))
    bob.forward(randint(1, 5))
    sally.forward(randint(1, 5))

input("Press enter to exit")
