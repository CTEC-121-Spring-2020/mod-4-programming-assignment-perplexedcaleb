# Module 5
#   Programming Assignment 6
#       Prob-2.py

# <YOUR NAME>

from graphics import *

def main():
     # creating window and rectangle
     win = GraphWin()
     rect = Rectangle(Point(60, 60), Point(140, 140))
     rect.setOutline("red")
     rect.setFill("red")
     rect.draw(win)

     # telling rectangle where to go based off clicks
     for i in range(5):
          p = win.getMouse()
          c = rect.getCenter()
          dx = p.getX() - c.getX()
          dy = p.getY() - c.getY()
          rect.move(dx,dy)
          print("Click again to quit")
     win.close()

main()