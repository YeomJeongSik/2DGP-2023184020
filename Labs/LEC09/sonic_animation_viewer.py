from pathlib import Path
from collections import namedtuple

from pico2d import *


WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
CENTER_X = WINDOW_WIDTH // 2
CENTER_Y = WINDOW_HEIGHT // 2
SCALE = 4
SOURCE_HEIGHT = 525

Frame = namedtuple("Frame", "left bottom width height")


def make_box_frames(top, bottom, boxes):
	source_bottom = SOURCE_HEIGHT - bottom - 1
	return [
		Frame(left, source_bottom, right - left + 1, bottom - top + 1)
		for left, right in boxes
	]


ANIMATIONS = []


def get_sprite_path():
	return Path(__file__).with_name("sonic-sprite.png")


open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)
sprite_sheet = load_image(str(get_sprite_path()))
running = True

while running:
	for event in get_events():
		if event.type == SDL_QUIT:
			running = False

	clear_canvas()
	sprite_sheet.clip_draw(
		0,
		SOURCE_HEIGHT - 78,
		32,
		40,
		CENTER_X,
		CENTER_Y,
		32 * SCALE,
		40 * SCALE,
	)
	update_canvas()

close_canvas()
