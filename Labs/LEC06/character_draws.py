# 실습 과제 진행
import math
from pico2d import*

open_canvas(800,600)

character = load_image('character.png')

x = 400
y = 300

def move_circle():
    global x,y
    print("Circle")
    cx = 400
    cy = 300
    R = 150
    Angle = 0.0
    Radius = 0
    Speed = 1

    while Angle <= 360:
            clear_canvas()
            Radius = math.radians(Angle)
            x = cx + R * math.cos(Radius)
            y = cy + R * math.sin(Radius)
            character.draw(x,y)
            update_canvas()
            Angle += Speed
            delay(0.01)
    pass

def down_move(Max_index, Speed):
     global y
     for i in range(Max_index//Speed):
        y -= Speed
        clear_canvas()
        character.draw(x,y)
        update_canvas()
        delay(0.01)

def up_move(Max_index, Speed):
     global y
     for i in range(Max_index//Speed):
             y += Speed 
             clear_canvas()
             character.draw(x,y)
             update_canvas()
             delay(0.01)
                 
def left_move(Max_index, Speed):
    global x
    for i in range(Max_index//Speed):
            x -= Speed
            clear_canvas()
            character.draw(x,y)
            update_canvas()
            delay(0.01)

def right_move(Max_index, Speed):
    global x
    for i in range(Max_index//Speed):
            x += Speed
            clear_canvas()
            character.draw(x,y)
            update_canvas()
            delay(0.01)

def move_rectangle():
    print("Rectangle")
    Max_index = 300
    Speed = 5
    up_move(Max_index//2, Speed)
    left_move(Max_index, Speed)
    down_move(Max_index, Speed)
    right_move(Max_index, Speed)
    up_move(Max_index//2, Speed)
    pass

def move_triangle():
    print("Triangle")
    global x,y
    Speed = 2
    width = 300
    height = 150

    for n in range((width//2)//Speed):
        x -= Speed
        y += Speed * (height / (width//2))
        clear_canvas()
        character.draw(x,y)
        update_canvas()

    for n in range((width//2)//Speed):
         pass


while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass

close_canvas()