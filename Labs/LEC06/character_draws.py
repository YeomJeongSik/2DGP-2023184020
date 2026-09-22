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

    while Radius <= 360:
            clear_canvas()
            x = cx + R * math.cos(Radius)
            y = cy + R * math.sin(Radius)
            character.draw(x,y)
            update_canvas()
            Radius += 0.05
            delay(0.01)
    pass

def move_rectangle():
    print("Rectangle")
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