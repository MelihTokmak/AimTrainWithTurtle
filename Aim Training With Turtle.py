import random
import turtle
from random import randint
import time

#codes for screen and bg
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("gray")
turtle_screen.title("Aim Training With Turtle")
turtle_screen.setup(800, 600)

win_height = 600
win_width = 800

#score
score = 0
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.color("white")
score_writer.goto(0, win_height // 2 - 40)
score_writer.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

def update_display():
    score_writer.clear()
    score_writer.goto(0, win_height // 2 - 40)
    score_writer.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))
    score_writer.goto(0, win_height // 2 - 80)
    score_writer.write(f"Time left: {counter}", align="center", font=("Arial", 24, "normal"))

#timer
counter = 10
timer_running = True

def countdown():
    global counter, timer_running
    score_writer.clear()

    if counter <= 0:
        timer_running = False
        score_writer.goto(0, 0)
        score_writer.write(f"Time's up! Final Score: {score}", align="center", font=("Arial", 24, "normal"))


    else:
        counter -= 1
        update_display()
        turtle.ontimer(countdown, 1000)


#target
target = turtle.Turtle()
target.speed(0)
target.color("red")
target.shape("circle")
target.shapesize(stretch_wid=1, stretch_len=1)
target.penup()

def target_move(x, y):
    if not timer_running:
        return

    new_x = random.randint(-win_width // 2 +30, +win_width // 2 -30)
    new_y = random.randint(-win_height // 2 +30, +win_height // 2 -30)
    target.goto(new_x, new_y)
    global score
    score_writer.clear()
    score += 1
    score_writer.goto(0, win_height // 2 - 40)
    score_writer.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))
    update_display()

def restart_game():
    global score, counter, timer_running
    score = 0
    counter = 10
    timer_running = True
    target.hideturtle()  # Hide the target during reset
    turtle.ontimer(countdown, 1000)
    update_display()
    target.showturtle()

target.onclick(lambda x, y: target_move(x, y))
turtle.ontimer(countdown, 1000)
target.onclick(target_move)
turtle_screen.listen()
turtle_screen.onkey(restart_game, "r")
update_display()

turtle.mainloop()