# Import required library
import turtle
# turtle.bgpic('images/pong_background.jpg')
 
 
# Create screen
sc = turtle.Screen()
sc.title("Pong game")
# sc.bgcolor("white")
sc.setup(width=1000, height=1000)
#sc.bgpic(f'images/pong_background.gif')
 
 
# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)
 
 
# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
#right_pad.color("magenta")
right_pad.shapesize(stretch_wid=25, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)
 
 
# Ball of circle shape
hit_ball = turtle.Turtle()
hit_ball.speed(0)
hit_ball.shape("circle")
hit_ball.color("orange")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 25
hit_ball.dy = -25
 
 
# Initialize the score
left_player = 0
right_player = 0
 
 
# Displays the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_player : 0    Right_player: 0",
             align="center", font=("Courier", 24, "normal"))
 
 
# Functions to move paddle vertically
def paddleaup():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)
 
 
def paddleadown():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)
 
 
def paddlebup():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)
 
 
def paddlebdown():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)
 







pen = turtle.Turtle()
pen.speed(0)

#Creating Menu option buttons
def button(length):
    for i in range(4):
        pen.forward(length)
        pen.left(90)

def column(n, length):
    pen.left(270)
    for i in range(n):
        button(length)
        pen.forward(length)
    pen.penup()
    pen.left(90)
    pen.forward(n * length)
    pen.left(180)
    pen.pendown()

column(5, 100)

#Menu Options
pen.penup()
pen.goto(8, -46)
pen.write("START GAME!", font=("Arial",12,"normal"))

pen.penup()
pen.goto(6, -145)
pen.write("RULES", font=("Arial",12,"normal"))

pen.penup()
pen.goto(3, -248)
pen.write("HIGH SCORE", font=("Arial",12,"normal"))

pen.penup()
pen.goto(4, -343)
pen.write("FAQ", font=("Arial",12,"normal"))

pen.penup()
pen.goto(3, -450)
pen.write("QUIT GAME", font=("Arial",12,"normal"))

#Making options clickable
def btnclick(x,y):
    if x > 0 and x < 101 and y > 0 and y < -101:
        print("Start Game")
        print(x, y)
        turtle.clearscreen()
    elif x > 0 and x < 101 and y > 101 and y < -201:
        print("Rules")
        print(x, y)
        turtle.clearscreen()
    elif x > 0 and x < 101 and y > 201 and y < -301:
        print("Highscore")
        print(x, y)
        turtle.clearscreen()
    elif x > 0 and x < 101 and y > 301 and y < -401:
        print("Hi")
        print(x, y)
        turtle.clearscreen()
    elif x > 0 and x < 101 and y > 401 and y < -501:
        print("Hi")
        print(x, y)
        turtle.clearscreen()
    elif x > 0 and x < 101 and y > 501 and y < -601:
        print("Hi")
        print(x, y)
        turtle.clearscreen()
    else:
        print("Click One Of The Options!")
        print(x, y)
        btnclick(x, y)

turtle.onscreenclick(btnclick, 1)
turtle.listen()

turtle.done()










 
# Keyboard bindings
sc.listen()
sc.onkeypress(paddleaup, "e")
sc.onkeypress(paddleadown, "x")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")














 
 
while True:
    sc.update()
 

    # print(hit_ball.dx)
    print(hit_ball.xcor())
    # print(right_pad.xcor())
    # print(left_pad.xcor())
    # fix for ray-cast problem right paddle
    if (hit_ball.xcor() + hit_ball.dx > (right_pad.xcor() - 40)) and hit_ball.dx > 0:
        print(f'step1')
        hit_ball.setx(right_pad.xcor() - 35)
    elif (hit_ball.xcor() + hit_ball.dx < (left_pad.xcor() + 40)) and hit_ball.dx <0:
        print(f'step2')
        if (hit_ball.ycor() < left_pad.ycor()+60 and hit_ball.ycor() > left_pad.ycor()-60):
            print(f'collision step2')
            hit_ball.setx(left_pad.xcor() + 35)
        else:
            hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    else:
        hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
 
    print(f'bal speed: {hit_ball.dx}')
    print(f'bal xcor: {hit_ball.xcor()}')
    hit_ball.sety(hit_ball.ycor()+hit_ball.dy)

    # Checking borders
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1
 
    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1
 
    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
                      left_player, right_player), align="center",
                      font=("Courier", 24, "normal"))
 
    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        hit_ball.dx *= -1
        right_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
                                 left_player, right_player), align="center",
                                 font=("Courier", 24, "normal"))
 
    # Paddle ball collision
    if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor()+400 and hit_ball.ycor() > right_pad.ycor()-400):
        print(f'collision! right')
        hit_ball.setx(360)
        hit_ball.dx*=-1
        
    if (hit_ball.xcor() <-360 and hit_ball.xcor() > -370) and (hit_ball.ycor() < left_pad.ycor()+60 and hit_ball.ycor() > left_pad.ycor()-60):
        print(f'collision! left')
        hit_ball.setx(-360)
        hit_ball.dx*=-1