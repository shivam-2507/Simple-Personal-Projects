# Imports
import turtle
import keyboard

# Score variables
score_a = 0
score_b = 0

# initializing screen
wn = turtle.Screen()
wn.title("Pong by Shivam Walia")
wn.bgcolor("#000000")
wn.setup(width=800, height=600)

# Start Screen Set Up
pen1 = turtle.Turtle()
pen1.speed(0)
pen1.color('red')
pen1.penup()
pen1.hideturtle()
pen1.goto(0, 0)
pen1.write("Press K to Start", align="center", font=("Courier", 32, "bold"))


def start_program():
    global start
    start = False


start = True
while start:
    wn.update()
    if keyboard.is_pressed('k'):
        start_program()
        wn.tracer(0)

pen1.clear()
wn.update()

# Creating Paddles and Ball
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(5)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0.25)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

# Score board
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center",
          font=("Courier", 24, "normal"))

# Paddle Functions


def paddle_a_up():
    y = paddle_a.ycor()  # Return y coordinate
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


# Main game loop
running = True
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

    # Pause menu
    if keyboard.is_pressed('1'):
        pen.clear()
        pen.write("Paused Press P to Restart", align="center",
                  font=("Courier", 24, "normal"))
        ball.dx = 0
        ball.dy = 0

    # Game restart
    if keyboard.is_pressed('p'):
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))
        ball.dx = 0.25
        ball.dy = 0.25
        ball.goto(0, 0)
        paddle_a.goto(-350, 0)
        paddle_b.goto(350, 0)

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

    # Quit program button
    if keyboard.is_pressed('esc'):
        quit_program()

    # Debugging Print Statements
#    print(f"Ball coordinates: ({ball.xcor()}, {ball.ycor()})")
#    print(f"Paddle A coordinates: ({paddle_a.xcor()}, {paddle_a.ycor()})")
#    print(f"Paddle B coordinates: ({paddle_b.xcor()}, {paddle_b.ycor()})")
# comment1
