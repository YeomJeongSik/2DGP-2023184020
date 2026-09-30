from pico2d import *
from pathlib import Path

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FRAME_TIME = 0.12
REPEAT_COUNT = 5
PAUSE_TIME = 1.0


class SpriteSheet:
    def __init__(self, filename, actions, frame_width=155, frame_height=180):
        self.image = load_image(str(Path(__file__).with_name(filename)))
        self.actions = actions
        self.rows = len(actions)
        self.frame_width = frame_width
        self.frame_height = frame_height

    def frame_count(self, action):
        return len(self.actions[action][1])

    def draw_frame(self, action, frame, x, y, draw_width, draw_height):
        top, frame_x = self.actions[action]
        source_x = frame_x[frame]
        source_y = self.image.h - top - self.frame_height
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
        self.next_frame_at = get_time() + FRAME_TIME

    def update(self, now):
        if self.pause_until is not None:
            if now < self.pause_until:
                return
            self.pause_until = None
            self._advance_action()
            self.next_frame_at = now + FRAME_TIME
            return
        if now < self.next_frame_at:
            return
        self.frame += 1
        self.next_frame_at = now + FRAME_TIME
        sheet = self.sheets[self.sheet_index]
        if self.frame < sheet.frame_count(self.action):
            return
        self.frame = 0
        self.repetition += 1
        if self.repetition < REPEAT_COUNT:
            return
        self.repetition = 0
        self.pause_until = now + PAUSE_TIME

    def _advance_action(self):
        sheet = self.sheets[self.sheet_index]
        self.frame = 0
        self.action += 1
        if self.action < sheet.rows:
            return
        self.action = 0
        self.sheet_index = (self.sheet_index + 1) % len(self.sheets)

    def draw(self, x, y, draw_width, draw_height):
        self.sheets[self.sheet_index].draw_frame(
            self.action,
            self.frame,
            x,
            y,
            draw_width,
            draw_height,
        )


def get_display_size(sheet):
    scale = min(SCREEN_WIDTH / sheet.frame_width, SCREEN_HEIGHT / sheet.frame_height) * 0.75
    return int(sheet.frame_width * scale), int(sheet.frame_height * scale)


def main():
    open_canvas(SCREEN_WIDTH, SCREEN_HEIGHT)
    first_x = (200, 360, 520, 680, 840, 1000, 1140, 1293)
    second_x = (245, 409, 574, 739, 904, 1069, 1234, 1381)
    sheets = [
        SpriteSheet('1animation.png', (
            (35, first_x[:6]),       # IDLE
            (245, first_x),          # WALK
            (440, first_x),          # RUN
            (630, first_x[:6]),      # FIGHTING STANCE
            (825, (220,) + first_x[1:]),  # CHARGING: skip the row label
        )),
        SpriteSheet('2animation.png', (
            (30, second_x[:4]),
            (205, second_x),
            (425, second_x[:4]),
            (605, second_x[:4]),
            (790, second_x[:5]),
        )),
    ]
    animation = AnimationSequence(sheets)

    while True:
        now = get_time()
        animation.update(now)
        clear_canvas()
        sheet = sheets[animation.sheet_index]
        draw_width, draw_height = get_display_size(sheet)
        animation.draw(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, draw_width, draw_height)
        update_canvas()
        delay(0.01)


main()


close_canvas()
