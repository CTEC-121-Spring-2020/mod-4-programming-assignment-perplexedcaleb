# Module 5
#   Programming Assignment 6
#       Prob-3.py

# Caleb Howard

from graphics import *

def main():

    win = GraphWin('Archery Target',300,300)
    center = Point(150,150)
 
    whiteCircle = Circle(center, 100)
    whiteCircle.setFill('white')
    whiteCircle.draw(win)
 
    blackCircle = Circle(center, 80)
    blackCircle.setFill('black')
    blackCircle.draw(win)
 
    blueCircle = Circle(center, 60)
    blueCircle.setFill('blue')
    blueCircle.draw(win)
 
    redCircle = Circle(center, 40)
    redCircle.setFill('red')
    redCircle.draw(win)
 
    yellowCircle = Circle(center, 20)
    yellowCircle.setFill('yellow')
    yellowCircle.draw(win)
 
    win.getMouse() 
    win.close()

main()    