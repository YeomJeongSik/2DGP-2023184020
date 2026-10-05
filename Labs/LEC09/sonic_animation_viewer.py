from pathlib import Path
from collections import namedtuple

from pico2d import *


WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
CENTER_X = WINDOW_WIDTH // 2
CENTER_Y = WINDOW_HEIGHT // 2
SCALE = 4
SOURCE_HEIGHT = 525
FRAME_INTERVAL = 0.1
PAUSE_DURATION = 1.0
REPEAT_LIMIT = 5

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
	make_pixel_frames([
		(1, 29, 283, 317),
		(36, 65, 283, 317),
		(72, 110, 286, 316),
		(123, 161, 285, 316),
		(172, 210, 286, 316),
		(218, 255, 285, 316),
	]),
	make_pixel_frames([
		(1, 24, 326, 370),
		(31, 59, 327, 370),
		(65, 84, 327, 370),
		(90, 114, 327, 369),
		(119, 143, 327, 369),
		(149, 168, 327, 370),
		(184, 223, 341, 368),
		(232, 270, 341, 367),
	]),
	make_pixel_frames([
		(1, 27, 379, 416),
		(31, 61, 379, 414),
		(64, 94, 379, 414),
		(99, 131, 377, 414),
		(136, 167, 379, 414),
		(176, 208, 379, 414),
		(217, 249, 379, 414),
		(254, 286, 378, 413),
	]),
	make_pixel_frames([
		(6, 39, 429, 468),
		(49, 82, 426, 468),
		(96, 118, 427, 465),
		(125, 147, 427, 465),
	]),
]


class AnimationPlayer:
	def __init__(self, animations):
		self.animations = animations
		self.animation_index = 0
		self.frame_index = 0
		self.repeat_count = 0
		self.state = "playing"
		self.elapsed_time = 0.0

	@property
	def current_animation(self):
		return self.animations[self.animation_index]

	@property
	def current_frame(self):
		return self.current_animation[self.frame_index]

	def update(self, delta_time):
		self.elapsed_time += delta_time
		if self.state == "waiting":
			if self.elapsed_time >= PAUSE_DURATION:
				self.animation_index = (self.animation_index + 1) % len(self.animations)
				self.frame_index = 0
				self.repeat_count = 0
				self.elapsed_time = 0.0
				self.state = "playing"
			return

		while self.elapsed_time >= FRAME_INTERVAL:
			self.elapsed_time -= FRAME_INTERVAL
			self.frame_index += 1
			if self.frame_index >= len(self.current_animation):
				self.frame_index = 0
				self.repeat_count += 1
				if self.repeat_count >= REPEAT_LIMIT:
					self.frame_index = len(self.current_animation) - 1
					self.elapsed_time = 0.0
					self.state = "waiting"
					break


def get_sprite_path():
	return Path(__file__).with_name("sonic-sprite.png")


open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)
sprite_sheet = load_image(str(get_sprite_path()))
animation_player = AnimationPlayer(ANIMATIONS)
running = True
previous_time = get_time()

while running:
	for event in get_events():
		if event.type == SDL_QUIT:
			running = False

	current_time = get_time()
	animation_player.update(current_time - previous_time)
	previous_time = current_time

	clear_canvas()
	frame = animation_player.current_frame
	sprite_sheet.clip_draw(
		frame.left,
		frame.bottom,
		frame.width,
		frame.height,
		CENTER_X,
		CENTER_Y,
		frame.width * SCALE,
		frame.height * SCALE,
	)
	update_canvas()

close_canvas()
