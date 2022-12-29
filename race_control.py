from track import Track
from car import Car

class RaceControl:

    def __init__(self, track):
        self.track = track
        self.track.set_race_control(self)
        self.finishing_order = []

    def tick(self):
        self.track_car_laps()

    def finish(self, car):
        self.finishing_order.append(car)

    def track_car_laps(self):
        for car in self.track.cars:
            curr_lap = car.on_lap
            car.on_lap = int(car.distance_driven / self.track.track_length)
            if curr_lap != car.on_lap:
                car.cross_finish_line()
            print(car.on_lap)
