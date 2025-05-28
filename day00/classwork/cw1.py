from turtle import *


#we want to paint a house

#step 1: draw a square 
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
          
forward(200)
left(90)
#end of square

#drawing a door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(90)
right(90)
forward(60)
right(90)
forward(90)
end_fill()

penup()
goto(200, 200)
pendown
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#draw window
color("purple")

penup()
goto(200, 200)
pendown()

right(330)
forward(100)
begin_fill()
right(90)
forward(65)
left(270)
forward(65)
right(90)
forward(65)
right(90)
forward(166)
left(270)
forward(200)
left(270)
forward(170)
right(90)
forward(65)
right(90)
forward(65)
right(90)
forward(65)
end_fill()

exitonclick()