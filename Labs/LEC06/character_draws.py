import math
from pico2d import*

open_canvas(800,600)
character = load_image('character.png')

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
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass

def move_top():
    print('TOP')
    for x in range(50,750,5):
        clear_canvas()
        character.draw(x,550)
        update_canvas()
        delay(0.05)

    pass

def move_right():
    print('RIGHT')
    pass

def move_bottom():
    print('BOTTOM')
    pass

def move_left():
    print('LEFT')
    pass

def draw_triangle():
    print("Triangle")
    pass


while True:
    #draw_circle()
    draw_rectangle()
    draw_triangle()
    pass

close_canvas()