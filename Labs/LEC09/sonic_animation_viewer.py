from pico2d import *


WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800


open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)
running = True

while running:
	for event in get_events():
		if event.type == SDL_QUIT:
			running = False

	clear_canvas()
	update_canvas()

close_canvas()
