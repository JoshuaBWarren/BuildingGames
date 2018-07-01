import turtle
import os
import math
import random

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders!")

#Draw border
border_pen = turtle.Turtle()

#0 speed is the fastest speed
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -260)
player.setheading(90)

#Create player movement left and right
playerspeed = 15

#Number of enemies in the game
number_of_enemies = 18

#Create list of enemies
enemies = []

#Create offset value
xOffset = 0
yOffset = 50

#Create row value
row = 0

#Add enemies to the list
for i in range(number_of_enemies):
    #Create the enemy
    enemies.append(turtle.Turtle())

#For each of the enemy turtles
for enemy in enemies:
    if row > 10:
        xOffset += 50
        x = -235 + xOffset - 550
        y = 200
        enemy.setposition(x, y)
        row += 1
    else:
        xOffset += 50
        enemy.color("red")
        enemy.shape("circle")
        enemy.penup()
        enemy.speed(0)
        x = -285 + xOffset
        y = 250
        enemy.setposition(x, y)
        row += 1

    
        


enemyspeed = 2

#Create player bullets
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.6, 0.5)
bullet.hideturtle()

bulletspeed = 20

#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

#Functions
def move_left():
    #grab the players current x-coordinate
    x = player.xcor()
    #reduce that coordinate by playerspeed
    x -= playerspeed
    #check to make sure x doesn't go too far left
    if x < -280:
        x = -280
    #set new coordinate location of player
    player.setx(x)

def move_right():
    #grab the players current x-coordinate
    x = player.xcor()
    #add that coordiante by playerspeed
    x += playerspeed
    #check to make sure x doesn't go too far right
    if x > 280:
        x = 280
    #set new coordinate location of player
    player.setx(x)

def fire_bullet():
    #Declare bulletstate as a global if it needs to be changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #Move the bullet up
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

#Check for collision
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


#Create keyboard bindings
wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(fire_bullet, "space")

#Main game loop
while True:

    for enemy in enemies:
        #Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #Move the enemy back and down
        if enemy.xcor() > 280:
            x = enemy.xcor() * -1
            y = enemy.ycor() - 40
            #enemyspeed *= -1
            enemy.setposition(x, y)

        #Check collision between a bullet and an enemy
        if isCollision(bullet, enemy):
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            #take bullet way below screen so it doesn't hit other enemies
            bullet.setposition(0, -400)

            #Hide the enemy
            enemy.setposition(0, -500)
            number_of_enemies = number_of_enemies - 1
            enemy.hideturtle()

        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print ("Game Over")
            break

    #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    
    #Check to see if the bullet reaches the end of the screen
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    #Check the number of enemies for win state
    if number_of_enemies == 0:
        player.hideturtle()
        print ("You win!")
        break

       

wn.mainloop()


delay = input("Press enter to finish.")