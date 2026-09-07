import turtle as t
from turtle import colormode
import random

colormode(255)
t.speed(0)
t.bgcolor("black")
t.penup()
t.goto(0, -300)
t.pendown()
t.left(90)
t.pensize(2)

def draw_tree(branch, depth):
    if branch < 3:
        t.color(random.randint(120,255), random.randint(100,200), 200)
        t.dot(10)
        return
    t.pensize(depth * 0.5)
    t.color(139, 69, 19)
    t.forward(branch)
    angle = random.randint(18, 28)
    t.right(angle)
    draw_tree(branch * 0.72, depth+1)
    t.left(angle * 2)
    draw_tree(branch * 0.72, depth+1)
    t.right(angle)
    t.backward(branch)

draw_tree(110, 1)
t.done()
