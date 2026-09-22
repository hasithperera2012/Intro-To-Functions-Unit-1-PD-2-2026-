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
rotate = 110
def square(x,y):
    for i in range(5):
        t.forward(x)
        t.left(y)
square(100,36)

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
        length += 67
addSquares(1000)

# def star(x,y):
#     for i in range(100):
#         t.forward(x)
#         t.left(y)
# star(110,145)

# def addStars(iRange):
#     lenght = 25
#     for i in range(iRange):
#         star((lenght + 1, 100))
# addStars(100000)

turtle.done