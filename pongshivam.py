import turtle
import keyboard
import time  

score_a = 0
score_b = 0
wn = turtle.Screen()
wn.title("Pong by Shivam Walia")  
wn.bgcolor("#0029B1")  
wn.setup(width=800, height=600)  
wn.tracer(0) 

paddle_a = turtle.Turtle()
paddle_a.speed(0)  
paddle_a.shape("square")  
paddle_a.color("#FFA500")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()  
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(5)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)   

ball = turtle.Turtle()
ball.speed(0.25)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

#start = turtle.Turtle()
#start.speed(0)
#start.color('white')
#start.penup()
#start.hideturtle()
#start.goto(0, 0)
#start.write("Press Any Key to Start", align="center", font=("Courier", 24, "normal"))

#start.clear()


pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

def paddle_a_up():
    y = paddle_a.ycor()  # .ycor() return y coordinate
    y += 20  # Move up
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20  # Move down
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def quit_program():
    global running
    running = False

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

running = True
# Main game loop
while running:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Top & Bottom Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # Reverse the direction of ball
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    #pause menu
    if keyboard.is_pressed('1'):
        pen.clear()
        pen.write("Paused press 2 to restart", align="center", font=("Courier", 24, "normal"))
        ball.dx = 0
        ball.dy = 0

    if keyboard.is_pressed('2'):
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))
        ball.dx = 0.25
        ball.dy = 0.25
        ball.goto(0, 0)

    # Left & Right Border
    if ball.xcor() > 390:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))  # Update score
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Bounce of the paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 70):
        ball.setx(340)
        ball.dx *= -1
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
        ball.setx(-340)
        ball.dx *= -1

    if keyboard.is_pressed('esc'):
        quit_program()
        