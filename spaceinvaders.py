#Space Invaders - Part 1
#Set up the screen
#Python 2.7 on Mac
import turtle
import os
import math
import random

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

#Chose a number of ememies
number_of_enemies = 5
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
    # create the enemy
    enemies.append(turtle.Turtle())


#Create the enemy
for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-245, 245)
    y = random.randint(175, 250)
    enemy.setposition(x, y)

enemyspeed = 2

#Create the players bullit
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

#Move the player left
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

#Move the player right
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

#fire the bullet
def fire_bullet():
    #Declare bulletstate as a global if it needs change
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

#
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#Main Game loop
while True:

    for enemy in enemies:
        #Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #Move enemy back and down
        if enemy.xcor() > 280:
            y = enemy.ycor()
            y -= 40
            enemyspeed *= -1
            enemy.sety(y)

        if enemy.xcor() < -280:
            y = enemy.ycor()
            y -= 40
            enemyspeed *= -1
            enemy.sety(y)
        
        #Check for collision betweem bullit and enemy
        if isCollision(bullet, enemy):
            #Rest the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #Reset the enemy
            x = random.randint(-245, 245)
            y = random.randint(250, 250)
            enemy.setposition(x, y)

        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Check to set if bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    




delay = raw_input("Press space to continue")