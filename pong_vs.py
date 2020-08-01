import turtle 

t = turtle.Screen()
t.title("Ping Pong")
t.bgcolor("yellow")
t.setup(width = 800, height = 600)
t.tracer(2)


# Score
score_a = 0
score_b = 0


# paddle A
padA = turtle.Turtle()
padA.speed(0)
padA.shape("square")
padA.color("red")
padA.shapesize(stretch_wid=7, stretch_len=1)
padA.penup()
padA.goto(-350,0)



#paddle B
padB = turtle.Turtle()
padB.speed(0)
padB.shape("square")
padB.color("red")
padB.shapesize(stretch_wid= 7, stretch_len=1) #70 pix
padB.penup()

padB.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("black")

ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = 1 #moves by 1 pixels

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Player A: 0 ", align="center", font=("Courier", 24, "normal",))

#func
def padA_up():
    y = padA.ycor()
    y+=30
    padA.sety(y)

def padA_down():
    y = padA.ycor()
    y-=30
    padA.sety(y)

def padB_up():
    y = padB.ycor()
    y+=30
    padB.sety(y)

def padB_down():
    y = padB.ycor()
    y-=30
    padB.sety(y)
#Keyboard binding
t.listen()
t.onkeypress(padA_up,"w")
t.onkeypress(padA_down,"s")
t.onkeypress(padB_up,"Up")
t.onkeypress(padB_down,"Down")


#Main game loop
while True:
    t.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *=-1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a+=1
        pen.clear()
        pen.write("Player A: {} ".format(score_a), align="center", font=("Courier", 24, "normal"))



    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *=-1
        score_b +=1
        pen.clear()


        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    
    #Paddle collisions
    if ball.xcor() > 340 and ball.xcor()<350 and (ball.ycor() < padB.ycor() +40 and ball.ycor() > padB.ycor()-40):
        ball.setx(340)
        ball.dx *= -1
    if ball.xcor() < -340 and ball.xcor()>-350 and (ball.ycor() < padA.ycor() +40 and ball.ycor() > padA.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1