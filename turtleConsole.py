Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.Screen()
<turtle._Screen object at 0x7fc4a9f32b20>
>>> turtle.pen()
{'shown': True, 'pendown': True, 'pencolor': 'black', 'fillcolor': 'black', 'pensize': 1, 'speed': 3, 'resizemode': 'noresize', 'stretchfactor': (1.0, 1.0), 'shearfactor': 0.0, 'outline': 1, 'tilt': 0.0}
>>> turtle.shape("turtle")
>>> turtle.forward(200)
>>> turtle.left(90)
>>> turtle.forward(200)
>>> turtle.left(90)
>>> turtle.forward(200)
>>> turtle.left(90)
>>> turtle.forward(200)
>>> turtle.left(90)
>>> 
>>> turtle.clear()
>>> for i in range(4):
	turtle.forward(200)
	turtle.left(90)

>>> turtle.clear()
>>> x=20
>>> for i in range(4):
	turtle.forward(x)
	turtle.left(90)
	x+=50

>>> turtle.clear()
>>> for i in range(400):
	turtle.forward(x)
	turtle.left(90)
	x+=30

