import pygame
import random


'''
800 x 400
cars have 400/20=20 pixels space, are 16 high
movable space is 800 - length, so for 16 / 2 * 5.5 = 44 that means
movable space is 800 - 44 = 756
'''


class Renderer:

    def __init__(self, track):
        self.track = track
        self.width = 1200
        self.height = 400
        self.window = None
        self.clock = None
        self.show_tyre_condition = True

        self.init_pygame()
        self.running = True

    def init_pygame(self):
        pygame.init()
        self.window = pygame.display.set_mode([self.width, self.height])
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("RSAI v0.1")

    def tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.clear()
        self.draw()
        pygame.display.flip()
        self.clock.tick(60)

    def clear(self):
        self.window.fill((255, 255, 255))

    def draw(self):
        self.draw_lines()

        for idx, car in enumerate(self.track.cars):
            self.draw_car(idx, car)

    def draw_lines(self):
        step_size = self.height / len(self.track.cars)
        y_offset = step_size / 2
        color = [0, 0, 0]
        for idx in range(len(self.track.cars)):
            start_x = self.track.cars[0].width / 2
            end_x = self.width - self.track.cars[0].width / 2

            y = y_offset + step_size * idx

            start = [start_x, y]
            end = [end_x, y]

            self.draw_line(start, end, color, 2)

    def draw_line(self, start, end, color, width=1):
        pygame.draw.line(self.window, color, start, end, width)

    def draw_car(self, idx, car):
        x, y = self.get_car_coordinates(idx, car)
        self.draw_rect(x, y, car.width, car.height, car.color)
        if self.show_tyre_condition:
            self.draw_tyre_condition(x, y, car)

    def draw_tyre_condition(self, x, y, car):
        x_start = x - car.width / 2
        x_end = x_start + car.width / 100 * car.tyres
        y = y + car.height / 2 - 4
        self.draw_line([x_start, y], [x_end, y], [100, 100, 180], 3)

    def get_car_coordinates(self, idx, car):
        x_min = car.width / 2
        x_max = self.width - car.width / 2
        x = x_min + ((x_max - x_min) / self.track.track_length) * (car.distance_driven % self.track.track_length)
        if car.distance_driven > self.track.race_length:
            x = x_max

        step_size = self.height / len(self.track.cars)
        y_offset = step_size / 2
        y = y_offset + step_size * idx
        return int(x), int(y)

    def draw_rect(self, x, y, width, height, color):
        rect = self.make_rect(x, y, width, height)
        pygame.draw.rect(self.window, color, rect)

    def make_rect(self, x, y, width, height):
        x = x - width / 2
        y = y - height / 2
        return pygame.Rect(x, y, width, height)
