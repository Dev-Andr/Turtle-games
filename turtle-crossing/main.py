import random
import time, obstacles
from turtle import Screen
from random import randrange as r

s = Screen()
s.setup(width=600, height=600)
s.tracer(0)

lvls = {1: 30, 2: 30, 3: 40, 4: 40, 5: 50, 6: 60}
lvl = 1
obs = obstacles.Create
obj = []
plr = obstacles.Create("turtle", (0, -280))
plr.setheading(90)

def setup():
    global obj
    if len(obj) > 0:
        obj2 = []
        for v in obj:
            v[0].goto(r(-280, 310, 25), r(-230, 270, 25))
            obj2.append([v[0], random.uniform(0.7, lvl)])
        obj = obj2[:]

    for _ in range(lvls[lvl]-len(obj)):
        t = obs("square", (r(-280, 310, 25), r(-230, 270, 25)))
        obj.append([t, random.uniform(0.7, lvl)])

    plr.goto((0,-280))

s.listen()
s.onkeypress(lambda: plr.fd(10), "Up")
s.onkeypress(lambda: plr.fd(-10), "Down")

writer = obs("circle", (0,0))
writer.hideturtle()

def score(txt):
    writer.clear()
    writer.write(txt, align="center", font=("Arial Bold", 50, "normal"))
score(f"Level {lvl}!")
setup()


def retry():
    score(f"Level {lvl}!")
    setup()
    gaem()

def gaem():
    global lvl
    game = True
    while game:
        for i in obj:
            hit = obs.move(i[0], i[1], plr)
            if hit:
                game = False
                score("Game Over! (R)")
                s.onkeypress(lambda: retry(), "r")

        if plr.ycor() >= 280:
            lvl += 1
            score(f"Level {lvl}!")
            setup()

        time.sleep(0.01)
        s.update()

gaem()
s.exitonclick()
