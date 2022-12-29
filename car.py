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

    def drive(self):
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

    def pit(self):
        self.pit_in = True
