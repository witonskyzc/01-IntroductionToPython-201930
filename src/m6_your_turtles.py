"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Zach Witonsky.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.

import rosegraphics as rg

window = rg.TurtleWindow()

###############################################################################
# Picture 1.
###############################################################################
turtle1 = rg.SimpleTurtle()
turtle1.pen = rg.Pen('black', 3)
turtle1.speed = 100

size = 150

for k in range(10):

    turtle1.draw_circle(size)

    turtle1.pen_up()
    turtle1.right(45)
    turtle1.forward(10)
    turtle1.left(45)

    turtle1.pen_down()
    size = size - 12

###############################################################################
# Picture 2.
###############################################################################
window.tracer(10)  # Bigger numbers make the animation run faster

turtle2 = rg.SimpleTurtle()
turtle2.pen = rg.Pen('red', 3)
turtle2.speed = 10

turtle2.backward(50)

for k in range(500):
    turtle2.left(91)
    turtle2.forward(k)

window.close_on_mouse_click()
########################################################################
