import math
from pico2d import*

open_canvas(800,600)
character = load_image('character.png')

def draw_character(x,y):
    clear_canvas()
    character.draw(x,y)
    update_canvas()
    delay(0.05)

# 실습 과제 진행
def draw_circle():
    print("Circle")

    for degree in range(0,360,5):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)
        draw_character(x, y)
    pass

def draw_rectangle():
    print("Rectangle")
    move_top()
    #move_right()
    #move_bottom()
    move_left()
    pass

def move_top():
    print('TOP')
    for x in range(50,750,5):
        draw_character(x, 550)

    pass



def move_right():
    print('RIGHT')
    for y in range(550, 50, -5):
        draw_character(750, y)
    pass

def move_bottom():
    print('BOTTOM')
    for x in range(750, 50, -5):
        draw_character(x, 50)
    pass

def move_left():
    print('LEFT')
    for y in range(50, 550, 5):
        draw_character(50, y)
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