import turtle
# making basic shape

wn = turtle.Screen()
wn.bgcolor("light blue")

skk = turtle.Turtle()
# just normal line
# skk.forward(100)


# making square
# wn.title("Square")
# for i in range(4):
#     skk.forward(50)
#     skk.right(90)
# turtle.done()

# Star
# star = turtle.Turtle()
# star.right(75)
# star.forward(100)
# for i in range(4):
#     star.right(144)
#     star.forward(100)
# turtle.done()

# Spiral  Helix Pattern
loadWindow = turtle.Screen()
turtle.speed(50)
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
for i in range(100):
    t.pencolor(colors[i % 6])
    t.circle(5 * i)
    t.circle(-5 * i)
    t.left(i)

t.exitonclick()

# Rainbow Benzene
# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
# t = turtle.Pen()
# turtle.bgcolor('black')
# for x in range(360):
#     t.pencolor(colors[x%6])
#     t.width(x//100 + 1)
#     t.forward(x)
#     t.left(59)
#
# turtle.done()