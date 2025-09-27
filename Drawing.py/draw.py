import turtle


window = turtle.Screen()
window.bgcolor("skyblue")


house = turtle.Turtle()
house.speed(2)


house.penup()
house.goto(-75, -75)
house.pendown()
house.color("orange")
house.begin_fill()
for _ in range(4):
    house.forward(150)
    house.left(90)
house.end_fill()

house.color("brown")
house.begin_fill()
house.goto(-75, 75)
house.goto(0, 150)
house.goto(75, 75)
house.goto(-75, 75)
house.end_fill()


house.penup()
house.goto(-25, -75)
house.pendown()
house.color("darkblue")
house.begin_fill()
for _ in range(2):
    house.forward(50)
    house.left(90)
    house.forward(75)
    house.left(90)
house.end_fill()


house.penup()
house.goto(30, 0)
house.pendown()
house.color("lightyellow")
house.begin_fill()
for _ in range(4):
    house.forward(30)
    house.left(90)
house.end_fill()


house.hideturtle()
window.mainloop()
