import random
import time


class Car:

    def __init__(self, driver, color, track):
        self.nr = driver.nr
        self.driver = driver
        self.color = color
        self.track = track
        self.finished = False
        self.on_lap = 0

        self.fuel = 100
        self.tyres = 100
        self.car_base_speed = random.randint(150, 200)
        self.distance_driven = 0
        self.width = 44
        self.height = 16

        self.pit_in = False
        self.pit_timer = 0

    def drive(self):
        if self.pit_timer <= 0:
            # Speed in kmh
            speed = (self.car_base_speed + self.tyres) + 25 - random.randint(0, 50)
            # Race over, drive slowly
            if self.distance_driven > self.track.race_length:
                speed = 100

            # 60 fps, so kmh -> m per frame is * 1000 / 60(min) / 60(sec) / 60(fps) = / 216
            speed /= 216

            # apply timescale
            speed *= self.track.timescale

            # wear tyres by distance driven this frame
            self.tyres -= self.driver.tyre_usage * speed

            # drive
            self.distance_driven += speed
        else:
            self.pit_timer -= 1/60
            if self.pit_timer <= 0:
                self.pit_in = False
                self.tyres = 100

    def pit_this_lap(self):
        if not self.finished:
            self.pit_in = True

    def cross_finish_line(self):
        if self.track.chequered_flag:
            self.finished = True
        if self.pit_in:
            self.pit_timer = 4
