import turtle
import random
def spiral():
	t = turtle
	t.color('blue')
	t.speed(10)
	x = 10
	a = 91
	# Draw the base
	for i in range(150):
		for i in range(4):
			t.forward(x)
			t.left(a)
		x += 7
	# Move up
	#t.penup()
	#t.left(90)
	#t.forward(50)
	#t.pendown()

#spiral()
holdit = input()
