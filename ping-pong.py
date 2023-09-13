import turtle

wind = turtle.Screen()
wind.setup(width=800, height=600)
wind.bgcolor("black")
wind.title("welcome to mohamed alaa game's")
wind.tracer(0)

madrab1 = turtle.Turtle()
madrab1.shape("square")
madrab1.shapesize(stretch_wid=6 ,stretch_len=1)
madrab1.color("red")
madrab1.speed(0)
madrab1.penup()
madrab1.goto(350,0)


madrab2 = turtle.Turtle()
madrab2.shape("square")
madrab2.shapesize(stretch_wid=6 ,stretch_len=1)
madrab2.color("blue")
madrab2.speed(0)
madrab2.penup()
madrab2.goto(-350,0)

ball = turtle.Turtle()
ball.shape("circle")
ball.shapesize(stretch_wid=1 ,stretch_len=1)
ball.color("white")
ball.speed(0)
ball.penup()
ball.goto(0,0)
ball.dx= .3
ball.dy= .3

score1 = 0
score2 = 0
score= turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.goto(0,270)
score.write("player 1: 0 ,player 2: 0 " , font=("courier",14 ,"normal"),align="center")
score.hideturtle()

center_line = turtle.Turtle()
center_line.shape("square")
center_line.shapesize(stretch_wid=20 ,stretch_len=.1)
center_line.speed(0)
center_line.goto(0,0)
center_line.color("white")
def madrab1_up():
    y=madrab1.ycor()
    y+=20
    madrab1.sety(y)
    
def madrab1_down():
    y=madrab1.ycor()
    y-=20
    madrab1.sety(y)

def madrab2_up():
    y=madrab2.ycor()
    y+=20
    madrab2.sety(y)
    
def madrab2_down():
    y=madrab2.ycor()
    y-=20
    madrab2.sety(y)
wind.listen()
wind.onkeypress(madrab1_up, "w")
wind.onkeypress(madrab1_down, "s")
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")

while True:
    wind.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *=-1
        score.clear()
        score1 +=1
        score.write("player 1: {} ,player 2: {} ".format(score1, score2),align="center" , font=("courier",14 ,"normal"))


    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *=-1
        score.clear()
        score2 +=1
        score.write("player 1: {} ,player 2: {} ".format(score1, score2) ,align="center", font=("courier",14 ,"normal"))


    if (ball.xcor() >340 and ball.xcor() <350 and ball.ycor() <madrab1.ycor()+60 and ball.ycor() >madrab1.ycor() -60): 
        ball.setx(340)
        ball.dx *=-1

    if (ball.xcor() <-340 and ball.xcor() >-350 and ball.ycor() <madrab2.ycor()+60 and ball.ycor() >madrab2.ycor() -60): 
        ball.setx(-340)
        ball.dx *=-1

        
    if madrab1.ycor() > 235:
        madrab1.sety(235)

    if madrab1.ycor() < -235:
        madrab1.sety(-235)
    
    if madrab2.ycor() > 235:
        madrab2.sety(235)

    if madrab2.ycor() < -235:
        madrab2.sety(-235)
        


    
        

