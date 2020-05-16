# Module 5
#   Programming Assignment 6
#       Prob-1.py

# <YOUR NAME>

# INSTRUCTIONS:
#   Insert a comment above each line of code in the program below to describe
#   what the code does

# importing the graphics.py file (I had to import this manually to get it to work).
from graphics import *

def main():
     # creates a window size 200 x 200
     win = GraphWin()
     # creates a circle at 50,50
     shape = Circle(Point(50,50), 20)
     # sets the circles outline to the color red
     shape.setOutline("red")
     # sets the inside of the circle to the color red
     shape.setFill("red")
     # draws the circle and colors it in
     shape.draw(win)
     for i in range(5):
          # waits for users mouse click
          p = win.getMouse()
          # centers the circle where you click your mouse
          c = shape.getCenter()
          # amount of turns for each click?
          dx = p.getX() - c.getX()
          dy = p.getY() - c.getY()
          # circle moves based off click
          shape.move(dx,dy)
          # the window closes after 4 clicks
     win.close()

main()