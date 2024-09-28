import turtle
import time 

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("lightblue") 

t = turtle.Turtle()
t.hideturtle()
t.speed(2)

def draw_bear(x, y, size, color, thickness):
    # Kepala Beruang
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.pensize(thickness)
    t.begin_fill()
    t.circle(size)  # Kepala berbentuk lingkaran
    t.end_fill()

    # Telinga kiri
    t.penup()
    t.goto(x - size * 0.6, y + size * 1.1)
    t.pendown()
    t.begin_fill()
    t.circle(size * 0.3)
    t.end_fill()

    # Telinga kanan
    t.penup()
    t.goto(x + size * 0.6, y + size * 1.1)
    t.pendown()
    t.begin_fill()
    t.circle(size * 0.3)
    t.end_fill()

    # Mata kiri
    t.penup()
    t.goto(x - size * 0.3, y + size * 0.3)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(size * 0.1)
    t.end_fill()

    # Mata kanan
    t.penup()
    t.goto(x + size * 0.3, y + size * 0.3)
    t.pendown()
    t.begin_fill()
    t.circle(size * 0.1)
    t.end_fill()

    # Hidung
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(size * 0.15)
    t.end_fill()

bears = [
    (0, -150, 100, "#A0522D", 5),
    (-200, -100, 80, "#8B4513", 5),
    (200, -100, 80, "#D2691E", 5),
]

for each_bear in bears:
    draw_bear(*each_bear)
    time.sleep(0.5)

turtle.done()
