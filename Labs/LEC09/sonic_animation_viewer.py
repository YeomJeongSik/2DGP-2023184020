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


def make_pixel_frames(boxes):
	return [
		Frame(left, SOURCE_HEIGHT - bottom - 1, right - left + 1, bottom - top + 1)
		for left, right, top, bottom in boxes
	]


ANIMATIONS = [
	make_pixel_frames([
		(1, 31, 39, 77),
		(32, 63, 40, 77),
		(64, 95, 39, 77),
		(96, 127, 40, 77),
		(128, 159, 40, 77),
		(160, 191, 40, 77),
		(192, 223, 40, 77),
		(224, 255, 39, 76),
		(256, 287, 42, 76),
		(288, 319, 48, 76),
		(320, 330, 51, 76),
	]),
	make_pixel_frames([
		(8, 33, 80, 116),
		(37, 63, 80, 116),
		(65, 95, 80, 117),
		(97, 133, 80, 116),
		(135, 166, 80, 114),
		(170, 201, 79, 116),
		(206, 231, 79, 116),
		(238, 261, 80, 116),
		(263, 292, 80, 116),
		(295, 330, 80, 116),
		(334, 365, 80, 115),
		(370, 398, 79, 116),
	]),
	make_pixel_frames([
		(1, 33, 124, 163),
		(39, 73, 124, 162),
		(89, 123, 125, 162),
		(130, 163, 121, 162),
		(181, 214, 122, 162),
		(228, 260, 122, 161),
	]),
	make_pixel_frames([
		(1, 29, 169, 198),
		(35, 63, 167, 197),
		(67, 96, 169, 197),
		(98, 128, 169, 197),
		(131, 159, 168, 197),
		(162, 190, 168, 198),
		(193, 222, 170, 198),
		(230, 260, 170, 198),
		(268, 297, 170, 199),
	]),
	make_pixel_frames([
		(1, 30, 206, 232),
		(36, 64, 206, 232),
		(70, 98, 206, 232),
		(105, 133, 206, 232),
		(139, 167, 206, 232),
		(174, 202, 206, 232),
	]),
	make_pixel_frames([
		(1, 29, 239, 273),
		(36, 65, 239, 273),
		(74, 104, 239, 273),
		(111, 141, 238, 273),
		(149, 178, 239, 273),
		(186, 216, 238, 273),
	]),
]


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
