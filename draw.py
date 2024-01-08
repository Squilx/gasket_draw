import turtle
import math
from PIL import ImageGrab
import os

class Gasket:
    def __init__(self, sku, outside_diameter, inside_diameter, pcd=None, holes=None, hole_diameter=None,
                 pb_width=None, pb_shape=None, colour=None):
        self.sku = sku
        self.outside_diameter = outside_diameter
        self.inside_diameter = inside_diameter
        self.pcd = pcd
        self.holes = holes
        self.hole_diameter = hole_diameter
        self.pb_width = pb_width
        self.pb_shape = pb_shape
        self.colour = colour

        if self.outside_diameter > 900 or self.outside_diameter < 500:
            ratio = 900 / self.outside_diameter
            self.outside_diameter = self.outside_diameter * ratio
            if self.inside_diameter: self.inside_diameter = self.inside_diameter * ratio
            if self.pcd: self.pcd = self.pcd * ratio
            if self.hole_diameter: self.hole_diameter = self.hole_diameter * ratio
            if self.pb_width: self.pb_width = self.pb_width * ratio


    def draw(self):
        # get the screen
        screen = turtle.getscreen()
        screen.setup(width=self.outside_diameter + 40, height=self.outside_diameter + 40)
        #create the turtle
        t = turtle.Turtle()
        t.speed(0)

        # draw the outside of the gasket
        if self.colour:
            t.dot(self.outside_diameter, self.colour)
        else:
            t.dot(self.outside_diameter, "grey")
        # draw the inside of the gasket
        t.dot(self.inside_diameter, "white")

        #draw the holes
        if self.pcd and self.holes and self.hole_diameter:
            degrees = float((360 / self.holes))
            for hole in range(self.holes):
                t.penup()
                t.forward((self.pcd / 2))
                t.dot(self.hole_diameter, "white")
                t.goto(0,0)
                t.right(degrees)
        if self. pb_width and self.pb_shape == "T":
            edge = ((self.outside_diameter - self.inside_diameter) / 2)
            start_x = 0 - (self.pb_width / 2)
            start_y = 0 + (self.pb_width / 2)
            t.goto(start_x, start_y)
            t.fillcolor("grey")
            t.pencolor("grey")
            t.showturtle()
            t.speed(10)
            t.pendown()
            t.begin_fill()
            t.setheading(0)
            t.forward(self.pb_width)
            t.setheading(270)
            t.forward((self.inside_diameter / 2) + edge/2)
            t.setheading(180)
            t.forward(self.pb_width)
            t.setheading(90)
            t.forward((self.inside_diameter / 2) + edge/2)
            t.end_fill()
            edge = ((self.outside_diameter - self.inside_diameter) / 2)
            start_x = 0 - ((self.inside_diameter / 2) + (edge/4))
            start_y = 0 - (self.pb_width / 2)
            t.penup()
            t.goto(start_x, start_y)
            t.pendown()
            t.begin_fill()
            t.setheading(90)
            t.forward(self.pb_width)
            t.setheading(0)
            t.forward(self.inside_diameter + edge/2)
            t.setheading(270)
            t.forward(self.pb_width)
            t.setheading(180)
            t.forward(self.inside_diameter + edge/2)
            t.end_fill()
        elif self.pb_width:
            edge = ((self.outside_diameter - self.inside_diameter) / 2)
            start_x = 0 - ((self.inside_diameter / 2) + (edge/4))
            start_y = 0 - (self.pb_width / 2)
            t.goto(start_x, start_y)
            t.fillcolor("grey")
            t.pencolor("grey")
            t.showturtle()
            t.speed(10)
            t.pendown()
            t.begin_fill()
            t.setheading(90)
            t.forward(self.pb_width)
            t.setheading(0)
            t.forward(self.inside_diameter + edge/2)
            t.setheading(270)
            t.forward(self.pb_width)
            t.setheading(180)
            t.forward(self.inside_diameter + edge/2)
            t.end_fill()

        t.hideturtle()
        # Capture the canvas
        canvas = screen.getcanvas()

        # Save the canvas as a JPG image
        canvas.postscript(file="temp.eps")  # Save as EPS file
        img = ImageGrab.grab(bbox=(
        canvas.winfo_rootx(), canvas.winfo_rooty(), canvas.winfo_rootx() + canvas.winfo_width(),
        canvas.winfo_rooty() + canvas.winfo_height()))

        directory = "gasket/static/"
        file_name = f"{self.sku}.jpg"
        file_path = directory + file_name
        if not os.path.exists(directory):
            os.makedirs(directory)
        try:
            img.save(f"gasket/static/{self.sku}.jpg", "JPEG")
        except Exception as e:
            print(f"Error: {e}")
