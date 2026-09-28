# 실습 과제 진행
import math
from pico2d import*

open_canvas(800,600)

character = load_image('character.png')

def draw_circle():
    print('원')
    for degree in range(0,360, 5):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)
        clear_canvas()
        character.draw(x,y)
        update_canvas()
        delay(0.05)
    pass

def draw_rectangle():
    print('사각형')
    pass

def draw_triangle():
    print('삼각형')

while True:
    draw_circle()
    draw_rectangle()
    draw_triangle()
    pass

close_canvas()