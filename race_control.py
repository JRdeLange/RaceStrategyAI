from track import Track


class RaceControl:

    def __init__(self, track):
        self.track = track
        self.finishing_order = []

    def tick(self):
        pass

    def finish(self, car):
        self.finishing_order.append(car)

    def track_car_laps(self):
        for car in self.track.cars:
            car.on_lap = 
