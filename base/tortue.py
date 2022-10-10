import turtle

turtle.speed(8) 

# 1er figure
turtle.penup()
turtle.goto(100, 100)

turtle.pendown()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)


# 2e figure
turtle.penup()
turtle.goto(-100, 100)

turtle.left(90)
turtle.pendown()
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)

# 3e figure
turtle.left(72)
turtle.penup()
turtle.goto(-100, -100)


turtle.pendown()
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)

turtle.left(180)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.right(90)
turtle.forward(85)

turtle.penup()
turtle.right(180)
turtle.forward(90)

turtle.left(90)
turtle.pendown()
turtle.forward(50)
turtle.right(120)
turtle.forward(25)
turtle.right(60)
turtle.forward(75)
turtle.right(60)
turtle.forward(25)
turtle.right(120)
turtle.forward(50)

turtle.penup()
turtle.goto(0, 0)

turtle.done()