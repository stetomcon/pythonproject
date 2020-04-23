# Space Invaders Game 
# Using Python 3 on MAC

import turtle
import os

mainScreeen = turtle.Screen()
mainScreeen.bgcolor("black")
mainScreeen.title("Steven's Space Invaders")

#Draw Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Creating Player
player = turtle.Turtle()
player.color("green")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)


#player speeds
playerspeed = 12

#Movement
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

#Create Keyboard Bindings actions like on key
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")


delay = raw_input("Enter")