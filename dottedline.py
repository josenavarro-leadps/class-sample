import turtle
notshawn = turtle.Turtle()

count = 0
notshawn.speed(0)
while count < 20:
	notshawn.forward(5)
	notshawn.penup()
	notshawn.forward(5)
        notshawn.pendown()
	notshawn.penup()
	notshawn.goto(-100, -55)
	notshawn.circle(10)
	notshawn.pendown()
count = count + 1
turtle.exitonclick()

