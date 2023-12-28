from turtle import Turtle
import random

def clr():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"#{r:02x}{g:02x}{b:02x}"

class Create(Turtle):
    def __init__(self,shp, pos):
        super().__init__()
        self.shape(shp)
        self.color(clr())
        self.penup()
        self.goto(pos)
        self.setheading(180)

    def move(self, step, plr):
        self.fd(step)
        if self.xcor() < -320:
            self.goto(320, self.ycor())
            self.color(clr())

        if self.distance(plr) <= 20:
            print("over")
            return True
