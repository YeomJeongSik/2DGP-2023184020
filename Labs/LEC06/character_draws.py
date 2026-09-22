# 실습 과제 진행
import math
from pico2d import*

open_canvas(800,600)

character = load_image('character.png')

x = 400
y = 300

def move_circle():
    print("Circle")
    cx = 400
    cy = 300
    R = 150
    Radius = 0
    Speed = 0.05

    while Radius <= 360:
            clear_canvas()
            x = cx + R * math.cos(Radius)
            y = cy + R * math.sin(Radius)
            character.draw(x,y)
            update_canvas()
            Radius += Speed
            delay(0.01)
    pass

def down_move(Max_index, Speed):
     for i in range(Max_index/2):
        y -= Speed

def up_move(Max_index, Speed):
     for i in range(Max_index/2):
             y += Speed
     
def left_move(Max_index, Speed):
    for i in range(Max_index/2):
            x -= Speed

def right_move(Max_index, Speed):
    for i in range(Max_index/2):
            x += Speed

def move_rectangle():
    print("Rectangle")
    Max_index = 300
    Speed = 1
    down_move(Max_index, Speed)
    left_move(Max_index, Speed)
    up_move(Max_index, Speed)
    right_move(Max_index, Speed)
    down_move(Max_index, Speed)
    clear_canvas()
    character.draw(x,y)
    update_canvas()
    pass

def move_triangle():
    print("Triangle")
    clear_canvas()
    character.draw(x,y)
    update_canvas()
    pass


while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass

close_canvas()