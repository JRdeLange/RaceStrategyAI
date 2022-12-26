class RaceControl:

    def __init__(self, track):
        self.track = track

    def order_cars(self):
        finished = []   
        racing = []
        if self.track.chequered_flag:
            for car in cars: