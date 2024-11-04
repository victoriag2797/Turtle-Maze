#setup
#turt controls
import turtle
#moves turtle foward when up is pressed
def turtle_forward():
    turt.foward(10)
#moves turtle right when right is pressed
def turtle_right():
    turt.right (90)
#moves turtle left when left is pressed
def turtle_left():
    turt.left(90)

turt = turtle.Turtle()
turt.shape("turtle")
colors = ['red', ‘orange', 'yellow',' green', ‘blue’, ‘purple’, ‘pink’]
turt.penup()
turt.goto(-200, 200)

screen = turtle.Screen()
screen.listen()
screen.onkey(turtle_foward, “Up”)
screen.onkey(turtle_right, “Right”)
screen.onkey(turtle_left, “Left”)

turtle.mainloop()

#message
def end_message();
    message_turtle = turtle.Turtle()
    message_turtle.hideturtle()
    message_turtle.penup()
    message_turtle.goto(-200,200)
    message_turtle.write(“Congrats! You solved the maze!”)

#to check if the player solved the maze
def check_finish():
    If turt.distance(200,-180) < 10:
        end_message()

while True:
check_finish()

turtle.mainloop

t.speed(0)
t.penup()
t.setpos(-200,200)
t.pendown()

#walls
t.pensize(5)
t.right(90)
t.forward(360)
t.left(90)
t.forward(297)
t.penup()
t.forward(33)
t.pendown()
t.forward(66)
t.left(90)
t.forward(360)
t.left(90)
t.forward(363)

#inside of maze
#vertical row 1/11
t.pensize(3)
t.left(90)
t.forward(90)
t.penup()
t.forward(30)
t.pendown()
t.forward(120)
t.penup()
t.forward(90)

#vertical row 2/11 
t.left(90)
t.forward(33)
t.left(90)
t.pendown()
t.forward(60)
t.penup()
t.forward(75)
t.pendown()
t.forward(75)
t.penup()
t.forward(30)
t.pendown()
t.forward(90)
t.right(90)

#vertical row 3/11
t.penup()
t.forward(33)
t.right(90)
t.forward(30)
t.pendown()
t.forward(120)
t.penup()
t.forward(30)
t.pendown()
t.forward(60)
t.penup()
t.forward(30)
t.pendown()
t.forward(30)
t.penup()

#vertical row 4/11
t.left(90)
t.forward(33)
t.left(90)
t.forward(105)
t.pendown()
t.forward(75)
t.penup()
t.forward(45)
t.pendown()
t.forward(15)
t.right(90)

#vertical row 5/11
t.penup()
t.forward(33)
t.right(90)
t.pendown()
t.forward(60)
t.penup()
t.forward(60)
t.pendown()
t.forward(30)
t.penup()
t.forward(30)
t.pendown()
t.forward(30)
t.penup()
t.forward(30)
t.pendown()
t.forward(30)
t.penup()
t.left(90)

#vertical row 6/11
t.forward(33)
t.left(90)
t.forward(30)
t.pendown()
t.forward(60)
t.penup()
t.forward(120)
t.pendown()
t.forward(60)
t.right(90)
t.penup()

#vertical row 7/11
t.forward(33)
t.right(90)
t.forward(15)
t.pendown()
t.forward(45)
t.penup()
t.forward(90)
t.pendown()
t.forward(60)
t.left(90)
t.penup()

#vertical row 8/11
t.forward(33)
t.left(90)
t.forward(15)
t.pendown()
t.forward(15)
t.penup()
t.forward(90)
t.pendown()
t.forward(30)
t.penup()
t.forward(45)
t.pendown()
t.forward(15)
t.penup()
t.forward(30)
t.right(90)

#vertical row 9/11
t.forward(33)
t.right(90)
t.pendown()
t.forward(60)
t.penup()
t.forward(210)
t.pendown()
t.forward(60)
t.left(90)
t.penup()

#vertical row 10/11
t.forward(33)
t.left(90)
t.pendown()
t.forward(90)
t.penup()
t.forward(60)
t.pendown()
t.forward(30)
t.penup()
t.forward(60)
t.pendown()
t.forward(90)
t.right(90)
t.penup()

#vertical row 11/11
t.forward(33)
t.right(90)
t.forward(15)
t.pendown()
t.forward(45)
t.penup()
t.forward(180)
t.pendown()
t.forward(90)

#horizontal column 1/13
t.penup()
t.setpos(-200,200)
t.forward(30)
t.left(90)
t.forward(99)
t.pendown()
t.forward(198)
t.penup()
t.forward(99)
t.right(90)

#horizontal column 2/13
t.forward(30)
t.right(90)
t.forward(33)
t.pendown()
t.forward(33)
t.penup()
t.forward(66)
t.pendown()
t.forward(66)
t.penup()
t.forward(33)
t.pendown()
t.forward(33)
t.penup()
t.forward(132)
t.left(90)

#horizontal column 3/13
t.forward(30)
t.left(90)
t.forward(33)
t.pendown()
t.forward(33)
t.penup()
t.forward(33)
t.pendown()
t.forward(66)
t.penup()
t.forward(66)
t.pendown()
t.forward(66)
t.penup()
t.forward(99)
t.right(90)

#horizontal column 4/13
t.forward(30)
t.right(90)
t.forward(66)
t.pendown()
t.forward(66)
t.penup()
t.forward(165)
t.pendown()
t.forward(66)
t.penup()
t.forward(33)
t.left(90)

#horizontal column 5/13
t.forward(30)
t.left(90)
t.forward(99)
t.pendown()
t.forward(231)
t.penup()
t.forward(66)
t.right(90)

#horizontal column 6/13
t.forward(15)
t.right(90)
t.pendown()
t.forward(33)
t.penup()
t.forward(363)
t.left(90)

#horizontal column 7/13
t.forward(15)
t.left(90)
t.forward(165)
t.pendown()
t.forward(165)
t.penup()
t.forward(66)
t.right(90)

#horizontal column 8/13
t.forward(15)
t.right(90)
t.forward(33)
t.pendown()
t.forward(33)
t.penup()
t.forward(330)
t.left(90)

#horizontal column 9/13
t.forward(15)
t.left(90)
t.forward(231)
t.pendown()
t.forward(99)
t.penup()
t.forward(66)
t.right(90)

#horizontal column 10/13
t.forward(30)
t.right(90)
t.pendown()
t.forward(132)
t.penup()
t.forward(66)
t.pendown()
t.forward(165)
t.penup()
t.forward(33)
t.left(90)

#horizontal column 11/13
t.forward(30)
t.left(90)
t.forward(66)
t.pendown()
t.forward(99)
t.penup()
t.forward(66)
t.pendown()
t.forward(99)
t.penup()
t.forward(66)
t.right(90)

#horizontal column 12/13
t.forward(30)
t.right(90)
t.forward(99)
t.pendown()
t.forward(99)
t.penup()
t.forward(165)
t.pendown()
t.forward(33)
t.penup()
t.left(90)

#horizontal column 13/13
t.forward(30)
t.left(90)
t.forward(66)
t.pendown()
t.forward(198)
t.penup()

#turtle
t.setpos(-200,200)
