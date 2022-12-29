import random


class Driver:

    def __init__(self, track, name, nr):
        self.track = track
        self.name = name
        self.nr = nr
        # use from 11 to 22 percent per lap
        self.tyre_usage = random.randint(11, 22) / self.track.track_length
