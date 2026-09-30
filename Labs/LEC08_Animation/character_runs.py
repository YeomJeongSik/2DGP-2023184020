from pico2d import *


def stay_character() :
    pass

def stay_reverse_character() :
    pass

def run_character() :
    pass

def run_reverse_character():
    pass

open_canvas()

grass = load_image('grass.png')
boy = load_image('run_animation.png')


frame = 0

for x in range(0, 800, 5) :
    clear_canvas()
    grass.draw(400,30)
    boy.clip_composite_draw(
        100 * frame, 0, 
        100, 100,
        0, 'h',
        x,90,
        100,100
    )
    stay_character()
    run_character()
    stay_reverse_character()
    run_reverse_character()

    update_canvas()

    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()

