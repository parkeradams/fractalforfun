import turtle
import random

# triangle
list = [[0.0, 200.0], [-200.0, -100.0], [200.0, -100.0]]

# hexagonal
# list = [[0.0, 200.0], [-200.0, -100.0], [200.0, -100.0], [-200.0, 100],[200.0, 100.0],[0, -200.0]]


turtle.speed('fastest')
turtle.up()
turtle.hideturtle()
for coord in list:
    turtle.goto(coord[0], coord[1])
    turtle.dot(3, 'black')


x = random.randint(-100, 100)
y = random.randint(-200, 200)

turtle.goto(x, y)
turtle.dot(3, 'red')


for i in range(30000):
    point = random.choice(list)
    xdist = point[0] - x
    ydist = point[1] - y
    #triangle
    x = x + (xdist * .5)
    y = y + (ydist * .5)
    
   #hexagonal
#     x = x + (xdist * .66)
#     y = y + (ydist * .66)
#     
    
    turtle.goto(x, y)
    turtle.dot(3, 'black')

turtle.done()
