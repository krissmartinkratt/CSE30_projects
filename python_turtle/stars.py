#Write a program named stars.py that has two functions for generating star polygons. One function should be based on iteration (a for loop), and another function should be based on recursion. 

import turtle

def star(size,n,d=2):
    global t
    for i in range(n):
        t.pendown()
        angle = 180 - (180 * (d - 1) / n)
        t.fd(size)
        t.rt(angle)

def star_recursive(size,n,level,d=2):
    global t
    if level == 0:
        return
    else:
        star(size,n)
        star_recursive(size/2,n,level-1)

# main program
if __name__ == '__main__':

    s = turtle.Screen()     
    s.setup(800, 400)
    s.bgcolor("white")
    s.title("Turtle Program")

    t = turtle.Turtle()     
    t.shape("turtle")  
    t.pen(pencolor='dark violet',fillcolor='dark violet', pensize=3, speed=1)

    t.penup()
    t.goto(-150, 0)         
    star(100, 5, 2) # should draw a purple pentagram (5-pointed star)
    
    t.penup()
    t.goto(150, 0)
    t.color('red')
    t.pendown()
    star_recursive(100, 8, 8, 3) # should draw a red octogram (8-pointed star)