import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
t.speed(10000)
# t.forward(400)

# def message(input):
#     print(input)
# message("Hello World")

# t.shape('turtle')
# t.speed(10)
# t.forward(300)
# t.left(90)
# t.forward(300)
# t.left(90)
# t.forward(300)
# t.left(90)
# t.forward(300)
# t.left(90)

# def equal(x):
#     t.forward(x)
#     t.left(120)
#     t.forward(x)
#     t.left(120)
#     t.forward(x)
#     t.left(120)
# equal(400)

# def equal(x):
#     t.forward(x)
#     t.left(120)
#     t.forward(x)
#     t.left(120)
#     t.forward(x)
# equal(200)

# def right():
#     t.forward(100)
#     t.left(90)
#     t.forward(100)
#     t.left(135)
#     t.forward(142)
# right()


# for i in range(3):
#     print(i)

# for i in range(4):
#     t.forward(100)
#     t.left(90)

# for i in range(60):
#     t.forward(200)
#     t.left(91)
#     t.forward(200)
#     t.left(91)
#     t.forward(200)
#     t.left(91)
#     t.forward(200)
#     t.left(95)

sidelength = 100
rotate = 90
def square(x,y):
    for i in range(100):
        t.forward(x)
        t.left(y)
square(101,91)

# def doubleSquares(iRange):
#     length = 25
#     for i in range(iRange):
#         square(length, 90)
#         length = length * 2
# doubleSquares(100)

def addSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length += 25
addSquares(5)

turtle.done