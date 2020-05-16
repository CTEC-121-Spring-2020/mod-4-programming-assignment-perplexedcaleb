# Module 5
#   Programming Assignment 6
#       Prob-7.py

# <YOUR NAME>

from graphics import *

def main():

    #head
    win = GraphWin('Face',300,300)
    head = Oval(Point(75,50),Point(225,250))
    head.setFill('red')
    head.draw(win)
 
    #eyes
    eyeballLeft = Circle(Point(120,120),15)
    eyeballLeft.setFill('white')
    eyeballLeft.draw(win)
    ebl = Circle(Point(120,120),5)
    ebl.setFill('green')
    ebl.draw(win)
 
    eyeballRight = Circle(Point(180,120),15)
    eyeballRight.setFill('white')
    eyeballRight.draw(win)
    ebr = Circle(Point(180,120),5)
    ebr.setFill('green')
    ebr.draw(win)
 
    #mouth
    mustache = Oval(Point(110,185),Point(190,225))
    mustache.setFill('black')
    mustache.draw(win)
 
    #nose
    nose = Oval(Point(125,110),Point(175,190))
    nose.setFill('red')
    nose.draw(win)
 
    win.getMouse()
    win.close()
    


main()