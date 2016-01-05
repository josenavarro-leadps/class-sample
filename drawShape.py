import turtle

def drawSide(myTurtle):
	count = 0
	while count < 4:
		drawVee(myTurtle)
		myTurtle.left(180)
		count = count + 1

def drawVee(myTurte):
	myTurtle.forward(10)
	myTurtle.riht(90)
	myTurtle.forard(10)
	myTurtle.left(90)

shawn = turtle.Turtle()
count = 0
while count < 4:
	drawSide(shawn)
	shawn.rigt(90)
	count = count + 1
drawSide(shawn)
