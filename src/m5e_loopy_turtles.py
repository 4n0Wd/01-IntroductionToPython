"""
Demonstrates:
  -- LOOPS (doing something repeatedly) and
  -- using OBJECTS
via Turtle Graphics.

Concepts include:
 * Using OBJECTS:
   -- CONSTRUCT an INSTANCE of a CLASS (we call such instances OBJECTS).
   -- Make an object  ** DO **  something by using a METHOD.
   -- Reference an object's  ** DATA **  by using an INSTANCE VARIABLE.

 * LOOPS:
   -- Using a FOR expresssion like this:
         for k in range(41):
             blah
             blah
             blah

     The above repeats the body of the FOR expression 41 times.
     The name  k  is:
            0 the first time the body runs,
       then 1 the next time the body runs,
       then 2 the next time the body runs,
         etc
       then 40 the last time the body runs.

 * ASSIGNMENT and NAMES
  -- ASSIGNING a VALUE to a NAME (aka VARIABLE), as in these examples:
        jack = 45
        jill = 'ran down the hill'
        size = size - 12

 * The DOT trick: Type expressions like the following,
     pausing after typing the DOT (period, full stop).
     The window that pops up give lots of clues for what you can do!
        rg.
        rg.SimpleTurtle().
        rg.Pen().
        rg.PaintBucket().

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         and their colleagues.
"""
import rosegraphics as rg

window = rg.TurtleWindow()

blue_turtle = rg.SimpleTurtle('turtle')
blue_turtle.pen = rg.Pen('midnight blue', 3)
blue_turtle.speed = 80  # Fast

# The first square will be 300 x 300 pixels:
size = 300
sizec = 140

red_turtle = rg.SimpleTurtle('turtle')
red_turtle.pen = rg.Pen('red', 10)
red_turtle.speed = 40  # slower

for k in range (10):

    red_turtle.draw_circle(sizec)
    red_turtle.pen_up()
    red_turtle.left(90)
    red_turtle.forward(10)
    red_turtle.right(90)
    red_turtle.pen_down()
    sizec = sizec - 10

# Do the indented code 13 times.  Each time draws a square.
for k in range(15):

    # Put the pen down, then draw a square of the given size:
    blue_turtle.draw_square(size)

    # Move a little below and to the right of where the previous
    # square started.  Do this with the pen up (so nothing is drawn).
    blue_turtle.pen_up()
    blue_turtle.right(45)
    blue_turtle.forward(10)
    blue_turtle.left(45)

    # Put the pen down again (so drawing resumes).
    # Make the size for the NEXT square be 12 pixels smaller.
    blue_turtle.pen_down()
    size = size - 12

green_turtle = rg.SimpleTurtle('turtle')
green_turtle.pen = rg.Pen('green', 4)
green_turtle.speed = 5

sizep = 100
for k in range (5):
    green_turtle.draw_regular_polygon(5, sizep)
    green_turtle.pen_up()
    green_turtle.left(72)
    green_turtle.forward(10)
    green_turtle.right(72)
    green_turtle.pen_down()


    sizep = sizep - 10



window.close_on_mouse_click()
