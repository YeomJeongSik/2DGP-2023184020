from pico2d import *


def stay_character(name) :
    
    frame = 0
    while True:
        clear_canvas()
        grass.draw(400,30)
        name.clip_draw(
            frame * 100, 300,
            100, 100, x, 90
                )
        update_canvas()
        frame = frame + 1
        if frame % 8 == 0:
            break
        delay(0.1)

def stay_reverse_character() :
    pass

def run_character() :
    pass

def run_reverse_character():
    pass

open_canvas()

grass = load_image('grass.png')
boy = load_image('animation_sheet.png')



for x in range(0, 800, 5) :
    
    
    stay_character(boy)
    run_character(boy)
    stay_reverse_character(boy)
    run_reverse_character(boy)

    

close_canvas()

