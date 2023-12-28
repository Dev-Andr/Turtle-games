from turtle import Turtle, Screen
import random, time
from datetime import datetime
random.seed(datetime.now().timestamp())

s = Screen()
s.setup(width=500, height=400)
bet = s.textinput(title="Make your bet", prompt="Which turtle will win?")

Turs = []
for i in range(7):
    t = Turtle(shape="turtle")
    Turs.append(t)

def start(a):

    colors = ['Black', 'Red', 'Green', 'Yellow', 'Blue', 'Magenta', "Orange"]
    yList = [-60,-90,-30,0,30,90,60]

    for t in Turs:
        t.penup()
        choice = random.choice(colors)
        t.color(choice)
        colors.remove(choice)

        yPos = random.choice(yList)
        t.goto(-240,yPos)
        yList.remove(yPos)

    b=1
    while b:
        for i in Turs:
            i.fd(random.randint(-10,35))
            if i.xcor() >= 220:
                if a == i.color()[0]:
                    print("Your turtle has won!")
                else:
                    print(i.color()[0],"has won the race. Better luck next time!")
                time.sleep(5)
                b=0
                s.reset()
                start("")

start(bet)
s.listen()
s.exitonclick()