import random


class Driver:

    def __init__(self, track, name, nr):
        self.track = track
        self.name = name
        self.nr = nr
        # use from 33 to 67 percent per race
        self.tyre_usage = random.randint(33, 67) / self.track.race_length
