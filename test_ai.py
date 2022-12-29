class TestAI:

    def __init__(self, track, race_control):
        self.track = track
        self.race_control = race_control

    def tick(self):
        for car in self.track.cars:
            if car.tyres < 50 and not car.pit_in:
                car.pit_this_lap()
