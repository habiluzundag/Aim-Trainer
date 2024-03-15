import random
import turtle
import time
turtle.register_shape("head.gif")
#turtle.Screen.register_shape("sea.gif")
turtle_instance=turtle.Turtle()
score=turtle.Turtle()
Time=turtle.Turtle()
turtle_instance.shapesize(2)
turtle_instance.shape("head.gif")
draw_board=turtle.Screen()
draw_board.bgpic("cs.gif")
draw_board.title("Aim Trainer")
#draw_board.tracer()
turtle_instance.penup()
turtle_instance.speed(0)
Time.hideturtle()
Time.penup()
Time.goto(0,250)
Time.speed(0)
#Time.write("Time: 30", align="center", font=("Arial",15,"normal"))
score.penup()
score.hideturtle()
score.speed(0)
score.goto(0, 275)
score.write("SCORE:0", align="center", font=("Arial", 20, "normal"))
def click(x, y):
    if not hasattr(click, 'sayac'):
        click.sayac = 0
    click.sayac += 1
    score.clear()
    score.write("SCORE:%s"%click.sayac, align="center", font=("Arial", 15, "normal"))
t=1
for i in range(60):
    vakit=60-i
    Time.write("Time: %s"%vakit, align="center", font=("Arial", 15, "normal"))
    x=random.randint(-250,250)
    y=random.randint(-250,250)
    #turtle_instance.goto(x,y)
    turtle_instance.setposition(x,y)
    turtle_instance.showturtle()
#turtle_instance.setx(25)
#turtle_instance.sety(100)
    t-=0.01
    time.sleep(t)
    turtle_instance.onclick(click)
    turtle_instance.hideturtle()
    time.sleep(0.1)
    Time.clear()
Time.write("Game Over!", align="center", font=("Arial", 15, "normal"))

draw_board.mainloop()