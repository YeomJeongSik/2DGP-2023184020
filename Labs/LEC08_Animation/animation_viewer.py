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


open_canvas()


close_canvas()