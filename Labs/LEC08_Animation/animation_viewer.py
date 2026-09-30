from pico2d import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FRAME_TIME = 0.12
REPEAT_COUNT = 5
PAUSE_TIME = 1.0


class SpriteSheet:
	def __init__(self, filename, columns, rows):
		self.filename = filename
		self.columns = columns
		self.rows = rows


open_canvas()


close_canvas()