from turtle import *
import random

screen = Screen()
screen.bgcolor("White")
screen.setup(1300, 700)

t = Turtle(shape="turtle")
t.color("black")

pensz = 1
distance = 10


def k1():
    """ Move turtle forward and change pen-color randomly """
    t.pencolor(random.random(), random.random(), random.random())
    t.forward(20)


def inc_dist():
    """ Increase the distance turtle moves"""
    global distance
    t.pencolor(random.random(), random.random(), random.random())
    distance += 5
    t.forward(distance)


def dec_dist():
    """ Decrease the distance turtle moves"""
    global distance
    distance -= 5
    if distance > 5:
        t.forward(distance)
    else:
        distance = 5
        t.forward(distance)


def k2():
    """ Move turtle 45 degrees to the right"""
    t.right(45)


def k3():
    """ Move turtle backwards with pen-color set to white"""
    t.pencolor("white")
    t.backward(20)


def k4():
    """ Move turtle 45 degrees to the left"""
    t.left(45)


def up():
    """ turtle pen up"""
    t.penup()


def down():
    """ turtle pen down"""
    t.pendown()


def sz():
    """ Increase pen size"""
    global pensz
    pensz += 1
    t.pensize(pensz)


def sz_2():
    """ Decrease pen size"""
    global pensz
    pensz -= 1
    if pensz > 0:
        t.pensize(pensz)
    else:
        pensz = 1
        t.pensize(pensz)


def close():
    """ close the screen"""
    screen.bye()


def reset():
    """ Reset the canvas"""
    screen.reset()


def guideline(text, x, y):
    """ Write the guideline on the specified place on canvas"""
    guide = Turtle(shape="blank")
    guide.penup()
    guide.goto(x, y)
    guide.write(text, font=("Times", 10, "bold"))


def main():
    guideline("GUIDE", 430, 315)
    guideline("'↑' FORWARD", 430, 285)
    guideline("'↓' BACKWARDS + CLEAN", 430, 255)
    guideline("'→' RIGHT", 430, 225)
    guideline("'←' LEFT", 430, 195)
    guideline("' q ' CLOSE CANVAS", 430, 165)
    guideline("' u ' PEN-UP", 430, 135)
    guideline("' d ' PEN-DOWN", 430, 105)
    guideline("' r ' RESET CANVAS", 430, 65)
    guideline("' s ' INCREASE PENSIZE", 430, 25)
    guideline("'space' DECREASE PENSIZE", 430, -15)
    guideline("' x ' INCREASE THE DISTANCE \n TURTLE MOVES BY 5  ", 430, -60)
    guideline("' z ' DECREASE THE DISTANCE \n TURTLE MOVES BY 5  ", 430, -110)

    screen.onkey(k1, "Up")       # Move Up
    screen.onkey(k2, "Right")    # Move Right
    screen.onkey(k3, "Down")     # Move Down
    screen.onkey(k4, "Left")     # Move left
    screen.onkey(close, "q")     # Close the canvas
    screen.onkey(up, "u")        # Pen up
    screen.onkey(down, "d")      # Pen down
    screen.onkey(reset, "r")     # Reset the Canvas
    screen.onkey(sz, "s")        # Increase pensize
    screen.onkey(sz_2, "space")  # Decrease pensize
    screen.onkey(inc_dist, "x")  # Increase the distance turtle moves by 5
    screen.onkey(dec_dist, "z")  # Decrease the distance turtle moves by 5

    screen.listen()
    screen.mainloop()

main()