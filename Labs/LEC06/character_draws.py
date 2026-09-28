import math
from pico2d import*

# 실습 과제 진행
def draw_circle():
    print("Circle")

    for degree in range(0,360,5):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)
        clear_canvas()
        character.draw(x,y)
        update_canvas()
        delay(0.05)
    pass

def draw_rectangle():
    print("Rectangle")
    pass

def draw_triangle():
    print("Triangle")
    pass


while True:
    draw_circle()
    draw_rectangle()
    draw_triangle()
    pass