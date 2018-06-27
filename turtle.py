import turtle

tina = turtle.Turtle()
tina.shape("turtle")

"""
John.penup()
John.forward(200)
John.write("Why, hello there!")
John.backward(200)
"""

"""
John.forward(50)
John.left(90)
John.forward(50)
John.left(90)
John.forward(50)
John.left(90)
John.forward(50)
"""

"""
tina.left(90)
tina.forward(20)
tina.write("What color am I now?")

tina.forward(20)
tina.color("blue")
tina.write("What color am I now?")

tina.forward(20)
tina.color("purple")
tina.write("What color am I now?")

tina.forward(20)
tina.color("green")
tina.write("What color am I now?")
"""

"""
tina.penup()
tina.goto(0,100)
tina.write("I don't draw when my pen is up!")
tina.goto(0,50)
tina.pendown()
tina.write("I do draw when my pen is down!")
tina.goto(-50,50)
"""

"""
tina.penup()
tina.write("I start at 0, 0")

tina.goto(100,100)
tina.write("This is 100, 100")

tina.goto(-100,-100)
tina.write("This is -100, -100")

tina.goto(100,-100)
tina.write("This is 100, -100")

tina.goto(-100,100)
tina.write("This is -100, 100")

tina.goto(-100, 0)
"""


"""
tina.penup()
tina.goto(30,-150)
tina.pendown()
tina.circle(130)
tina.penup()
tina.goto(0,0)
tina.pendown()
tina.circle(20)
tina.circle(10)
tina.penup()
tina.forward(60)
tina.right(45)
tina.pendown()
tina.circle(30)
tina.circle(10)
tina.penup()
tina.right(90)
tina.forward(90)
tina.pendown()
tina.circle(40)
tina.penup()
tina.goto(25,-25)
"""

"""
Guess = int(input("What is 2 X 7?"))

if Guess == 2*7:
    tina.write(str(Guess) + ' is correct!')
    tina.penup()
    tina.backward(10)
else:
    tina.write('You said ' + str(Guess) + '. I got ' + str(2*7))
    tina.penup()
    tina.backward(10)

"""

"""
def triangle():
    tina.left(60)
    tina.forward(30)
    tina.left(120)
    tina.forward(30)
    tina.left(120)
    tina.forward(30)

triangle()

"""


"""
def make_cake(x=0, y=0):
    tina.penup()
    tina.color('pink')
    tina.goto(x, y)
    tina.pendown()
    tina.begin_fill()
    tina.goto(x + 20, y)
    tina.goto(x + 20, y + 20)
    tina.goto(x - 20, y + 20)
    tina.goto(x - 20, y)
    tina.goto(x, y)  
    tina.end_fill()
    tina.goto(x, y + 20)
    tina.color('yellow')
    tina.goto(x, y + 35)
    tina.goto(x, y + 30)
    tina.color('black')
    tina.goto(x, y + 20)
    tina.penup()
    tina.goto(x, y + 10)

make_cake(0,0)
make_cake(-100,0)
make_cake(100,0)
"""

"""
def say(something):
    x, y = tina.pos()
    tina.write("You told me to say this:")
    tina.goto(x + 10, y -10)
    tina.write(something)
    tina.goto(x, y - 25)

say("Hi there!")
say("Hi there!")
say("Hi there!")
say("Hi there!")
say("Hi there!")
say("Hi there!")
say("Hi there!")
"""
