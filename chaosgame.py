# chaosgame.py CMT. This is a project for High School CS class, code licensed under GNU GPL v3.0

import turtle
import random
turtle.color("red")
turtle.bgcolor("black")
turtle.penup()

# lists containing starting points
xval = [0, 300, -300]
yval = [300, 0, 0] 

#print(xval[np], "," , yval[np]) # test endpoint picking code

def newpoint(): # uses midpoint formula to find mdpt. of segment to chosen other point
	current = turtle.position()
	#print(current[0], current[1])
	#print(current) 
	np = random.randint(0,2)
	nx = (xval[np] + current[0]) / 2
	ny = (yval[np] + current[1]) / 2
	parray = [nx, ny]
	print(parray)
	return(parray) 



def draw() :  # calls newpoint function and plots a n
	turtle.speed(0)
	sp = [random.randint(-300, 300) , random.randint(0, 300) ]
	#print(sp[0],sp[1])
	turtle.goto(sp[0], sp[1])
	c = 0
	while c < (10**4):
		parray = newpoint()
		#newpoint()
		turtle.penup()
		turtle.goto(parray[0], parray[1])
		#turtle.stamp
		turtle.pendown()
		turtle.forward(1)
		c += 1
				
draw()

holdit = input()
