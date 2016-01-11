import turtle

def drawSquare(myTurtle):
	myTurtle.forward(20)
	myTurtle.right(90)
	myTurtle.forward(20)
        myTurtle.right(90)
	myTurtle.forward(20)
        myTurtle.right(90)
        myTurtle.forward(20)

def drawSquareColor(myTurtle):
	count = 0
	while count < 5:
		myTurtle.color('red')
		drawSquare(myTurtle)
		myTurtle.right(90)
		myTurtle.forward(20)	
		myTurtle.color('blue')
		drawSquare(myTurtle)
		myTurtle.color('green')
		drawSquare(myTurtle)
		myTurtle.color('yellow')
		drawSquare(myTurtle)
		myTurtle.penup()
		myTurtle.forward(35)		
		myTurtle.left(90)
		myTurtle.pendown()
		count = count + 1

carl = turtle.Turtle()
drawSquareColor(carl)

turtle.exitonclick()
