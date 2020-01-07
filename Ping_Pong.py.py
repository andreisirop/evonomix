import turtle
wn = turtle.Screen()
wn.title("ping pong by @ANDREI SIROP")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# SCORUL
score_a = 0
score_b = 0

# LINIA 1
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# LINIA 2
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# MINGEA
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = -0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Jucatoru'A: " + str(score_a) + "  Jucatoru'B: " + str(score_b), align = "center",font=("Courier",24,"normal"))

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    if y > 270:
        paddle_a_down()
        
        

def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)
    if y < -270:
        paddle_a_up()

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    if y > 270:
        paddle_b_down()

def paddle_b_down():
    y = paddle_b.ycor()
    y += -20
    paddle_b.sety(y)
    if y < -270:
        paddle_b_up()


# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")




# lupa principala a jocului
while True:
    wn.update()

    # miscarea mingii
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # verificarea marginilor
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Jucatoru'A: " + str(score_a) + "  Jucatoru'B: " + str(score_b), align = "center",font=("Courier",24,"normal"))
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Jucatoru'A: " + str(score_a) + "  Jucatoru'B: " + str(score_b), align = "center",font=("Courier",24,"normal"))

    # coliziunea dintre bila si scandura
    if ball.xcor() > 340 and ball.xcor()<350 and (ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50):
        ball.setx(340)
        ball.dx *= -1
    if ball.xcor() < -340 and ball.xcor()>-350 and (ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50):
        ball.setx(-340)
        ball.dx *= -1

    
        
        
    
