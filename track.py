from car import Car
from driver import Driver
import utils
import data

import random
import utils


class Track:

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.timescale = 3
        self.length = 1000
        self.laps = 3
        self.race_length = self.length * self.laps
        self.curr_lap = 0

        # Flags
        self.full_course_yellow = False
        self.chequered_flag = False

    def cars_to_grid(self, n):
        print(n, len(self.drivers))
        for i in range(n):
            color = utils.random_color()
            car = Car(self.drivers[i], color, self)
            self.cars.append(car)

    def gen_drivers(self, n):
        given_numbers = []
        drivers = data.driver_names
        random.shuffle(drivers)
        idx = 0
        while len(self.drivers) < n:
            nr = random.randint(1, 99)
            if nr not in given_numbers:
                given_numbers.append(nr)
                driver = Driver(self, drivers[idx], nr)
                self.drivers.append(driver)
                idx += 1

    def tick(self):
        for car in self.cars:
            car.drive()

        self.order_cars()

        self.check_if_race_over()

    def order_cars(self):
        self.cars.sort(reverse=True, key=self.car_distance_getter)

    def car_distance_getter(self, car):
        return car.distance_driven

    def check_if_race_over(self):
        for car in self.cars:
            if not self.chequered_flag and car.distance_driven > self.race_length:
                self.chequered_flag = True
                print("finished!")
                break
