######################################################
# Project: Project 1
# Student Name:  Member, Miran
# UIN: 654424039
# repl.it URL: https://repl.it/@mmembe2/Turtle-project-1
######################################################
'''
IMPORTANT!!
Please run the program at least 2 times, the first time it does not load the drawing.
The buildings and stars are random each time.
'''

import turtle#importing the turtle module
import random#importing the randome module

#------------------------------------------------------------#
#if moon is 1 then it will be circle, if moon equals 2 then it will be polygon
moon=1
#------------------------------------------------------------#


t = turtle.Turtle()#creating turtle 1
t2 = turtle.Turtle()#creating tutle 2
screen = t.getscreen()
screen.setup(width=.4, height=.318, startx=None, starty=None)#making the screen big so it works in full screen also
screen.tracer(0)#making turtle draw fast
t.penup()#pen up for turtle 1 
t2.penup()#pen up for tutle 2
t.hideturtle()#hiding the turtle1
t2.hideturtle()#hiding the turtle 2

def draw_star(num_of_star):#function that draws star at randome 
  t.color('white')
  for i in range(num_of_star):#foor loop, which takes in variable for number of stars
    t.setpos(random.randrange(-700,700),random.randrange(-100,300))#using tutle 1 
    t.dot(random.randrange(2,5))#making the star size random

def draw_background():#creates the back ground
  t.color('dark blue')#setting dark blue for the dark sky
  t.dot(1000)#creating a huge dot so it covers up the whole screen
  draw_star(200)#calling the draw star funcion with 200 stars


def draw_polygon(num_sides,side_length):#if moon equals 2 it will draw a polygon 
  t.setpos(0,100)#setting position so its in the center
  t.color('white')#moon is white so changing turtle 1 to white
  t.pendown()#pen down 
  t.begin_fill()#uses the fill funcion of the module to fill the polydon white
  for i in range(num_sides):#creates the polygon
    t.fd(side_length)#uses the side lenght to make it bigger or smaller
    t.left(360/num_sides)#divides it by 360 so it gets the correct angle depending on its sides
  t.end_fill()#ends the filling funcion 

def draw_circle(radius):#creates a circle if moon equals 1
  t2.color('white')#uses the second turtle 
  t2.setpos(0,200)#positioning the second turtle
  t2.dot(radius)#creates a moon depedning on its radious input 

def draw_shape(color):#creates the building
  t2.setpos(-700,0)#setting the poisition of turtle 2
  t2.color(color,color)#getting the color of the buildings
  t2.pendown()#pendown for turtle 2
  t2.begin_fill()#uses the fill funcion
  for i in range(20):#creates random shapes of the building
    t2.fd(random.randrange(10,100))
    t2.right(90)
    t2.fd(random.randrange(10,100))
    t2.left(90)
    t2.fd(random.randrange(10,100))
    t2.left(90)
    t2.fd(random.randrange(10,100))
    t2.right(90)
  t2.right(90)
  t2.fd(1000)
  t2.right(90)
  t2.fd(3000)
  t2.goto(-700,0)#makes the turtle go back to orignal postion so the fill funcion works
  t2.end_fill()#ending the fill funcion

def turtle_write():
  t2.penup()
  t2.color('light blue')
  x=-150
  for i in range(25):
    x=x+10
    t2.goto(x,-175)
    t2.dot(75)
  t2.color('white')
  t2.goto(-125,-200)
  t2.write('Chicago', font=("Arial", 50))

def main():#the main funcion 
  draw_background()#draws the background
  if moon==1:#checkes weather the moon is 1 or 2
    draw_circle(100)#size of the moon circle
  elif moon ==2:
    draw_polygon(6,100)#amount of sides for the polygon and the length
  draw_shape('black')#color for the building
  turtle_write()

main()#runs the main function which in turn runs all the functions
screen.update()