
# To_Do

# - ask for contact info beginning of the game
# - Create dockerfile
# - Create scoring method
# - Save scores and info in a csv
# - adjust speed of bat when speed of ball increases

# Import required library
import time
from tracemalloc import start
import turtle
import numpy as np
import os

#os.chdir("..")

from win32api import GetSystemMetrics

def pong_game():
            

    # ask for contact info
    while True:
        try:
            contact_name = input("What is your name?: ")
        except ValueError:
            print("Sorry, I didn't understand that.")
        else:
            break


    while True:
        try:
            contact_mail = input("What is your mail address?: ")
        except ValueError:
            print("Sorry, I didn't understand that.")
        else:
            break


    # set game settings
    lives = 3

    # Create screen
    sc = turtle.Screen()
    sc.title("Pong game")
    sc.bgcolor("white")
    sc.setup(width=GetSystemMetrics(0), height=GetSystemMetrics(1))

    # print(os.getcwd())
    # sc.bgpic(f'img/pong_background.gif')


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
    right_pad.shapesize(stretch_wid=6, stretch_len=2)
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
    hit_ball.dx = 20
    hit_ball.dy = -20


    # Initialize the score
    # right_player = 0
    init_level = 0 
    score = 0
    round_idx = 1

    # increase ball speed by time and increment
    start_time = time.time()
    ball_speed_time = 3
    ball_speed_inc = 2

    # Displays the score
    sketch = turtle.Turtle()
    sketch.speed(0)
    sketch.color("blue")
    sketch.penup()
    sketch.hideturtle()
    sketch.goto(0, 400)
    # sketch.write("Lives: 3   Level: 0",
    #             align="center", font=("Courier", 24, "normal"))


    # Functions to move paddle vertically
    def paddleaup():
        y = left_pad.ycor()
        y += 30
        left_pad.sety(y)


    def paddleadown():
        y = left_pad.ycor()
        y -= 30
        left_pad.sety(y)


    def paddlebup(dy):
        y = right_pad.ycor()
        y += dy
        right_pad.sety(y)
    
    
    def paddlebdown(dy):
        y = right_pad.ycor()
        y -= dy
        right_pad.sety(y)


    def paddlemove(dy):
        y = right_pad.ycor()
        y += dy
        right_pad.sety(y)

    def reset_speed():
        hit_ball.dx = 10 + (round_idx * 2)
        hit_ball.dy = -10 - (round_idx * 2)
        
        
    def increase_speed():
        # print(f'increase speed')
        if hit_ball.dx < 0:
            hit_ball.dx -= ball_speed_inc
        else:
            hit_ball.dx += ball_speed_inc
        
        if hit_ball.dy < 0:
            hit_ball.dy -= ball_speed_inc
        else:
            hit_ball.dy += ball_speed_inc

        # print(f'speed x: {hit_ball.dx}')
        # print(f'speed y: {hit_ball.dy}')


    # Keyboard bindings
    sc.listen()
    sc.onkeypress(paddleaup, "Up")
    sc.onkeypress(paddleadown, "Down")
    # sc.onkeypress(paddlebup, "e")
    # sc.onkeypress(paddlebdown, "x")

    tmp_var = 0

    turtle.speed(0)
    # sc.tracer(1, 10)
    cnt = 1
    while lives > 0:
        sc.update()

        print(time.time() - tmp_var)
        print(turtle.speed())
        tmp_var = time.time()
        score = int(score + (np.abs(hit_ball.dx) / 5))

        cnt = cnt + 1

        if (cnt % 30 == 0):
            sketch.clear()
            sketch.write("Lives : {}      Score: {}".format(
                            lives, score), align="center",
                            font=("Courier", 24, "normal"))

        # fix for ray-cast problem right paddle
        if (hit_ball.xcor() + hit_ball.dx > (right_pad.xcor() - 40)) and hit_ball.dx > 0:
            # print(f'step1')
            # hit_ball.setx(right_pad.xcor() - 35)
            # print(f'step2')
            if (hit_ball.ycor() < right_pad.ycor()+60 and hit_ball.ycor() > right_pad.ycor()-60):
                # print(f'collision step2')
                hit_ball.setx(right_pad.xcor() - 35)
            else:
                hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
        elif (hit_ball.xcor() + hit_ball.dx < (left_pad.xcor() + 40)) and hit_ball.dx < 0:
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

        # Automatically move right paddle towards the ball
        # Use the difference in y pos from right paddle compared to the ball
        # But also define max dy for the right paddle so it's imperfect!
        # The speed ratio indicates how fast the paddle can move upwards with regards to the ball speed.
        # speed_ratio < 1 means the paddle is slower than the ball and will sometimes lose
        # Jitter bwteen 0.8 and 0.9 for imperfect vs perfect behavior
        speed_ratio = np.random.uniform(.8, .85)
        y_rp = right_pad.ycor()
        y_ball = hit_ball.ycor()
        diff_y = y_ball-y_rp
        
        # Scale by distance: the further away the ball is, the slower the right paddle moves up and down
        # dist_ratio = ((right_pad.xcor()-hit_ball.xcor()) / 1000) / 5
        
        # Select the max of the ball speed times the speed_ratio and 30, so the smallest step is always 30 in case the ball is slow
        # dy_max = np.abs(hit_ball.dx * speed_ratio * (1-dist_ratio))
        dy_max = np.abs(hit_ball.dx * speed_ratio)
        
        # # Invert y direction in 10% of iterations
        # p = np.random.random()
        # if (p <= .1):
        #     dy_max *= -1
            
        if (diff_y >= dy_max):
            paddlemove(dy_max)
        elif (diff_y <= (-1*dy_max)):
            paddlemove(-1*dy_max)
        else:
            paddlemove(diff_y)



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
            score += 100
            reset_speed()
            round_idx += 1
            # sketch.clear()
            # sketch.write("Left_player : {}    Right_player: {}".format(
            #               left_player, right_player), align="center",
            #               font=("Courier", 24, "normal"))

        if hit_ball.xcor() < -500:
            hit_ball.goto(0, 0)
            hit_ball.dy *= -1
            hit_ball.dx *= -1
            # right_player += 1
            score -= 100
            reset_speed()
            round_idx += 1

            if lives == 1:
                sketch.clear()
                sketch.write("GAME OVER!!!    Score: {}".format(
                    score), align="center",
                    font=("Courier", 36, "normal"))
                lives -= 1
            else:
                lives -= 1
                sketch.clear()
                sketch.write("Lives : {}    Score: {}".format(
                            lives, score), align="center",
                            font=("Courier", 24, "normal"))
            # sketch.clear()
            # sketch.write("Left_player : {}    Right_player: {}".format(
            #                          left_player, right_player), align="center",
            #                          font=("Courier", 24, "normal"))



        # Paddle ball collision
        if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor()+400 and hit_ball.ycor() > right_pad.ycor()-400):
            # print(f'collision! right')
            hit_ball.setx(360)
            hit_ball.dx*=-1
            
        if (hit_ball.xcor() <-360 and hit_ball.xcor() > -370) and (hit_ball.ycor() < left_pad.ycor()+60 and hit_ball.ycor() > left_pad.ycor()-60):
            # print(f'collision! left')
            hit_ball.setx(-360)
            hit_ball.dx*=-1

        # Make ball faster after x sec
        if (time.time() - start_time - ball_speed_time) > 0 :
            increase_speed()
            start_time = time.time()

        # calculate score
        end_score = score


    # create output
    output = {'Naam': contact_name,'Mail': contact_mail, 'Score': end_score}

    return output
