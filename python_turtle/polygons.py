#Write a program named polygons.py that has two functions for generating convex regular polygons. One function should be based on iteration (a for loop), and another function should be based on recursion. 

import turtle 

def polygon(size,n):
    ''' creates one polygon'''
    global t
    t.pendown()
    turns =360/n
    for i in range(n):
        t.fd(size)
        t.rt(turns)

def polygon_recursive(size,n,level):
    ''' Constantly creates a polygon
        size is the size of the polygon 
        n is the number of sides
        level is the level of recursion
    '''
    if level == 0:
        return
    else:
        polygon(size,n)
        polygon_recursive(size/2,n,level-1)

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
    polygon(100, 5) # should draw a purple pentagon
    
    t.penup()
    t.goto(150, 0)
    t.color('red')
    t.pendown()
    polygon_recursive(100, 5, 5) # should draw a red pentagon