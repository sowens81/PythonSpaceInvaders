#Space Invaders - Part 1
#Set up the screen
#Python 2.7 on Mac
import turtle
import os

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#Draw Boarder
boarder_pen = turtle.Turtle()
boarder_pen.speed(0)
boarder_pen.color("white")
boarder_pen.penup()
boarder_pen.setposition(-300,-300)
boarder_pen.pendown()
boarder_pen.pensize(3)
for side in range(4):
    boarder_pen.fd(600)
    boarder_pen.lt(90)
boarder_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#Move the player left
def move_left():
    x = player.xcor()
    x -= playerspeed
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    player.setx(x)

#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")



delay = raw_input("Press space to continue")