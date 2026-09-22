# 실습 과제 진행

from pico2d import*

open_canvas(800,600)

character = load_image('character.png')

x = 400
y = 300

def move_circle():
    print("Circle")
    clear_canvas()
    character.draw(400,300)
    update_canvas()
    pass

def move_rectangle():
    print("Rectangle")
    clear_canvas()
    character.draw(400,300)
    update_canvas()
    pass

def move_triangle():
    print("Triangle")
    clear_canvas()
    character.draw(400,300)
    update_canvas()
    pass


while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass

close_canvas()