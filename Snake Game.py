#Importing Libraries
import turtle
import random
import time

#Creating Screen
screen = turtle.Screen()
screen.title("SNAKE GAME")
screen.setup(width=700, heigh=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")

#Creating Border
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

# Score
score = 0;
delay = 0.1

# Snake
snake = turtle.Turtle()
snake.speed()
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

# Food
