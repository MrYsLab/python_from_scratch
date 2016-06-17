"""
Copyright (c) 2016 Alan Yorinks All right reserved.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

# 1_hello_square.py

# This file draws 2 sides of a square
# Get the turtle library
import turtle

# Create a turtle who's name is "t"
t = turtle.Turtle()

# The default shape for the turtle is an arrow. Let's change it to a turtle
t.shape('turtle')

# Your code goes here

# point the turtle to face east
t.seth(0)

# move the turtle forward 150 units
t.fd(150)

# point the turtle to face north
t.seth(90)

# move the turtle 150 units
t.fd(150)

# point the turtle to face west
t.seth(180)

# move the turtle forward 150 units
t.fd(150)

# point the turtle to face south
t.seth(270)

# move the turtle forward 150 units
t.fd(150)

# point the turtle to face east
t.seth(0)


# This line leaves the screen open for us to see the results
t.screen.exitonclick()
