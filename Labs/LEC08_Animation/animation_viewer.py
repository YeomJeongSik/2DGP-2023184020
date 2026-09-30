from pico2d import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FRAME_TIME = 0.12
REPEAT_COUNT = 5
PAUSE_TIME = 1.0


class SpriteSheet:
	def __init__(self, filename, columns, rows):
		self.filename = filename
		self.image = load_image(filename)
		self.columns = columns
		self.rows = rows
		self.frame_width = self.image.w // columns
		self.frame_height = self.image.h // rows

	def draw_frame(self, action, frame, x, y, draw_width, draw_height):
		source_x = frame * self.frame_width + self.frame_width // 2
		source_y = action * self.frame_height + self.frame_height // 2
		self.image.clip_draw(
			source_x,
			source_y,
			self.frame_width,
			self.frame_height,
			x,
			y,
			draw_width,
			draw_height,
		)


class AnimationSequence:
	def __init__(self, sheets):
		self.sheets = sheets
		self.sheet_index = 0
		self.action = 0
		self.frame = 0
		self.repetition = 0
		self.pause_until = None
		self.next_frame_at = get_time()


open_canvas()


close_canvas()