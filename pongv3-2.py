# Import required library
import time
from tracemalloc import start
import turtle
# turtle.bgpic('images/pong_background.jpg')
 
 
# Create screen
sc = turtle.Screen()
sc.title("Pong game")
# sc.bgcolor("white")
sc.setup(width=1200, height=800)
# sc.bgpic(f'img/pong_background2.gif')
 
 
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
right_pad.color("magenta")
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
# start ball speed
hit_ball.dx = 5
hit_ball.dy = -5
 
 
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
 
 
# def paddlebup():
#     y = right_pad.ycor()
#     y += 20
#     right_pad.sety(y)
 
 
# def paddlebdown():
#     y = right_pad.ycor()
#     y -= 20
#     right_pad.sety(y)
 
 
# Keyboard bindings
sc.listen()
# sc.onkeypress(paddleaup, "e")
# sc.onkeypress(paddleadown, "x")
sc.onkeypress(paddleaup, "Up")
sc.onkeypress(paddleadown, "Down")

# increase ball speed by time and increment
start_time = time.time()
ball_speed_time = 2
ball_speed_inc = 2
 
while True:
    sc.update()
 
    # print(hit_ball.dx)
    # print(hit_ball.xcor())
    # print(right_pad.xcor())
    # print(left_pad.xcor())
    # fix for ray-cast problem right paddle
    if (hit_ball.xcor() + hit_ball.dx > (right_pad.xcor() - 40)) and hit_ball.dx > 0:
        # print(f'step1')
        hit_ball.setx(right_pad.xcor() - 35)
    elif (hit_ball.xcor() + hit_ball.dx < (left_pad.xcor() + 40)) and hit_ball.dx <0:
        # print(f'step2')
        if (hit_ball.ycor() < left_pad.ycor()+60 and hit_ball.ycor() > left_pad.ycor()-60):
            # print(f'collision step2')
            hit_ball.setx(left_pad.xcor() + 35)
        else:
            hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    else:
        hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
 
    # print(f'bal speed: {hit_ball.dx}')
    # print(f'bal xcor: {hit_ball.xcor()}')
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
        # print(f'collision! right')
        hit_ball.setx(360)
        hit_ball.dx*=-1
        
    if (hit_ball.xcor() <-360 and hit_ball.xcor() > -370) and (hit_ball.ycor() < left_pad.ycor()+60 and hit_ball.ycor() > left_pad.ycor()-60):
        # print(f'collision! left')
        hit_ball.setx(-360)
        hit_ball.dx*=-1

    # make ball faster after x sec
    if (time.time() - start_time - ball_speed_time) > 0 :
        print(f'increase speed')
        if hit_ball.dx < 0:
            hit_ball.dx -= ball_speed_inc
        else:
            hit_ball.dx += ball_speed_inc
        
        if hit_ball.dy < 0:
            hit_ball.dy -= ball_speed_inc
        else:
            hit_ball.dy += ball_speed_inc

        print(f'speed x: {hit_ball.dx}')
        print(f'speed y: {hit_ball.dy}')
        start_time = time.time()